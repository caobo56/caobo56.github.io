# codewars（python）练习笔记三：获取多位数字的乘法持久性
### 题目：
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                                     # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                                      # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.

### 题目大意：
编写一个函数persistence，它接受一个正数参数num并返回它的乘法持久性，这是您必须将num中的数字相乘直到达到结果为一个个位数的次数。

例如：输入一个多位数字，例如39，（1）让3和9相乘，变成27，（2）2和7之间相乘，变成14，（3）1和4相乘，变成4。 整个过程需要3次，那么就返回3。
输入999，（1）9*9*9 = 729, （2）7*2*9 = 126,（3） 1*2*6 = 12,并且最终，（4）1*2 = 2.返回4。
输入4，因为 4 已经是一个个位数了，所以直接返回0.

### 我的解法：
```
#!/usr/bin/python

case_total_num = 0

def persistence(n):
    global case_total_num
    if n > 9:
        case_total_num += 1 
        n_str = str(n)
        temp = 1
        for i in n_str:
            temp = temp * int(i)
        if temp > 9:
            return persistence(temp)
            # python的递归调用，也是需要return 的
        else:
            temp = case_total_num
            case_total_num = 0
            return temp
    else:
        return case_total_num
```
其实这个就是一个常规的递归算法，有递归意识，这个算法就能自然而然的写出来。函数需要递归的次数，就设定一个 case_total_num ，存储递归的次数。

### 两个坑
我在写这个函数的过程中，遇到了两个坑：
* 一个是python的递归调用，也是需要return 的，即：return persistence(temp)。否则的话，函数执行完，会直接返回None。
* 另一个是codewars 的测试case 是依次执行的，如果不在递归完成后，将global case_total_num清零的话，上一个case 的结果会带入到下一次的测试case 中去，导致第一次是正确的，之后的全是错误的。

### 一点疑问
算法执行完之后的一点疑问：我将case_total_num 定义在def persistence(n): 之前，执行四个测试case 的速度为
>Time: 538ms Passed: 4 Failed: 0

但是将case_total_num 定义在def persistence(n): 之后，执行四个测试case 的速度就会大大延长，测试case 的速度为
>Time: 720ms Passed: 4 Failed: 0

当然两者相差不多，但后者的平均速度要比前者慢一些确实事实。

### 一点疑问的测试结论：
但后来在，我写了这么一个demo 来测试具体时间时，缺没有提现出足够的差别：
```
begin = datetime.datetime.now()
for i in range(1000,9999999):
    persistence(i)
end = datetime.datetime.now()
k = end - begin
print k 
```
执行结果：
![图片.png](https://upload-images.jianshu.io/upload_images/1136127-12598a33f0078227.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 理论上应该是没差别的，无论global在上面声明还是在函数之后声明，函数内一执行到global 马上就去模块全局去找的，不应该会因为这个产生明显的差别。

### 优化解法一：
去掉 global case_total_num
因为，既然可以return persistence(temp) ，那在return 的时候，让persistence(temp)直接加1，就是的引用次数
```
#!/usr/bin/python

def persistence(n):
    case_total_num = 0
    if n > 9:
        case_total_num += 1 
        n_str = str(n)
        temp = 1
        for i in n_str:
            temp = temp * int(i)
        if temp > 9:
            return persistence(temp) + 1
        else:
            return case_total_num
    else:
        return case_total_num
```
### 优化解法二：
```
def persistence(n):
    if str(n) == 1:
        return 0
    count = 0
    while len(str(n)) > 1:
        total = 1
        for i in str(n):
            total *= int(i)
        n = total
        count += 1
    return count
```
这种方法，利用while循环来替换掉递归循环，降低了算法的复杂度，也是一种很不错的算法。
### 优化解法三：
```
def persistence(n):
    ni = 0
    while n >= 10:
        n = reduce(lambda x, y: x * y, [int(i) for i in str(n)])
        ni += 1
    return ni
```
### 优化解法四：
```
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
```
codewars上大神多啊！！