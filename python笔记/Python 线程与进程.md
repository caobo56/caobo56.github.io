Python由于有全锁局的存在（同一时间只能有一个线程执行），并不能利用多核优势。所以，如果程序的多线程进程是CPU密集型的，那多线程并不能带来效率上的提升，相反还可能会因为线程的频繁切换，导致效率下降；如果是IO密集型，多线程进程可以利用IO阻塞等待时的空闲时间执行其他线程，提升效率。

但我们总会有在程序中实现多并发来提升程序运行效率的情形。在这些情形下，可以适当的利用多进程来实现提升效率。

另外，python中，为了解决网络请求密集中，延时等待的问题，我们还可是使用协程来提交效率。

在于IO密集型程序中，多线程应用较多。
但在网络请求密集中，协程比多线程强上很多。
在CPU密集中，还是进程应用更多。
以下是三个例子：

### 线程：


```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time, datetime


# 为线程定义一个函数
def print_time(thread_name):
    for i in range(3):
        now = datetime.datetime.now()
        print(now, thread_name)
        time.sleep(1)

# 不带线程处理的程序
for i in range(5):
    threadname = "threadName" + str(i)
    print_time(threadname)

#线程处理
# for i in range(5):
#     threadname = "threadName"+str(i)
#     t = threading.Thread(target=print_time(threadname))
#     t.start()
```

运行发现，不带线程处理的程序和线程处理的程序运行顺序是一样的：

```
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/caobo/PycharmProjects/ThreadTest/threadTest.py

2017-11-08 11:55:32.889184 threadName0
2017-11-08 11:55:33.890456 threadName0
2017-11-08 11:55:34.894145 threadName0
2017-11-08 11:55:35.899107 threadName1
2017-11-08 11:55:36.900408 threadName1
2017-11-08 11:55:37.903821 threadName1
2017-11-08 11:55:38.907008 threadName2
2017-11-08 11:55:39.909538 threadName2
2017-11-08 11:55:40.914680 threadName2
2017-11-08 11:55:41.918500 threadName3
2017-11-08 11:55:42.921579 threadName3
2017-11-08 11:55:43.925748 threadName3
2017-11-08 11:55:44.928359 threadName4
2017-11-08 11:55:45.931913 threadName4
2017-11-08 11:55:46.932414 threadName4

Process finished with exit code 0
```

每个线程执行完需要3秒，依次执行线程，总耗时15秒。

### 进程

```
# 进程处理
if __name__ == "__main__":
    for i in range(5):
        threadName = "threadName" + str(i)
        p = multiprocessing.Process(target=print_time, args=(threadName,))
        p.start()
```

进程处理运行结果如下：

```
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/caobo/PycharmProjects/ThreadTest/threadTest.py
2017-11-08 11:58:44.045175 threadName0
2017-11-08 11:58:44.046196 threadName1
2017-11-08 11:58:44.047036 threadName2
2017-11-08 11:58:44.048071 threadName3
2017-11-08 11:58:44.049010 threadName4
2017-11-08 11:58:45.045841 threadName0
2017-11-08 11:58:45.046783 threadName1
2017-11-08 11:58:45.048291 threadName2
2017-11-08 11:58:45.048476 threadName3
2017-11-08 11:58:45.050095 threadName4
2017-11-08 11:58:46.046989 threadName0
2017-11-08 11:58:46.047063 threadName1
2017-11-08 11:58:46.048629 threadName2
2017-11-08 11:58:46.049239 threadName3
2017-11-08 11:58:46.050937 threadName4

Process finished with exit code 0
```

每个进程执行完需要3秒，并发执行线程，总耗时3秒。

### 进程池

```
# 进程池处理
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    for i in range(5):
        threadName = "threadName" + str(i)
        pool.apply_async(print_time, (threadName,))
    pool.close()
    pool.join()
    print("Sub-process(es) done.")
```

进程池处理结果如下：

```
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/caobo/PycharmProjects/ThreadTest/threadTest.py
2017-11-08 12:01:03.557402 threadName0
2017-11-08 12:01:03.557552 threadName1
2017-11-08 12:01:03.557686 threadName2
2017-11-08 12:01:03.557827 threadName3
2017-11-08 12:01:04.558322 threadName2
2017-11-08 12:01:04.558306 threadName0
2017-11-08 12:01:04.558311 threadName1
2017-11-08 12:01:04.558322 threadName3
2017-11-08 12:01:05.558841 threadName1
2017-11-08 12:01:05.558833 threadName2
2017-11-08 12:01:05.558841 threadName0
2017-11-08 12:01:05.558845 threadName3
2017-11-08 12:01:06.560105 threadName4
2017-11-08 12:01:07.561340 threadName4
2017-11-08 12:01:08.561577 threadName4
Sub-process(es) done.

Process finished with exit code 0
```

由于设置了进程并发的数量为4，所以，前三秒执行的都是前四个进程的内容（每个进程执行完需要三秒），进程5只能在前四个进程执行完成之后，才开始执行。总耗时6秒。

修改进程并发数量为5：

```
# 进程池处理
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=5)
    for i in range(5):
        threadName = "threadName" + str(i)
        pool.apply_async(print_time, (threadName,))
    pool.close()
    pool.join()
    print("Sub-process(es) done.")
```

运行结果如下：

```
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/caobo/PycharmProjects/ThreadTest/threadTest.py
2017-11-08 12:12:17.210982 threadName0
2017-11-08 12:12:17.211084 threadName1
2017-11-08 12:12:17.211188 threadName2
2017-11-08 12:12:17.211335 threadName3
2017-11-08 12:12:17.211451 threadName4
2017-11-08 12:12:18.211480 threadName0
2017-11-08 12:12:18.211481 threadName2
2017-11-08 12:12:18.211480 threadName1
2017-11-08 12:12:18.211785 threadName3
2017-11-08 12:12:18.211787 threadName4
2017-11-08 12:12:19.211773 threadName2
2017-11-08 12:12:19.211784 threadName0
2017-11-08 12:12:19.212676 threadName1
2017-11-08 12:12:19.212679 threadName4
2017-11-08 12:12:19.212679 threadName3
Sub-process(es) done.

Process finished with exit code 0
```

修改设置进程并发的数量为5，所以，所有5个进程能够同步执行。每个进程执行完需要三秒，总耗时3秒。


