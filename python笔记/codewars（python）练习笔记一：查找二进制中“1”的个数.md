### codewars（python）练习笔记一：查找二进制中“1”的个数

### 题目：

Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

题目大意：
>编写一个将（无符号）整数作为输入的函数，并返回该数字二进制表示中等于1的位数。
>例如：输入1234，其二进制表示为10011010010，所以所要求实现函数的输出应该是5。


这也是一道比较经典的题目，貌似不少面试总结文章里有这样的题目。

### 普通方法：

```
#!/usr/bin/python

def countBits(n):
    count = 0
    while n > 0 :
        if(n&1) == 1:
            count = count+1
        n>>=1
    return count
    
print countBits(1234)
```

在codewars上的测试结果：
>Time: 550ms Passed: 5 Failed: 0

这种方法是很常规的移位+计数。这种方法的运算次数与输入n最高位1的位置有关，最多循环32次。

### 结合python系统函数的解法：

```
def countBits(n):
    return len(bin(n).replace("0b","").replace("0",""))
    #一句话的事儿
```

在codewars上的测试结果：
>Time: 574ms Passed: 5 Failed: 0

bin(n) 是python的一个系统函数，能够将n 转换为 0b110001 的二进制形式
replace("0b","")是将 0b去掉，这样就得到了n 完整的二进制表示
replace("0","")是将 二进制中的0去掉，这样就得到了生下的都是1的表示
len() 再获取其长度，就是该数字二进制表示中等于1的位数
虽然这是四个系统函数的拼接使用，但有效的减少了相应的代码行数。

### 下面是个从codewars找到的更短的：

```
def countBits(n):
    return bin(n).count("1")
```

python 的系统函数的正确使用，不仅能够降低代码的复杂度，也能有效的减少代码行数。
