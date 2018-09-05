# codewars（python）练习笔记二十三：Brainfuck Translator(Brainfuck翻译)

### 题目
#### Introduction

Brainfuck is one of the most well-known esoteric programming languages. But it can be hard to understand any code longer that 5 characters. In this kata you have to solve that problem.

####Description

In this kata you have to write a function which will do 3 tasks:

1.     Optimize the given Brainfuck code.
2.     Check it for mistakes.
3.     Translate the given Brainfuck programming code into C programming code.

More formally about each of the tasks:

1. Your function has to remove from the source code all useless command sequences such as: '+-', '<>', '[]'. Also it must erase all characters except +-<>,.[].
    Example:
    
  ```
    "++--+." -> "+."
    "[][+++]" -> "[+++]"
    "<>><" -> ""
  ```
2. If the source code contains unpaired braces, your function should return "Error!" string.

3. Your function must generate a string of the C programming code as follows:

* Sequences of the X commands + or - must be replaced by *p += X;\n or *p -= X;\n.

Example:

```
"++++++++++" -> "*p += 10;\n"
"------" -> "*p -= 6;\n"
```

* Sequences of the Y commands > or < must be replaced by p += Y;\n or p -= Y;\n.
Example:

```
">>>>>>>>>>" -> "p += 10;\n"
"<<<<<<" -> "p -= 6;\n"
```

* . command must be replaced by putchar(*p);\n.
Example:

```
".." -> "putchar(*p);\nputchar(*p);\n"
```

* , command must be replaced by *p = getchar();\n.
Example:

```
"," -> "*p = getchar();\n"
```

* [ command must be replaced by if (*p) do {\n. ] command must be replaced by } while (*p);\n.
Example:

```
"[>>]" ->
if (*p) do {\n
  p += 2;\n
} while (*p);\n
```

* Each command in the code block must be shifted 2 spaces to the right accordingly to the previous code block.
Example:

```
"[>>[<<]]" ->
if (*p) do {\n
  p += 2;\n
  if (*p) do {\n
    p -= 2;\n
  } while (*p);\n
} while (*p);\n
```

####Examples

```
Input:
+++++[>++++.<-]
Output:
*p += 5;
if (*p) do {
  p += 1;
  *p += 4;
  putchar(*p);
  p -= 1;
  *p -= 1;
} while (*p);
```       

####Sample Tests

```
def testing(code, expected):
    result = brainfuck_to_c(code)
    test.assert_equals(result, expected)
    
test.describe("general tests")
test.it("basic")

testing("++++", "*p += 4;\n")
testing("----", "*p -= 4;\n")

testing(">>>>", "p += 4;\n");
testing("<<<<", "p -= 4;\n");
    
testing(".", "putchar(*p);\n");
testing(",", "*p = getchar();\n");
    
testing("[[[]]", "Error!");
    
testing("[][]", "");
    
testing("[.]", "if (*p) do {\n  putchar(*p);\n} while (*p);\n");

testing("[]][", "Error!");

testing("++ ++", "*p += 4;\n");

testing("> <<", "p -= 1;\n");

testing("[[.]]", "if (*p) do {\n  if (*p) do {\n    putchar(*p);\n  } while (*p);\n} while (*p);\n");
```

 
### 我的解法
####最初版：
```
#!/usr/bin/python


def brainfuck_sum(l):
    r = ''
    if l['key'] == '+':
        r = '*p += ' + str(l['value']) + ';\n'
    if l['key'] == '-':
        r = '*p -= ' + str(l['value']) + ';\n'
    if l['key'] == '<':
        r = 'p -= ' + str(l['value']) + ';\n'
    if l['key'] == '>':
        r = 'p += ' + str(l['value']) + ';\n'
    return r


def brainfuck_add(i):
    r = ''
    if i == ',':
        r = "*p = getchar();\n"
    if i == '.':
        r = "putchar(*p);\n"
    if i == '[':
        r = "if (*p) do {\n"
    if i == ']':
        r = "} while (*p);\n"
    return r


def brainfuck_retract(i, p):
    r = ''
    p_count_l = p[0:i].count('[')
    p_count_r = p[0:i+1].count(']')
    p_count = p_count_l - p_count_r
    for t in range(p_count):
        r += '  '
    return r


def brainfuck_to_c(source_code):
    p = source_code
    for i in p:
        if i not in ['+', '-', '<', '>', '.', ',', '[', ']']:
            p = p.replace(i, '')
    while '+-' in p or '-+' in p or '<>' in p or '><' in p or '[]' in p:
        p = p.replace('+-', '').replace('-+', '').replace('<>', '').replace('><', '').replace('[]', '')
    if '[' in p or ']' in p:
        if p.count('[') != p.count(']') or p.index('[') > p.index(']'):
            return 'Error!'
    r = ''
    l = {'key': 'p', 'value': 0}
    for i in range(len(p)):
        r += brainfuck_retract(i, p)
        r += brainfuck_add(p[i])
        if p[i] == '<' or '>' or '+' or '-':
            if p[i] == l['key']:
                l['value'] += 1
            else:
                r += brainfuck_sum(l)
                l['key'] = p[i]
                l['value'] = 1
        else:
            r += brainfuck_sum(l)
            l['key'] = ''
            l['value'] = 0
    if l['value'] != 0:
        r += brainfuck_sum(l)
    return r
```

####部分优化版本：

解法一代码太过于冗长，做边界测试的时候直接内存过载，所以要优化代码。
简单看了一下，决定要把while 循环的部分拿掉，优化思路，看看代码执行情况。

