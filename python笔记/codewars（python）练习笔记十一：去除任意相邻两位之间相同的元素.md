# codewars（python）练习笔记十一：去除任意相邻两位之间相同的元素
### 题目
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

题目大意：
实现函数unique_in_order，该函数将参数作为参数，并返回一个项目列表，其中任意相邻两位之间，没有包含相同值的元素，区分大小写，并保留元素的原始顺序。

我的解法：
```
def unique_in_order(iterable):
    list_temp = []
    for item in iterable:
        if len(list_temp) == 0 or item != list_temp[len(list_temp)-1]:
            list_temp.append(item)
    return list_temp
```

其他解法一：
```
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
```

其他解法二：
```
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
```

其他解法三：
```
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]
```

其他解法四：
```
def unique_in_order(iterable):
  r = []
  for x in iterable:
    x in r[-1:] or r.append(x)
  return r
```

 其他解法五：
```
def unique_in_order(it):
    return [it[0]] + [e for i, e in enumerate(it[1:]) if it[i] != e] if it else []
```

其他解法六：
```
def unique_in_order(string):
    lst = [string[i] for i in range(0,len(string)) if (i==0 or string[i]!=string[i-1])];
    return lst;

```

