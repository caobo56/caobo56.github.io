# codewars（python）练习笔记十六：求出小于solution的能整除3或5的数的和
### 题目
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
Note: If the number is a multiple of both 3 and 5, only count it once.
Courtesy of ProjectEuler.net

题目大意：
求出小于solution的能整除3或5的数的和。

### 我的解法：
```
#!/usr/bin/python

def solution(number):
    temp = 0
    for item in range(0,number):
        if item%3 == 0 or item%5 == 0:
            temp += item
    return temp
    
print solution(10)
```

简化解法：

```
def solution(number):
  return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])
```
###牛逼解法：

```
def solution(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result

```
这个一开始没看明白。但后来转念一想就明白了：这个就是求出能被3整除的数的和，加上能被5整除的数的和，减去能被15整除的数的和，就满足题目要求了。

