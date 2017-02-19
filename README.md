# ziroom_spider

## usage

```python
In [1]: from spider import ZiroomSpider

In [2]: z = ZiroomSpider('http://sh.ziroom.com/z/nl/z1-d310115-u2-x6-o1.html')

In [3]: z.houses()
Out[3]:
[<House 高桥二村2居室-东 ￥3280(每月) 47.27㎡>,
 <House 绿海家园2居室-南 ￥3450(每月) 61.12㎡>,
 <House 港城新苑2居室-东 ￥3860(每月) 55.27㎡>,
 <House 海高二村2居室-东 ￥3860(每月) 63.22㎡>,
 <House 潼港八村2居室-南 ￥3920(每月) 66.72㎡>,
 <House 海高二村2居室-东 ￥3990(每月) 62.07㎡>,
 <House 潼港四村2居室-东 ￥3990(每月) 64.05㎡>,
 <House 潼港八村2居室-东 ￥4120(每月) 53.65㎡>,
 <House 高南新村2居室-南北 ￥4150(每月) 59.71㎡>]

In [4]: z.max_area()
Out[4]: [<House 潼港八村2居室-南 ￥3920(每月) 66.72㎡>]

In [5]: z.max_area(all=True)
Out[5]: [<House 璞真园2居室-南 ￥6260(每月) 96.7㎡>]

In [6]: z.cheapest()
Out[6]: [<House 巨东小区2居室-南北 ￥5660(每月) 67㎡>]

In [7]: z.reget_data(page=3)

In [8]: z.houses()
Out[8]:
[<House 绿波城2居室-南 ￥4590(每月) 58.97㎡>,
 <House 朱家门小区2居室-南 ￥4590(每月) 62.85㎡>,
 <House 荷三小区2居室-南 ￥4590(每月) 67.39㎡>,
 <House 崮山小区2居室-东 ￥4790(每月) 45.64㎡>,
 <House 博一小区2居室-南北 ￥4820(每月) 59.52㎡>,
 <House 金杨新村五街坊2居室-南 ￥4990(每月) 59.53㎡>,
 <House 金杨新村九街坊2居室-南 ￥4990(每月) 57.76㎡>,
 <House 金杨新村九街坊2居室-南北 ￥5020(每月) 56.05㎡>,
 <House 宜嘉苑2居室-东 ￥5020(每月) 84.97㎡>]

In [9]: len(z.houses(all=True))
Out[9]: 65

In [10]: z.cheapest()[0]
Out[10]: <House 巨东小区2居室-南北 ￥5660(每月) 67㎡>

In [11]: z.cheapest()[0].subway
Out[11]: '[浦东洋泾] 6号线北洋泾路'

In [12]: z.cheapest()[0].subway_distance
Out[12]: '距离6号线北洋泾路站290米'

In [13]: z.cheapest()[0].url
Out[13]: 'http://sh.ziroom.com/z/vr/60032108.html'

In [14]: z.cheapest()[0].area
Out[14]: '67㎡'

In [15]: z.max_area(number=3)
Out[15]:
[<House 璞真园2居室-南 ￥6260(每月) 96.7㎡>,
 <House 巨东小区2居室-南北 ￥5660(每月) 67㎡>,
 <House 巨杨小区2居室-东 ￥6290(每月) 55.09㎡>]
 
```
