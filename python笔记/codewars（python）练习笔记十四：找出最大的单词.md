# codewars（python）练习笔记十四：找出最大的单词
###题目
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

### Test case:
```
test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
```
题目大意：
设定 a = 1, b = 2, c = 3 依次类推，求出句子中所有字母加和值最大的单词。

### 我的解法：
```
#!/usr/bin/python

def high(x):
    list_p = []
    for item in x.split(' '):
        p = 0
        for i in item:
            p += ord(i)-ord('a')+1
        list_p.append(p)
    return x.split(' ')[list_p.index(max(list_p))]
```

牛逼的解法:

```
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
```

思路大同小异。

