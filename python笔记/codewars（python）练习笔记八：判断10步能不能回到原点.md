# codewars（python）练习笔记八：判断10步能不能回到原点

### 题目：
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

题目大意：
就是一个人，一步一格，可以走北南西东四个方向，即（n，s，w，e）。
给一个 10步的方案，来判断这10步之后是不是能够回到原点。
如果不是10步，返回False。 10步能到原点，返回True，不能则返回False。

### 我的解法：

```
#!/usr/bin/python

def isValidWalk(walk):
    if len(walk) != 10:
        return False
    if walk.count('n') == walk.count('s'):
        if walk.count('w') == walk.count('e'):
            return True
    return False
```

思路：就是先判断步数够不够10步，在判断 n s  or  w e 是不是两两相等。

## 难度在题目比较长，需要了解足够的信息，并提炼出前提条件。

精炼的解法：

```
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
```






