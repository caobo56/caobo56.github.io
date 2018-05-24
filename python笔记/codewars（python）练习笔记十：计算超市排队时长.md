# codewars（python）练习笔记十：计算超市排队时长

### 题目
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

The function has two input variables:

* customers: an array (list in python) of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
* n: a positive integer, the number of checkout tills.

The function should return an integer, the total time required.

EDIT: A lot of people have been confused in the comments. To try to prevent any more confusion:

* There is only ONE queue, and
* The order of the queue NEVER changes, and
* Assume that the front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
* The diagram on the wiki page I linked to at the bottom of the description may be useful.

So, for example:
```
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
```
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool

Test case:
queue_time([2,3,10], 2)  should be 12
queue_time([], 5)  should be 0
queue_time([2], 5)  should be 2
queue_time([1,2,3,4,5], 100) should be 5
queue_time([2,3,10,2,3], 2) should be 12

### 题目大意:
这道题是经典的超市购物排队问题：有一个队列 customers[]，队列中每个元素是当前顾客的处理时长，有 n 个购物台,可以同时处理n个客户。这是题目大意，求的是队列的处理时长。
特别注意：
* 只有一个队列，
* 队列处理顺序不能变，
* 假设队列中的前面的人(即数组/列表中的第一个元素)在有购物台空闲的时候就会继续前进。

### 我的解法：
```
#!/usr/bin/python

def queue_time(customers, n):
    if customers == []:
        return 0
    if len(customers) < n:
        return max(customers)
    list_temp = [customers[i] for i in range(0,n)]
    for item in range(n,len(customers)):
        list_temp[list_temp.index(min(list_temp))] += item
    return max(list_temp)
```

### 牛逼解法：
```
#!/usr/bin/python

def queue_time(customers, n):
    list_temp = [0]*n
    for item in customers:
        list_temp[list_temp.index(min(list_temp))] += item
    return max(list_temp)
```

我跟最牛逼的解法之间的差距在于：我意识到了    list_temp 通过 [customers[i] for i in range(0,n)]这样创建，绝对不是最佳解法。但没有想到，可以直接生成长度为n 的空数组。

### 另一个牛逼解法：
```
def queue_time(customers, n):
    queues = [0] * n
    for i in customers:
        queues.sort()
        queues[0] += i
    return max(queues)
```
相对于上一个，sort() 要比min()  算法复杂度高一些。

### 另一个牛逼解法：
```
def queue_time(cs, n):
    def serve(q,c): return sorted([q[0]+c] + q[1:])
    return max(reduce(serve, cs, [0]*n))
```
利用reduce(),相当精奇的思路。

