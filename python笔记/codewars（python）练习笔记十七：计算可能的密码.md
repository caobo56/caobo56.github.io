# codewars（python）练习笔记十七：计算可能的密码

### 题目
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. 

Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
```

He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we count on you!

Sample Tests:

```
test.describe('example tests')
expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

for tup in expectations:
  test.assert_equals(sorted(get_pins(tup[0])), sorted(tup[1]), 'PIN: ' + tup[0])
```

题目大意：

已知一个如上图所示的密码盘。已经观测到了一次密码输入,但是由于观测的不准确，任何一次按钮输入，都可能是相邻的按钮。例如：按了8，可能实际是 5 7 8 9 0这四项的任何一个。写出一个算法，输入密码输入序列，给出可能的真实密码。

例如：
('8', ['5','7','8','9','0']),
('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])

### 我的解法：

```
#!/usr/bin/python

def get_pins(observed):
    temp_map = {'1':['1','2','4'],'2':['1','2','5','3'],'3':['2','3','6'],'4':['1','4','5','7'],'5':['2','4','5','6','8'],'6':['3','5','6','9'],'7':['4','7','8'],'8':['5','7','8','9','0'],'9':['6','8','9'],'0':['0','8']}
    if len(observed) > 1: 
        arr = []
        for item in temp_map[observed[0]]:
            for it in get_pins(observed[1:]):
                arr.append(item+it)
        return arr
    else:
        return temp_map[observed]
```

这个解法，是常规的解法。构造temp_map，特定的需求直接构造相应的temp_map,以每个输入项为key，后面跟的是他对应的可能值。

### 照例，后面是牛逼的解法：
```
#!/usr/bin/python

from itertools import product

def get_pins(observed):
    ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]

```

另一个牛逼的解法：
```
def get_pins(observed):
  map = [['8','0'], ['1','2','4'], ['1','2','3','5'], ['2','3','6'], ['1','4','5','7'], ['2','4','5','6','8'],
         ['3','5','6','9'], ['4','7','8'], ['5','7','8','9','0'], ['6','8','9']]
  return map[int(observed[0])] if len(observed) == 1 else [x + y for x in map[int(observed[0])] for y in get_pins(observed[1:])]

```
其实，大部分网友的思路都是相同的， 只是细节上的差异
```
def get_pins(observed):
  map = [['8','0'], ['1','2','4'], ['1','2','3','5'], ['2','3','6'], ['1','4','5','7'], ['2','4','5','6','8'],
         ['3','5','6','9'], ['4','7','8'], ['5','7','8','9','0'], ['6','8','9']]
  return map[int(observed[0])] if len(observed) == 1 else [x + y for x in map[int(observed[0])] for y in get_pins(observed[1:])]

```

