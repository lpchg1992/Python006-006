# 学习笔记
## 网络协议与编程
1. 网络的不同层级一般有对应的通信协议，一般应用层为HTTP等协议；传输层网络层为TCP/IP协议，我们可以通过socket协议建立起TCP或者UDP连接，编写网络服务端和服务端应用；用requests这个HTTP客户端进行HTTP协议的网络请求，结果接收。
2. 我们可以利用socket库来编写socket协议的通信软件。
## HTTP协议与HTML
1. HTTP是网络数据的一种传输协议，除了关注传输内容，我们重点应该关注HTTP协议传递信息时的“头信息”，了解头文件传递的参数，便于了解其机理，有利于爬虫软件模拟正常浏览器的访问。
2. HTML是一种超文本标记语言，由浏览器等解析成为网页等内容。
3. HTML 和 CSS 以及 JS 分别定义网页的布局，样式，行为，都是前端的重要内容。
## 异常处理与上下文管理
1. 对程序可能出现异常的地方，比如文件读写，socket连接等进行异常捕获管理可以增强代码的健壮性。
2. 可以使用with上下文管理器管理具备上下文功能的类及其方法，也可以自己编写适用于上下文管理的类，依照固定范式即可。
## HTTP 的请求方式与Cookie
1. GET和POST都是提交HTTP请求的方式。
2. POST一般用于不显示传递普通字符串信息以及富文本信息/长文本/帐号密码等。
3. 当我们发起请求时，一般服务端会返回cookies信息，其中一般会包含用户登陆信息，有效时间等，如果需要访问要求权限的网页可以用requests带上cookies信息在同一个会话池中访问其相关内容。
## XPATH
1. xpath有其类似于正则表达式的特定语法，单纯用于网页解析时比正则表达式方便。
2. 可以通过特定语法依照比标签属性获取标签属性的值及其内容以及标签内的内容。
## 自顶向下设计
1. 其关键在于，对复杂的问题进行模块化拆分，将一个大问题分为几个小问题，将小问题通过代码进行一一实现。
2. 也就是将每一个方法都抽象出来为函数或者类。
## Scrapy爬虫框架
1. 这一模型包含爬虫部分，引擎部分，调度器部分，下载器部分以及文件处理管道5个部分。
2. 当爬虫需要发起请求，首先通过引擎传递给调度器，由调度器分配任务给下载器，下载器完成下载后通知爬虫，爬虫再通知文件处理管道一次处理。
3. 具体到这个应用可以认为，引擎负责多线程的协调，调度器限制并发请求的大小，调度若干个爬虫获取数据同时调用下载器下载缓存数据，之后由解析器对队列内容进行解析，获取结果，将结果写入本地文件。
# 作业备忘
1. （需提交代码作业）不使用开源框架，基于 TCP 协议改造 echo 服务端和客户端代码，实现服务端和客户端可以传输单个文件的功能。

【已经实现简单的文本文件传输】
2. （需提交代码作业）使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件。

【改为抓取solidot首页新闻标题及内容并保存为json文件】
3. 通过课程代码，熟练掌握 HTTP 协议头、返回码、HTML 等知识点，这些在后面开发 Web 服务端程序时会频繁使用到。

**知呼登陆需要会JS或使用selenium登陆，可用[替代网站](https://www.solidot.org)进行相关操作。**