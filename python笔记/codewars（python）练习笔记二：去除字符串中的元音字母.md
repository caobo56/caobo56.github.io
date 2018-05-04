### codewars（python）练习笔记二：去除字符串中的元音字母

### 题目：

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.

题目大意：
>你的任务是编写一个函数，它接受一个字符串并返回一个删除了所有元音的新字符串。
例如，字符串“This website for for losers LOL！”会变成“Ths wbst s fr lsrs LL!”。
注意：对于这个 y不被视为元音。

### 我的解法：

```
def disemvowel(string):
    string = string.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
    string = string.replace('A','').replace('E','').replace('I','').replace('O','').replace('U','')
    return string
```

哈哈哈，我承认我是个逗比了，主要是昨天的题给我的印象比较深，第一反应就是这样，哎。

### 常规解法：
```
def disemvowel(string):
    out=[]
    mystring=list(string)
    for i in mystring:
        if i not in ["a","e","i","o","u","A","E","I","O","U"]:
            out.append(i)
    return ''.join(out)
```
我仔细想了想，无论怎么写，时间复杂度都是m*n， 因为至少你要判断string中的每一个字母是不是在元音字母中的，无非是写法上优雅不优雅。

### 牛逼解法：

```
def disemvowel(string):
   return string.translate(None, "aeiouAEIOU")
```

### 关于translate()函数

