from bs4 import BeautifulSoup as bs
import heapq
import requests


class House:
    def __init__(self, **kwargs):
        self.location = kwargs.get('location')
        self.price = kwargs.get('price')
        self.subway = kwargs.get('subway')
        self.subway_distance = kwargs.get('subway_distance')
        self.area = kwargs.get('area')
        self.url = kwargs.get('url')

    def __repr__(self):
        return '<House {} {} {}>'.format(self.location, self.price, self.area)


class ZiroomSpider:
    def __init__(self, url, page=1):
        self.url = url
        self.data = requests.get(url, params={'p': page}).text
        self.bs = bs(self.data, 'lxml')

    def __re_get_data(self, url, page):
        self.data = requests.get(url, params={'p': page}).text
        self.bs = bs(self.data, 'lxml')

    def __get_pages(self):
        return self.bs.find_all('div', attrs={'class': 'pages'})[0].find_all('a')[-2].text

    def __houses(self, all=False):
        if all is True:
            pages = int(self.__get_pages())
            result = []
            for p in range(pages):
                self.__re_get_data(self.url, p)
                houses = self.bs.find_all('ul', attrs={'id': 'houseList'})[0]
                result.append(houses.find_all('li', attrs={'class': 'clearfix'}))
            result = [item for sublist in result for item in sublist]
            return result
        houses = self.bs.find_all('ul', attrs={'id': 'houseList'})[0]
        return houses.find_all('li', attrs={'class': 'clearfix'})

    def __get_price(self, house):
        return house.find_all('p', attrs={'class': 'price'})[0].text.replace(' ', '').replace('\n', '')

    def __get_location(self, house):
        return house.find_all('h3')[0].text

    def __get_subway(self, house):
        return house.find_all('h4')[0].text

    def __get_subway_distance(self, house):
        for item in house.find_all('div', attrs={'class': 'detail'})[0].find_all('p'):
            if '距离' in item.text:
                return item.text

    def __get_area(self, house):
        return house.p.span.text.replace(' ', '').replace('\n', '')

    def __get_url(self, house):
        return 'http:' + house.a.attrs.get('href')

    def __house_info(self, house):
        attrs = {
            'location': self.__get_location(house),
            'price': self.__get_price(house),
            'subway': self.__get_subway(house),
            'subway_distance': self.__get_subway_distance(house),
            'area': self.__get_area(house),
            'url': self.__get_url(house)
        }
        return House(**attrs)

    def houses(self, all=False):
        return [self.__house_info(h) for h in self.__houses(all)]

    def cheapest(self, all=False, number=1):
        return heapq.nsmallest(number, self.houses(all), lambda h: h.price)

    def max_area(self, all=False, number=1):
        return heapq.nlargest(number, self.houses(all), lambda h: float(h.area.replace('㎡', '')))