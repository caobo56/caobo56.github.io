# codewars（python）练习笔记七：电话号码格式化

### 题目：
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
Example:

```
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

题目大意：
将长度为10的数组（每个元素<10）格式化成"(123) 456-7890" 这样。

我的解法：

```
def create_phone_number(str_list):
    str_list = [str(i) for i in str_list]
    str_list.insert(0,'(')
    str_list.insert(4,') ')
    str_list.insert(8,'-')
    str1 = ''
    return str1.join(str_list)
```

这个就是直筒子的思路。

codewars 上大神众多：

解法一：

```
def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])


  return '({}) {}-{}'.format(str1, str2, str3)
```

解法二：

```
def create_phone_number(n):
    n = "".join([str(x) for x in n] )
    return("(" + str(n[0:3]) + ")" + " " + str(n[3:6]) + "-" + str(n[6:]))
```

解法三：

```
def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])
```

解法四：

```
def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
```

解法五：

```
def create_phone_number(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)
```