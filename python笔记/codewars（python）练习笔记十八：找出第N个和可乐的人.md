# codewars（python）练习笔记十八：找出第N个和可乐的人
### 题目
Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on. 

For example, Penny drinks the third can of cola and the queue will look like this:
Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
Write a program that will return the name of the person who will drink the n-th cola.
Note that in the very beginning the queue looks like that:

```
Sheldon, Leonard, Penny, Rajesh, Howard
```

Input

The input data consist of an array which contains at least 1 name, and single integer n.
```
(1 ≤ n ≤ 1000000000).
```
Output / Examples Return the single line — the name of the person who drinks the n-th can of cola. The cans are numbered starting from 1. Please note that you should spell the names like this: "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" (without the quotes). In that order precisely the friends are in the queue initially. 

```
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1)=="Sheldon"
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52)=="Penny"
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951)=="Leonard"
```


### 我的解法：
```
#!/usr/bin/python

def whoIsNext(names, r):
    if r <= len(names):
        return names[r-1];
    else:
        temp = num = it = 0
        while num < r:
            it += 1
            temp = num
            num += len(names)*2**(it-1)
        return names[(r-temp-1)/(2**(it-1))]
```

### 解法优化：
```
def whoIsNext(names, r):
    i = 0
    s = 0
    while(s+5*(2**i)<r):
      s+=5*(2**i)
      i += 1
    return names[(r-s-1)//(2**(i))]

```
### 另一种优化：
```
import math

def whoIsNext(names, r):
    x = int(math.ceil(math.log(1 + r / 5.0, 2) - 1))
    r = (r - 2 ** x * 5 + 5 - 1) / (2 ** x)
    return names[r]
```

没看懂：
```
def whoIsNext(names, r):
    i = 0
    mult = 1
    while True:
        for name in names:
            i += mult
            if i >= r:
                return name
        mult *= 2

```

```
def whoIsNext(names, r, n = 1):
    while n * 5 - 5 < r: n *= 2
    return names[(2 * r + 8) // n - 5]
```

下面是一个神一样的解法：
```
def whoIsNext(names, r):
    while r > len(names):
        r = (r - (len(names)-1)) / 2
    return names[r-1]
```



