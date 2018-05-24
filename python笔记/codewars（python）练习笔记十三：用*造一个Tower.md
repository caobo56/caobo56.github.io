# codewars（python）练习笔记十三：用*造一个Tower
### 题目
Build Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

    Python: return a list;
    JavaScript: returns an Array;
    C#: returns a string[];
    PHP: returns an array;
    C++: returns a vector<string>;
    Haskell: returns a [String];
    Ruby: returns an Array;

Have fun! 

题目大意：

![屏幕快照 2018-05-16 下午2.11.14.png](https://upload-images.jianshu.io/upload_images/1136127-359d018505a0496f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Go challenge [Build Tower Advanced](https://www.codewars.com/kata/57675f3dedc6f728ee000256) once you have finished this :)


### 我的解法：

```
def tower_builder(n_floors):
    if n_floors <= 0:return []
    temp = []
    for i in range(0,n_floors):
        line = ''
        for j in range(0,n_floors*2-1):
            if (j < n_floors and i + j >= n_floors-1) or (j+1 > n_floors and j - n_floors < i):
                line += '*'
            else:
                line += ' '
        temp.append(line)
    return temp
```

马蛋，这是大学刚开始学C的时候的题目，现在看，仍然不过时。但是我仍然不太会写。试了试，好歹先把题目解出来。

最牛逼的解法：
```
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
```

其他解法一：
```
def tower_builder(n_floors):
    if n_floors <= 0:return []
    count = 1
    result = []
    for i in range(1, n_floors + 1):
      stars = '*' * (2 * i - 1)
      space = ' ' * (n_floors - i)
      result.append(space + stars + space)
    return result
```

其他解法二：
```
def tower_builder(n_floors):
    tower = []
    spacing = n_floors - 1
    stars = 1
    for i in range(0, n_floors):
        tower.append(' ' * spacing + '*' * stars + spacing * ' ')
        stars += 2
        spacing -= 1
    return tower
```

其他解法三：
```
def tower_builder(n_floors):
    floors = []
    for i in range(n_floors):
        n_floors -= 1
        floors.append(' ' * n_floors + '*' * (i * 2 + 1) + ' ' * n_floors)
    return floors
```
其他解法四：
```
def tower_builder(n_floors):
    return ['{0}{1}{0}'.format(' ' * (n_floors - 1 - x), '*' * (1 + 2 * x)) for x in range(n_floors)]
```

