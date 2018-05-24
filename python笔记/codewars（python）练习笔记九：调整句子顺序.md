# codewars（python）练习笔记九：调整句子顺序

### 题目：
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
```
your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"
```

### 我的解法：

```
#!/usr/bin/python

def order(sentence):
    if not sentence:
        return ''
    arr = [filter(str.isdigit, item) for item in sentence.split(' ')]
    arr = [sentence.split(' ')[arr.index(str(item+1))] for item in range(0,len(arr))]
    return ' '.join(item for item in arr)

```

我的思路：
* 1）先将句子转换为数组
* 2）提取出每个word的索引
* 3）将索引排序
* 4）根据排序后的索引，和索引原来的位置，依次获取索引对应的word，生成新的word 数组
* 5）将新数组拼接成为 string 返回

因此第一遍的解法是：
```
def order(sentence):
    org = sentence.split(' ')
    arr = [filter(str.isdigit, item) for item in org]
    arr_sort = sorted(arr)
    arr = [sentence.split(' ')[arr.index(item)] for item in arr_sort]
    return ' '.join(item for item in arr)
```

根据python的语法特性，简写如下：

```
def order(sentence):
    arr = [filter(str.isdigit, item) for item in sentence.split(' ')]
    arr = [sentence.split(' ')[arr.index(item)] for item in sorted(arr)]
    return ' '.join(item for item in arr)
```

但是，又仔细思考了一下，arr本身就是一个数字数组，对数字数组进行排序，获得的就是一个顺序数字数组。顺序数字数组可以直接生成，没必要排序。

所以，可以将sorted(arr) 替换为  range(0,len(arr) 再在取值的时候直接加一即可。

```
def order(sentence):
    arr = [filter(str.isdigit, item) for item in sentence.split(' ')]
    arr = [sentence.split(' ')[arr.index(str(item+1))] for item in range(0,len(arr))]
    return ' '.join(item for item in arr)
```

再添加上前置条件：If the input String is empty, return an empty String.如果是空字符串，直接返回空即可。

```
def order(sentence):
    if sentence == '':
        return ''
    arr = [filter(str.isdigit, item) for item in sentence.split(' ')]
    arr = [sentence.split(' ')[arr.index(str(item+1))] for item in range(0,len(arr))]
    return ' '.join(item for item in arr)
```

这就是我思路的展开过程。

codewars 上永远有大神：

解法一：
```
def extract_number(word):
    for l in word: 
        if l.isdigit(): return int(l)
    return None

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))

```
解法二：

```
def order(s):
    z = []
    for i in range(1,10):
        for j in list(s.split()):
            if str(i) in j:
               z.append(j)
    return " ".join(z)
```

解法三：

```
def order(sentence):
    def sort_key(s):
        return next(c for c in s if c.isdigit())
    return ' '.join(sorted(sentence.split(), key=sort_key))
```

解法四：

```
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
```

解法五：

```
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
```

