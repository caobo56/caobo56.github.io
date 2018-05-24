# codewars（python）练习笔记十九：求数组的质因数的倍数和集
### 题目
Given an array of positive or negative integers 
```
I= [i1,..,in]
```
you have to produce a sorted array P of the form 
```
[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]
```
P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
```
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
```
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

**Notes:**
	•	It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others. 
	•	In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

Sample Tests:
```
a = [12, 15]
test.assert_equals(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])

list:   [12, 15]
result: [[2, 12], [3, 27], [5, 15]]


list:   [15, 21, 24, 30, 45]
result: [[2, 54], [3, 135], [5, 90], [7, 21]]


list:   [15, 21, 24, 30, -45]
result: [[2, 54], [3, 45], [5, 0], [7, 21]]


list:   [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
result: [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]]


list:   [-29804, -4209, -28265, -72769, -31744]
result: [[2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], [7451, -29804]]
```

题目大意

对一个数组，如[12,15],首先对每个元素进行质因数分解，比如，12 = 2X2X3，则12有质因数 2，3；15 =3X5，有质因数3，5。 

则数组有不同质因数2，3，5。 

那么，按从小到大的顺序：2的倍数有12；3的倍数有：12、15；5的倍数有：15。  

则可以输出[(2,12),(3,12+15),(5,15)] =>简化[(2,12),(3,27),(5,15)]. 

注意，负整数的质因数和对应的正整数的质因数相同。

### 我的解法：

```
import math

def isprime(n): 
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: return False
    return True

def sum_for_list(lst):
    arrArr = []
    for num in lst:
        if num < 0: num=-num
        arrArr += [item for item in range(1,num+1) if(num%item == 0 and isprime(item) and item not in arrArr)]
    temp_arr = []
    for item in sorted(arrArr):
        temp = 0
        for num in lst:
            if num%item == 0:
                temp += num
        temp_arr.append([item,temp])
    return temp_arr
```

然后想了想，是不是能简化一下提升一下效率，就考虑到是不是利用数据结构，简化一下加和那一步的效率。
```
#!/usr/bin/python
import math

def isprime(n): 
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: return False
    return True

def sum_for_list(lst):
    keyarr = []
    kvarr = []
    for num in lst:
        if num < 0:num=-num
        for item in range(1,num+1):
            if num%item == 0 and isprime(item):
                kvarr.append({item:num})
                if item not in keyarr:keyarr.append(item)
    res = []
    for key in keyarr:
        vsum = 0
        for dic in kvarr:
            if dic.keys()[0] == key:
                vsum += dic[key]
        res.append([key,vsum])
    return res
```
利用数组嵌套，不如直接利用dict，所以继续优化如下：
```
#!/usr/bin/python
import math

def isprime(n): 
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: return False
    return True

def sum_for_list(lst):
    kvdict = {}
    for num in lst:
        if num < 0:num=-num
        for item in range(1,num+1):
            if num%item == 0 and isprime(item):
                if item in kvdict.keys():
                    kvdict[item].append(num)
                else:
                    kvdict[item] = [num]
    res = []
    for key in kvdict.keys():
        vsum = 0
        for num in kvdict[key]:
                vsum += num
        res.append([key,vsum])
    return res
```
继续优化：
```
#!/usr/bin/python
import math

def isprime(n): 
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: return False
    return True

def sum_for_list(lst):
    kvdict = {}
    for num in lst:
        if num < 0:num=-num
        for item in range(1,num+1):
            if num%item == 0 and isprime(item):
                if kvdict.has_key(item):
                    kvdict[item].append(num)
                else:
                    kvdict[item] = [num]
    res = [[key,sum(kvdict[key])] for key in sorted(kvdict.keys())]
    return res
```

然后再在上面的嵌套想办法，首先是if else。abs(num)可以直接取num的绝对值。三目运算也可以减少代码行数：
```
#!/usr/bin/python
import math

def isprime(n): 
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: return False
    return True

def sum_for_list(lst):
    kvdict = {}
    for num in lst:
        for item in range(1,abs(num)+1):
            if abs(num)%item == 0 and isprime(item):
                kvdict[item] = kvdict[item]+[num] if kvdict.has_key(item) else [num]
    res = [[key,sum(kvdict[key])] for key in sorted(kvdict.keys())]
    return res
```
将判断质数的方法优化：
```
#!/usr/bin/python
import math

def isprime(n): 
    return n in filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i==0], range(2,n+1))

def sum_for_list(lst):
    kvdict = {}
    for num in lst:
        for item in range(1,abs(num)+1):
            if abs(num)%item == 0 and isprime(item):
                kvdict[item] = kvdict[item]+[num] if kvdict.has_key(item) else [num]
    res = [[key,sum(kvdict[key])] for key in sorted(kvdict.keys())]
    return res
```
### 另一种思路：
先求出需要求的数组的最大值以内的质数的集。然后再找出对应的质数的集合。这个思路是以空间换取部分时间，在给定数组的最大值较小的时候，比较合适。但，如果给定数组的最大值比较大，那么要生成的质数集就会非常大，生成效率也会大幅降低。
```
#!/usr/bin/python
import math

def func_get_prime(n):
  return filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i==0], range(2,n+1))
    
def sum_for_list(lst):
    temp_lst = [abs(item) for item in lst]
    prime_arr = func_get_prime(sorted(temp_lst)[len(temp_lst)-1])
    kvdict = {}
    for num in temp_lst:
        for key in prime_arr:
            if key < num and num%key == 0:
                kvdict[key] = kvdict[key]+[num] if kvdict.has_key(key) else [num]
            elif key > num:
                break
    res = [[key,sum(kvdict[key])] for key in sorted(kvdict.keys())]
    return res
```

### 牛逼人是怎么写的

我想了好久，都没有特别好优化算法，然后提交之后，一个牛逼的算法轰然而至：
```
def sum_for_list(lst):
    factors = {i for k in lst for i in xrange(2, abs(k)+1) if not k % i}
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]

```
这个是就对python语法的仔细掌握了，但从效率上和时间复杂度上来讲，也就这样了。

### 总结：
**毕竟，输入数组的情况，千变万化，既可以是[12,13,14]这样的，也可能是[90000,90001,90002]这样的，还有可能是[12,14,9000001]这样的，只能通过大量测试，找出在各种情况下都均衡的算法，而没有说是在任何一种情况下的最优解法。**


