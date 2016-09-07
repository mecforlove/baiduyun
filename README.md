# Yunhelper
一款基于python的仿shell风格的百度网盘在线管理工具，提供文件管理、文件/文件夹下载、关键字批量离线下载等功能。
> 引言：**Yunhelper**是一款强大的百度云在线管理工具，其最大的特色是交互方式为字符界面，操作方式仿shell风格，上手简单但功能强大。

##目录结构
``` bash
Yunhelper/
    ├── libs
    │   ├── __init__.py
    │   ├── pcs.py
    │   ├── source.py
    │   └── utils.py
    ├── lx_client.py
    ├── manager.py
    └── README.md
```
其中，libs目录下的模块对一些网络操作进行了封装，lx_client和manager.py为主程序。
- **lx_client**：离线下载主程序，运行格式为`./lx_client [keywords]`，其中keywords支持关键字、番号等。输入命令行回车运行，程序会自动下载10部资源（防止百度和谐）并将其保存着“/我的资源/keywords”下面。

- **manager.py**：在线文件管理器，支持文件浏览、文件/文件夹下载等功能。
>**注意**：`keywords`不能包含空格。

##功能说明
- **帮助界面**
``` bash
    Welcome to Yunhelper!  This is the help utility.
    quit----------------------退出程序
    cd [文件夹名称]-----------类似于cd和ls合起来的功能
    pwd-----------------------打印当前目录
    dl [文件名]---------------下载文件至本地
    dld [文件夹名]------------递归下载文件至本地
    ?-------------------------打印此帮助信息
```
- **文件管理**
``` bash
[@/]>>cd 物联网1301
物联网1301班级工作汇报.pptx
物联网1301班委名单.xls
物联网1301普通话测试报名表.xls
物联网1301特色团日_by_mec.zip
物联网1301通讯录.xlsx
物联网1班.xlsx
[@/物联网1301/]>>cd ..
```
- **文件夹递归下载**
``` bash
[@/]>>dld 来自：SM-A5000
/来自：SM-A5000/DCIM/Camera/20160329_171245-1.jpg--------------------downloaded successfully
/来自：SM-A5000/DCIM/Camera/20160329_171255-1.jpg--------------------downloaded successfully
```
- **离线下载**
``` bash
pi@raspberrypi:~/py_projects/Yunhelper $ ./lx_client.py 人在囧途
task: 1553645743------deleted!
{"task_id":1553924051,"rapid_download":0,"request_id":239951904}
{"task_id":1553924263,"rapid_download":1,"request_id":239996378}
{"task_id":1553924350,"rapid_download":0,"request_id":241324145}
{"task_id":1553924364,"rapid_download":1,"request_id":241397954}
{"task_id":1553924563,"rapid_download":1,"request_id":241495346}
{"task_id":1553924587,"rapid_download":0,"request_id":242481838}
{"task_id":1553924602,"rapid_download":0,"request_id":242607145}
{"task_id":1553924622,"rapid_download":1,"request_id":242685303}
{"task_id":1553924832,"rapid_download":1,"request_id":242810700}
{"task_id":1553924840,"rapid_download":0,"request_id":243813444}
{"task_id":1553924866,"rapid_download":0,"request_id":243873697}
```
##部署环境
Linux系统 Python2.6+
## 反馈与建议
- 微博：[@张光超mec](http://weibo.com/u/1672920821)
- 邮箱：<mecforlove@outlook.com>
