# Auto Wemeet


## 特性
- 腾讯会议定时自动入会
- 只需Python运行环境，只支持Windows系统
- 支持同时预定多个会议
- 通过windows任务计划程序来完成定时，无界面，无后台消耗


## 使用方法
1. 下载本项目代码，在`meetings.txt`中按照例子中的格式填入会议的时间以及会议编码，格式如下
```
2022年07月15日15:00,932222232
```
2. 执行下列命令
```bash
python auto_wemeet.py
```
3. `meetings.txt`中每一行都会被注册为一个Windows定时任务，你可以在Windows任务计划程序中看到，任务计划程序可以通过"win+R"打开运行并键入"taskschd.msc"来启动
![](https://s1.ax1x.com/2022/07/21/jqNVPO.png)

4. 请注意不要删除和移动本项目，因为到达设定的时间，计划任务是通过python执行本项目的代码来启动腾讯会议的。
