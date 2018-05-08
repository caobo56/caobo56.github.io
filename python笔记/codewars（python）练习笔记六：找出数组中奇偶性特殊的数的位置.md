# codewars（python）练习笔记六：找出数组中奇偶性特殊的数的位置

### 题目：
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :
```
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
```

题目大意：

找出数组中，与其他数组元素奇偶性不一致的数字的index（而且还要求index+1）。

我的解法：

```
#!/usr/bin/python

def iq_test(numbers):
    temp_list = []
    for i in numbers.split(' '):
        temp_list.append(str(int(i)%2))
    if temp_list.count("1") > temp_list.count("0"):
        return temp_list.index("0")+1
    else:
        return temp_list.index("1")+1

print iq_test('2 4 6 7 10 12')
```

这个主要是找出数组中，与其他数组元素奇偶性不一致的数字的index（而且还要求index+1）

所以思路比较固定，就是先将数组中所有的数%2 ，生成新数组，原数组中的数对应变为 0 和 1，0即为偶数，1即为奇数。

然后比较新数组中，0 和 1的个数哪个多，就返回另一种的index。

下面是更加牛逼的写法，但思路一致：
解法一：

```
def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1
```

解法二：

```
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
``` 