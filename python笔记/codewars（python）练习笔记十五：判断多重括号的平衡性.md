# codewars（python）练习笔记十五：判断多重括号的平衡性

### 题目
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return `true` if the string is valid, and `false` if it's invalid.

This Kata is similar to the [Valid Parentheses](https://www.codewars.com/kata/valid-parentheses) Kata, but introduces new characters: brackets `[]`, and curly braces `{}`. Thanks to `@arnedag` for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: `()[]{}`.

### What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace.

## Examples

```
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

```
题目大意：
给定字符串，判断字符串中，多重括号的平衡性。仅有 () {}  [] ，没有其他字符串。

### 解题思路：
1. 括号匹配的四种可能性：
①左右括号配对次序不正确
②右括号多于左括号
③左括号多于右括号
④左右括号匹配正确

2. 算法思想：
1.顺序扫描算数表达式（表现为一个字符串），当遇到三种类型的左括号时候让该括号进栈；
2.当扫描到某一种类型的右括号时，比较当前栈顶元素是否与之匹配，若匹配，退栈继续判断；
3.若当前栈顶元素与当前扫描的括号不匹配，则左右括号配对次序不正确，匹配失败，直接退出；
4.若字符串当前为某种类型的右括号而堆栈已经空，则右括号多于左括号，匹配失败，直接退出；
5.字符串循环扫描结束时，若堆栈非空（即堆栈尚有某种类型的左括号），则说明左括号多于右括号，匹配失败；
6.正常结束则括号匹配正确。

### 我的解法：
```
#!/usr/bin/python

def validBraces(string):
    temp = []
    for item in string:
        if item in ['[','{','(']:
            temp.insert(0,item)
        if item in [']','}',')']:
            if len(temp) == 0:
                return False
            elif (item == ']' and temp[0] == '[') or (item == '}' and temp[0] == '{') or (item == ')' and temp[0] == '('): 
                temp.remove(temp[0])
            else:
                return False
    if len(temp) != 0:
        return False
    else:
        return True

```
简单的讲，就是遇见左括号，就入栈，遇见右括号：
1）先判断栈内是否有元素，没有则出现了先右后左，不平衡，返回 False
2）再判断栈顶元素是否与当前右括号匹配，若不匹配，返回 False，若匹配，删除栈顶元素，继续下一循环
最后，循环结束后，判断栈内是否有元素，有则说明左括号数量多于右括号，不平衡，不匹配。没有则说明左右平衡，返回True。

### 其他解法一：
```
def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0  
```
这个是利用了map ，简化了数据模型和分析过程。


### 其他解法二：
```
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','').replace('[]','').replace('()','')
  return s==''
```

利用左右括号的平衡性，最内的括号一定时左右相邻且平衡的。  

