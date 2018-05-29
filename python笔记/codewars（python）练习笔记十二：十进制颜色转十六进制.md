# codewars（python）练习笔记十二：十进制颜色转十六进制

### 题目
The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value. 

The following are examples of expected output values:

    rgb(255, 255, 255) # returns FFFFFF
    rgb(255, 255, 300) # returns FFFFFF
    rgb(0,0,0) # returns 000000
    rgb(148, 0, 211) # returns 9400D3

题目大意：计算颜色值，将0~255 转 16进制。超出范围的，应该四舍四入到最接近的有效值。

### 我的解法：

```
#!/usr/bin/python

def rgb(r, g, b):
    temp = ''
    for item in [r,g,b]:
        if item < 0:
            item = 0
        elif item > 255:
            item = 255
        temp += str(hex(item)).replace('0x','').upper().zfill(2)
    return temp
```
几种不同的进制转换，这一块的知识点我比较弱，就弄最简单的思路来写。

其他解法一：

```
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
```

其他解法二：

```
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))
```

其他解法三：

```
def rgb(r, g, b):
    clamp = lambda x: max(0, min(x, 255))
    return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))
```

其他解法四：

```
def rgb(*args):
  return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args));
```

其他解法五：

```
def rgb(r, g, b):
  clamp = lambda x: max(0, min(x, 255))
  return "{:02X}{:02X}{:02X}".format(clamp(r), clamp(g), clamp(b))
```

其他解法六：

```
def rgb(r, g, b): 
    return ''.join(['%02X' % max(0, min(x, 255)) for x in [r, g, b]])
```