[translate(table, deletechars="")](http://www.runoob.com/python3/python3-string-translate.html)
str.translate(table, deletechars="")

根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中 |


以下实例展示了 translate()函数的使用方法：

```
#!/usr/bin/python

from string

intab = "aeiou"
outtab = "12345"
deltab = "thw"
  
trantab = string.maketrans(intab,outtab) # 创建字符映射转换表
  
test = "this is string example....wow!!!";
  
print test.translate(trantab);
print test.translate(trantab,deltab); # Python2中，删除指定字符在 translate() 方法中
```

以上实例输出结果如下：

```
th3s 3s str3ng 2x1mpl2....w4w!!!
3s 3s sr3ng 2x1mpl2....4!!!
```

translate()是个翻译函数，是将制定的字母表intab[]翻译为对应的映射表outtab[],并删除deltab[]。是python 的字符串内建函数。

### python的字符串内建函数

字符串方法是从python1.6到2.0慢慢加进来的——它们也被加到了Jython中。

这些方法实现了string模块的大部分方法，如下表所示列出了目前字符串内建支持的方法，所有的方法都包含了对Unicode的支持，有一些甚至是专门用于Unicode的。

### 下面就是从菜鸟笔记中摘过来的python 的字符串内建函数表。

| 方法 | 描述 |
| ------------- |:-------------:|
| [string.capitalize()](http://www.runoob.com/python/att-string-capitalize.html) | 把字符串的第一个字符大写 |
| [string.center(width)](http://www.runoob.com/python/att-string-center.html) | 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串 |
| [string.count(str, beg=0, end=len(string))](http://www.runoob.com/python/att-string-count.html) | 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数 |
| [string.decode(encoding='UTF-8', errors='strict')](http://www.runoob.com/python/att-string-decode.html) | 以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace' |
| [string.encode(encoding='UTF-8', errors='strict')](http://www.runoob.com/python/att-string-encode.html) | 以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace' |
| [string.endswith(obj, beg=0, end=len(string))](http://www.runoob.com/python/att-string-endswith.html) | 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False. |
| [string.expandtabs(tabsize=8)](http://www.runoob.com/python/att-string-expandtabs.html) | 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。 |
| [string.find(str, beg=0, end=len(string))](http://www.runoob.com/python/att-string-find.html) | 检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1 |
| [string.format()](http://www.runoob.com/python/att-string-format.html) | 格式化字符串 |
| [string.index(str, beg=0, end=len(string))](http://www.runoob.com/python/att-string-index.html) | 跟find()方法一样，只不过如果str不在 string中会报一个异常. |
| [string.isalnum()](http://www.runoob.com/python/att-string-isalnum.html) | 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False |
| [string.isalpha()](http://www.runoob.com/python/att-string-isalpha.html) | 如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False |
| [string.isdecimal()](http://www.runoob.com/python/att-string-isdecimal.html) | 如果 string 只包含十进制数字则返回 True 否则返回 False. |
| [string.isdigit()](http://www.runoob.com/python/att-string-isdigit.html) | 如果 string 只包含数字则返回 True 否则返回 False. |
| [string.islower()](http://www.runoob.com/python/att-string-islower.html) | 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False |
| [string.isnumeric()](http://www.runoob.com/python/att-string-isnumeric.html) | 如果 string 中只包含数字字符，则返回 True，否则返回 False |
| [string.isspace()](http://www.runoob.com/python/att-string-isspace.html) | 如果 string 中只包含空格，则返回 True，否则返回 False. |
| [string.istitle()](http://www.runoob.com/python/att-string-istitle.html) | 如果 string 是标题化的(见 title())则返回 True，否则返回 False |
| [string.isupper()](http://www.runoob.com/python/att-string-isupper.html) | 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False |
| [string.join(seq)](http://www.runoob.com/python/att-string-join.html) | 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串 |
| [string.ljust(width)](http://www.runoob.com/python/att-string-ljust.html) | 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串 |
| [string.lower()](http://www.runoob.com/python/att-string-lower.html) | 转换 string 中所有大写字符为小写. |
| [string.lstrip()](http://www.runoob.com/python/att-string-lstrip.html) | 截掉 string 左边的空格 
| [string.maketrans(intab, outtab)](http://www.runoob.com/python/att-string-maketrans.html)| maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。 |
| [max(str)](http://www.runoob.com/python/att-string-max.html) | 返回字符串 *str* 中最大的字母。 |
| [min(str)](http://www.runoob.com/python/att-string-min.html) | 返回字符串 *str* 中最小的字母。 |
| [string.partition(str)](http://www.runoob.com/python/att-string-partition.html) | 有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string. |
| [string.replace(str1, str2,  num=string.count(str1))](http://www.runoob.com/python/att-string-replace.html) | 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次. |
| [string.rfind(str, beg=0,end=len(string) )](http://www.runoob.com/python/att-string-rfind.html) | 类似于 find()函数，不过是从右边开始查找. |
| [string.rindex( str, beg=0,end=len(string))](http://www.runoob.com/python/att-string-rindex.html) | 类似于 index()，不过是从右边开始. |
| [string.rjust(width)](http://www.runoob.com/python/att-string-rjust.html) | 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串 |
| string.rpartition(str) | 类似于 partition()函数,不过是从右边开始查找. |
| [string.rstrip()](http://www.runoob.com/python/att-string-rstrip.html) | 删除 string 字符串末尾的空格. |
| [string.split(str="", num=string.count(str))](http://www.runoob.com/python/att-string-split.html) | 以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串 |
| [string.splitlines([keepends])](http://www.runoob.com/python/att-string-splitlines.html) | 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。 |
| [string.startswith(obj, beg=0,end=len(string))](http://www.runoob.com/python/att-string-startswith.html) | 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查. |
| [string.strip([obj])](http://www.runoob.com/python/att-string-strip.html) | 在 string 上执行 lstrip()和 rstrip() |
| [string.swapcase()](http://www.runoob.com/python/att-string-swapcase.html) | 翻转 string 中的大小写 |
| [string.title()](http://www.runoob.com/python/att-string-title.html) | 返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle()) |
| [string.translate(str, del="")](http://www.runoob.com/python/att-string-translate.html) | 根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中 |
| [string.upper()](http://www.runoob.com/python/att-string-upper.html) | 转换 string 中的小写字母为大写 |
| [string.zfill(width)](http://www.runoob.com/python/att-string-zfill.html) | 返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0 |
| [string.isdecimal()](http://www.runoob.com/python/att-string-isdecimal.html) | isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。 |




