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
 <House 潼港四村2居室-东 ￥3990(每月) 64.05㎡>,
 <House 海高二村2居室-东 ￥3990(每月) 62.07㎡>,
 <House 潼港八村2居室-东 ￥4120(每月) 53.65㎡>,
 <House 高南新村2居室-南北 ￥4150(每月) 59.71㎡>]

In [4]: len(z.houses(all=True))
Out[4]: 74

In [5]: z.max_area()
Out[5]: <House 潼港八村2居室-南 ￥3920(每月) 66.72㎡>

In [6]: z.max_area(all=True)
Out[6]: <House 璞真园2居室-南 ￥6260(每月) 96.7㎡>

In [7]: z.max_area(all=True).subway
Out[7]: '[浦东金桥] 6号线五莲路'

In [8]: z.max_area(all=True).subway_distance
Out[8]: '距离6号线五莲路站294米'

In [9]: z.cheapest()
Out[9]: <House 高桥二村2居室-东 ￥3280(每月) 47.27㎡>
```
