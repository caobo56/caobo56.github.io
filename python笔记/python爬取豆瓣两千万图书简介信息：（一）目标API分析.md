# python爬取豆瓣两千万图书简介信息：（一）目标API分析

这是全部的调试过程，我已经整理成为笔记，这里分享给大家：

[python爬取豆瓣两千万图书简介信息：（一）目标API分析](https://www.jianshu.com/p/a1331537544e)

[python爬取豆瓣两千万图书简介信息：（二）简单python请求urllib2](https://www.jianshu.com/p/d378598fc66e)

[python爬取豆瓣两千万图书简介信息：（三）异常处理](https://www.jianshu.com/p/807f4ca8b1ab)

[python爬取豆瓣两千万图书简介信息：（四）多进程并发](https://www.jianshu.com/p/40c3faadd4db)

[python爬取豆瓣两千万图书简介信息：（五）数据库设计](https://www.jianshu.com/p/5258c286f56d)

[python爬取豆瓣两千万图书简介信息：（六）数据库操作类](https://www.jianshu.com/p/916166d20105)

[python爬取豆瓣两千万图书简介信息：（七）代理IP](https://www.jianshu.com/p/1236d69337dc)

[python爬取豆瓣两千万图书简介信息：（八）总结](https://www.jianshu.com/p/012b157ff8f5)


###目标API分析

前一阵一直在看python，偶尔也写一写demo，但一直想写一个大一些的练手项目，偶尔看到豆瓣提供了一个图书简介信息的API：https://api.douban.com/v2/book/1220562
最后一位即 图书的id
稍微测试了一下，1000001 和 21220562 都有相应的图书简介信息：
而且 1000001 的API返回结果如下：

![屏幕快照 2017-07-10 上午9.01.43.png](http://upload-images.jianshu.io/upload_images/1136127-f3c488f471ce1d62.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在标记红框的位置出现了“第一”，“豆瓣的第一个条目”，“一本见证了豆瓣诞生的书”等字段。这说明id为1000001的《十一位牺牲在建国前的中共无衔军事家》 即为豆瓣的书id 的第一条。
把id依次递增，即可得到对应id的图书信息。
21220562 这个两千万级别的id ，是随手测试到的，测了31220562 ，返回值为：

```
{"msg":"book_not_found","code":6000,"request":"GET \/v2\/book\/31220562"}
```

再随意测试几个，21220562 以下的有图书简介信息的情况较多，21220562以上的几乎没有。

那，这一次我们爬取的目标就很明确了，就是爬取豆瓣API的所能提供的 两千万图书简介信息。

计划是用python发起网络请求，然后解析数据，并将数据放到mysql数据库中。具体的实现步骤，将在后面的文章中发布。