```
#!/usr/bin/python


def brainfuck_sum(l):
    r = ''
    if l['key'] == '+-':
        if l['value'] > 0:
            r = '*p += ' + str(l['value']) + ';\n'
        elif l['value'] < 0:
            r = '*p -= ' + str(-l['value']) + ';\n'
    if l['key'] == '<>':
        if l['value'] < 0:
            r = 'p -= ' + str(-l['value']) + ';\n'
        elif l['value'] > 0:
            r = 'p += ' + str(l['value']) + ';\n'
    return r


def brainfuck_add(i):
    r = ''
    if i == ',':
        r = "*p = getchar();\n"
    if i == '.':
        r = "putchar(*p);\n"
    if i == '[':
        r = "if (*p) do {\n"
    if i == ']':
        r = "} while (*p);\n"
    return r


def brainfuck_retract(i, p):
    r = ''
    p_count_l = p[0:i].count('[')
    p_count_r = p[0:i+1].count(']')
    p_count = p_count_l - p_count_r
    for t in range(p_count):
        r += '  '
    return r


def brainfuck_to_c(source_code):
    p = source_code
    print(p)
    for i in p:
        if i not in ['+', '-', '<', '>', '.', ',', '[', ']']:
            p = p.replace(i, '')
    if '[]' in p:
        p = p.replace('[]', '')
    if '[' in p or ']' in p:
        if p.count('[') != p.count(']') or p.index('[') > p.index(']'):
            return 'Error!'
    r = ''
    l = {'key': '', 'value': 0}
    for i in range(len(p)):
        if p[i] in '+-':
            if l['key'] != '+-':
                r += brainfuck_sum(l)
                l['key'] = '+-'
                l['value'] = 0
            l['value'] += (1 if (p[i] == '+') else -1)
        elif p[i] in '<>':
            if l['key'] != '<>':
                r += brainfuck_sum(l)
                l['key'] = '<>'
                l['value'] = 0
            l['value'] += (-1 if (p[i] == '<') else 1)
        elif p[i] in ['.', ',', '[', ']']:
            r += brainfuck_retract(i, p)
            r += brainfuck_add(p[i])
    if l['value'] != 0:
        r += brainfuck_sum(l)
    print(r)
    return r
```

####目前最终版：
解法二解决了内存过载的问题，但在边界测试的时候，仍然会遇到Max Buffer Size Reached (1.5 MiB)，这个说明代码尽管优化了一部分，但还需要继续优化。但仔细思考了一下，还是把while循环的部分添加上，只是作为单列的代码（这一部分是我觉得题目是有争议的，我没想清楚，思考部分在最后）。最终形成了以下解法：

```
#!/usr/bin/python


def brainfuck_sum(l):
    res = ''
    if l['key'] == '+-':
        if l['value'] > 0:
            res = '*p += ' + str(l['value']) + ';\n'
        elif l['value'] < 0:
            res = '*p -= ' + str(-l['value']) + ';\n'
        else:
            pass
    elif l['key'] == '<>':
        if l['value'] < 0:
            res = 'p -= ' + str(-l['value']) + ';\n'
        elif l['value'] > 0:
            res = 'p += ' + str(l['value']) + ';\n'
        else:
            pass
    else:
        pass
    return res


def brainfuck_add(i):
    r = ''
    if i == ',':
        r = "*p = getchar();\n"
    elif i == '.':
        r = "putchar(*p);\n"
    elif i == '[':
        r = "if (*p) do {\n"
    elif i == ']':
        r = "} while (*p);\n"
    else:
        pass
    return r


def brainfuck_retract(i, p):
    r = ''
    p_count_l = p[0:i].count('[')
    p_count_r = p[0:i+1].count(']')
    p_count = p_count_l - p_count_r
    for t in range(p_count):
        r += '  '
    return r


def brainfuck_replace(p):
    while '+-' in p or '-+' in p or '<>' in p or '><' in p or '[]' in p:
        p = p.replace('+-', '').replace('-+', '').replace('<>', '').replace('><', '').replace('[]', '')
    return p


def brainfuck_to_c(source_code):
    p = source_code
    print(p)
    for i in p:
        if i not in ['+', '-', '<', '>', '.', ',', '[', ']']:
            p = p.replace(i, '')
    p = brainfuck_replace(p)
    if '[' in p or ']' in p:
        if p.count('[') != p.count(']') or p.index('[') > p.index(']'):
            return 'Error!'
    if p == '':
        return ''
    r = ''
    l = {'key': '', 'value': 0}
    for i in range(len(p)):
        if p[i] in '+-':
            if l['key'] != '+-':
                r += brainfuck_sum(l)
                l['key'] = '+-'
                l['value'] = 0
            l['value'] += (1 if (p[i] == '+') else -1)
        elif p[i] in '<>':
            if l['key'] != '<>':
                r += brainfuck_sum(l)
                l['key'] = '<>'
                l['value'] = 0
            l['value'] += (-1 if (p[i] == '<') else 1)
        elif p[i] in ['.', ',', '[', ']']:
            r += brainfuck_retract(i, p)
            r += brainfuck_add(p[i])
    if l['value'] != 0:
        r += brainfuck_sum(l)
    return r
```

###思考：
我最终把while循环部分添加上了，主要是这里面我觉得题目是有争议的。
例如题目要求："Your function has to remove from the source code all useless command sequences such as: '+-', '<>', '[]'. Also it must erase all characters except +-<>,.[]."
    Is this rule recursive?
    For example:

    "<[+-]>" -> "<[]>"
    "<[+-]>" -> ""

 Which one is right?
 (I guess the second is right, just want to be sure.)



