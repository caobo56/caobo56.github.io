# codewars（python）练习笔记五：创建数字的根函数

### 题目：

In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

题目大意：

数字根是数字中所有数字的递归和。给定n，取n的数字的和，如果该值有两位数字，继续以这种方式减少，直到产生一位数。这只适用于自然数。

```
digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
```

简单解法：

```
def digital_root(n):
    n_str = str(n)
    temp = 0
    for i in n_str:
        temp = temp + int(i) 
    if temp > 9:
        return digital_root(temp)
    else:
        return temp
```

由于这道题跟之前的[获取多位数字的乘法持久性](https://www.jianshu.com/p/27503826d1b3)比较类似，所以类似的衍生算法有以下几个：

```
#!/usr/bin/python
from functools import reduce

def digital_root(n):
    while n >= 10:
        n = reduce(lambda x, y: x + y, [int(i) for i in str(n)])
    return n
```

或者使用operator.add：

```
#!/usr/bin/python
import operator

def digital_root(n):
    while n >= 10:
        n = reduce(operator.add, [int(i) for i in str(n)])
    return n
```
