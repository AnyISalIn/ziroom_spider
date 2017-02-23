from bs4 import BeautifulSoup as bs
import re
import requests
import grequests
import gevent
from models import House, Subway, session
from sqlalchemy import desc
from logger import Logger

price_pattern = r'￥(?P<price>\d+)\(.*'
o = re.compile(price_pattern)


class ZiroomSpider:
    def __init__(self, url, page=1):
        self.url = url
        self.data = requests.get(url, params={'p': page}).text
        self.bs = bs(self.data, 'lxml')

    def __get_pages(self):
        return self.bs.find_all('div', attrs={'class': 'pages'})[0].find_all('a')[-2].text

    def __houses(self, all=False):
        if all is True:
            pages = int(self.__get_pages())
            result = []
            urls = [grequests.get(self.url, params={'p': p}) for p in range(1, pages + 1)]
            res = grequests.map(urls)
            for r in res:
                async_bs = bs(r.text, 'lxml')
                houses = async_bs.find_all('ul', attrs={'id': 'houseList'})[0]
                result.append(houses.find_all('li', attrs={'class': 'clearfix'}))
            result = [item for sublist in result for item in sublist]
            return result
        houses = self.bs.find_all('ul', attrs={'id': 'houseList'})[0]
        return houses.find_all('li', attrs={'class': 'clearfix'})

    def __get_price(self, house):
        m = o.search(house.find_all('p', attrs={'class': 'price'})[0].text.replace(' ', '').replace('\n', ''))
        return int(m.groupdict().get('price'))

    def __get_location(self, house):
        return house.find_all('h3')[0].text

    def __get_subway(self, house):
        return house.find_all('h4')[0].text

    def __get_subway_distance(self, house):
        for item in house.find_all('div', attrs={'class': 'detail'})[0].find_all('p'):
            if '距离' in item.text:
                return item.text

    def __get_area(self, house):
        return float(house.p.span.text.replace(' ', '').replace('\n', '').replace('㎡', ''))

    def __get_url(self, house):
        return 'http:' + house.a.attrs.get('href')

    def __get_id(self, house_bs, house_url):
        return house_bs.find_all('h3')[0].text.replace('\n', '').split(' ')[1]

    def __get_environment(self, house_bs, house_url):
        return [e.text for e in house_bs.find_all('div', attrs={'class': 'aboutRoom gray-6'})[0].find_all('p') if
                '周边' in e.strong.text][0]

    def __get_traffic(self, house_bs, house_url):
        return [e.text for e in house_bs.find_all('div', attrs={'class': 'aboutRoom gray-6'})[0].find_all('p') if
                '交通' in e.strong.text][0]

    def __get_detail(self, house_url):
        data = requests.get(house_url).text
        house_bs = bs(data, 'lxml')
        detail_attr = {
            'number': self.__get_id(house_bs, house_url),
            'environment': self.__get_environment(house_bs, house_url),
            'traffic': self.__get_traffic(house_bs, house_url)
        }
        return detail_attr

    def __crawl_subway(self, house):
        subway_name = self.__get_subway(house)
        sw = session.query(Subway).filter(Subway.name == subway_name).first()
        if sw is None:
            sw = Subway(name=subway_name)
            Logger.info('获取地铁站 {}'.format(sw.name))
            session.add(sw)
            session.commit()
        else:
            Logger.info('地铁站 {} 存在'.format(sw.name))

    def __crawl_house_info(self, house):
        attrs = {
            'name': self.__get_location(house),
            'price': self.__get_price(house),
            'subway_distance': self.__get_subway_distance(house),
            'area': self.__get_area(house),
            'url': self.__get_url(house)
        }
        subway_name = self.__get_subway(house)
        sw = session.query(Subway).filter(Subway.name == subway_name).first()
        attrs['subway'] = sw
        attrs.update(self.__get_detail(attrs.get('url')))
        h = session.query(House).filter(House.number == attrs.get('number')).first()
        if h is None:
            h = House(**attrs)
            session.add(h)
            Logger.info('获取 {} 价格 {}'.format(h.name, h.price))
        else:
            Logger.info('{} 存在, 更新数据'.format(h.name))
            for key, value in attrs.items():
                setattr(h, key, value)

        session.commit()

    def crawl_houses(self, all=False, subway=True):
        try:
            if subway is True:
                Logger.info('====== 开始抓取地铁数据 ========')
                [self.__crawl_subway(h) for h in self.__houses(all=all)]
            Logger.info('====== 开始抓取房子数据 ========')
            threads = []
            for h in self.__houses(all=all):
                threads.append(gevent.spawn(self.__crawl_house_info, h))
            gevent.joinall(threads)
        except KeyboardInterrupt:
            Logger.warn('终止抓取进程')

    @staticmethod
    def query_houses():
        return session.query(House)

    @staticmethod
    def query_subway():
        return session.query(Subway)

    @staticmethod
    def max_area(limit=1):
        return session.query(House).order_by(desc(House.area)).limit(limit).all()

    @staticmethod
    def cheapest(limit=1):
        return session.query(House).order_by(House.price).limit(limit).all()
