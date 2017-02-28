from tabulate import tabulate
from models import session, House, Subway
from spider import ZiroomSpider
import argparse

parser = argparse.ArgumentParser(prog='spider')
parser.add_argument('-l', '--limit', dest='limit', help='limit output', default=10, type=int)
parser.add_argument('-s', '--sort', dest='sort', help='sort by column', default='area')
parser.add_argument('-b', '--subway', dest='subway', help='show subway', default=False, action='store_true')
parser.add_argument('-a', '--all', dest='all', help='show all houses', default=False, action='store_true')
parser.add_argument('-d', '--desc', dest='desc', help='desc', default=False, action='store_true')
subparsers = parser.add_subparsers()
update_parser = subparsers.add_parser('update', help='update house')
update_parser.add_argument('-u', '--url', dest='url', help='specify url', default=None)
update_parser.add_argument('-a', '--all', dest='all', help='update all page house', default=False, action='store_true')
args = parser.parse_args()


def update(all=False):
    z = ZiroomSpider(args.url)
    z.crawl_houses(all=all)


def sort():
    if args.all is True:
        args.limit = None
    if args.sort == 'area':
        return ZiroomSpider.max_area(limit=args.limit, desc_=args.desc)
    elif args.sort == 'price':
        return ZiroomSpider.cheapest(limit=args.limit, desc_=args.desc)


def get_data():
    if args.subway:
        title = ['名称', '编号', '价格', '面积', '链接', '地铁']
        return [[x.name, x.number, x.price, x.area, x.url, x.subway.name] for x in sort()], title
    title = ['名称', '编号', '价格', '面积', '链接']
    return [[x.name, x.number, x.price, x.area, x.url] for x in sort()], title


def main():
    if 'url' in args:
        update(all=args.all)
        return
    data = get_data()
    print(tabulate(*data, tablefmt='grid'))


if __name__ == '__main__':
    main()
