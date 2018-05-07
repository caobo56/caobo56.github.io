# codewars（python）练习笔记四：判断单词中是否有重复字母（不区分大小写）

### 题目：

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
test case：
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case

题目大意：

找出字符串中的重复字母，不区分大小写。

### 我的解法：
```
def is_isogram(string):
    temp_list = []
    for item in list(string):
        item = item.lower()
        if item in temp_list:
            return False
        else:
            temp_list.append(item)
    return True
```

### 牛逼一点的解法：

```
def is_isogram(string):
    s = set(string.lower()) 
    if len(s) == len(string): 
        return True
    return False
```
这个就是对set的运用。

优化：

```
def is_isogram(string):
    return len(string) == len(set(string.lower()))
```