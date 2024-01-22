# 概述
本项目是基于Python的深澜校园网登录认证客户端，适用于嘉兴大学/嘉兴学院，能够通过命令行登录上网。

本项目基于知乎博主“东风破”的原理和代码实现：[深澜校园网登录的分析与python实现-北京理工大学版](https://zhuanlan.zhihu.com/p/122556315)，
主要修改的地方是 ac_id 改为 5 以及认证服务器改为 portal.zjxu.edu.cn。

有任何意见和建议，欢迎随时反馈。

___
# 文件说明
|文件名|用途|
|:-:|:-:|
|core/|核心程序包，包含登录和加密等模块|
|utils|额外的工具包，包含保持在线功能以及基于selenium实现的登录模块|
|login.py|主程序|
|requirements.txt|依赖包列表|

___
# 使用方法
python login.py -u 上网账号/学号 -p 上网密码

___
# 运行结果

如果已经在线，会显示“The login result is: ip_already_online_error”。

如果登录成功，会显示“The login result is: login_ok”。

注销功能暂未实现。

---
# 依赖的包
selenium~=4.16.0, requests~=2.26.0, encryption~=0.0.1
