# codewars（python）练习笔记二十：ROT13解密

### 题目
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.
Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. 

Test examples:

```
rot13("EBG13 rknzcyr.") == "ROT13 example.";
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
```

```
test.expect(rot13("EBG13 rknzcyr.") == "ROT13 example.")
```

题目大意：
实现ROT13加密/解密方法。
提示:对于这个任务，您只需要替换字符。不是空格、标点、数字等。

### 关于ROT13
ROT13(“由13个地方旋转”，有时是连字符的ROT-13)是一个简单的字母替代密码，用字母表中的第13个字母代替字母。ROT13是古罗马时期发明的凯撒密码的一个特例。

因为在基本的拉丁字母中有26个字母，ROT13是它自己的逆;也就是说，要撤销ROT13，同样的算法也适用，所以同样的操作可以用于编码和解码。该算法几乎不提供加密安全性，并且经常被引用为弱加密的典型示例[1]。

ROT13被用于在线论坛，作为一种隐藏剧透、妙语、谜语和冒犯性材料的手段。ROT13被描述为“美国版的杂志，它的答案是颠倒的”。[2]ROT13在网上引发了各种各样的信件和文字游戏，在新闻组的对话中也经常被提及。

ROT13加密/解密过程。
加密解密用的是一个过程：将 ABCDEFGHIJKLM 依次替换为 NOPQRSTUVWXYZ，并将NOPQRSTUVWXYZ 依次替换为 ABCDEFGHIJKLM。

### 我的解法：

```
#!/usr/bin/python

def rot13(message):
    res = ''
    for item in message:
        if (ord(item)>= ord('A') and ord(item)<= ord('M')) or (ord(item)>= ord('a') and ord(item)<= ord('m')):
            res += chr(ord(item)+13)
        elif (ord(item)>= ord('N') and ord(item)<= ord('Z')) or (ord(item)>= ord('n') and ord(item)<= ord('z')):
            res += chr(ord(item)-13)
        else:
            res += item
    return res
    
print rot13('This is my first ROT13 excercise!')
```

简化后：

```
#!/usr/bin/python

def rot13(message):
    res = ''
    for item in message:
        if  (item >= 'A' and item <= 'M') or (item >= 'a' and item <= 'm'):
            res += chr(ord(item)+13)
        elif  (item >= 'N' and item <= 'Z') or (item >= 'n' and item <= 'z'):
            res += chr(ord(item)-13)
        else:
            res += item
    return res
    
print rot13('This is my first ROT13 excercise!')
```

或者：

```
#!/usr/bin/python

def rot13(message):
    res = ''
    for item in message:
        if ord(item) in range(65,78) or ord(item) in range(97,109):
            res += chr(ord(item)+13)
        elif ord(item) in range(78,90) or ord(item) in range(110,122):
            res += chr(ord(item)-13)
        else:
            res += item
    return res
```

这个题的思路并不复杂，直接替换就好。

### 其他解法
解法一：

```
def rot13(message):
  return message.encode('rot13')

```

解法二：

```
import string

def rot13(message):
  first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
     trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
  return message.translate(string.maketrans(first, trance))  

```

解法三：

```
def rot13(message):
    PAIRS = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"))
    return "".join(PAIRS.get(c, c) for c in message)

```
解法四：

```
def rot13(message):
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    return "".join(decode(c) for c in message)
```
解法五：

```
def rot13(message):
    s = ''
    alph = {'a':'n','A':'N','b':'o','B':'O','c':'p','C':'P','d':'q','D':'Q','e':'r','E':'R','f':'s','F':'S','g':'t','G':'T','h':'u','H':'U','i':'v','I':'V','j':'w','J':'W','k':'x','K':'X','l':'y','L':'Y','m':'z','M':'Z','n':'a','N':'A','o':'b','O':'B','p':'c','P':'C','q':'d','Q':'D','r':'e','R':'E','s':'f','S':'F','t':'g','T':'G','u':'h','U':'H','v':'i','V':'I','w':'j','W':'J','x':'k','X':'K','y':'l','Y':'L','z':'m','Z':'M'}
    for i in message:
        if i in alph:
            s+=alph[i]
        else:
            s+=i
    return s

```

