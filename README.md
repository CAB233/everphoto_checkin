**本脚本是在酷安找到的，但忘记是哪位老哥的了，先在此感谢**

# 时光相册每日签到

部署在腾讯云函数，支持server酱推送

## 获取数据

首先进入[登录界面](https://web.everphoto.cn/#signin)，按F12打开开发工具，进入`网络/Netmork`

然后**一定要选择手机号登录**，输入好手机号和密码后点击登录

在开发工具中找到`auth`一项，找到最底下的`mobile`和`password`，将它们记下

![](https://cdn.jsdelivr.net/gh/CAB233/Image@main/xxx.189y8xwv2940.png)

## 部署

登录[腾讯云](https://console.cloud.tencent.com/scf/)账号，进入云函数控制台，选择`函数服务`，点击`新建`

![](https://cdn.jsdelivr.net/gh/CAB233/Image@main/xxx.5bjqud28htk0.png)

将[代码](https://hub.fastgit.org/CAB233/everphoto_checkin/blob/main/index.py)全部粘贴进去,将`手机号`、`密码`改为上面获得的数据。

根据是否需要推送结果选择填入`server酱sendkey`，可在https://sct.ftqq.com/ 申请自己的sendkey然后修改代码，然后点击`完成`

![](https://cdn.jsdelivr.net/gh/CAB233/Image@main/xxx.150abrp7isyk.png)

然后进行测试，测试成功即可

![](https://cdn.jsdelivr.net/gh/CAB233/Image@main/xxx.538pkro32os0.png)

然后需要配置触发器，即每日何时运行程序

![](https://cdn.jsdelivr.net/gh/CAB233/Image@main/xxx.4ldu7bql1bw0.png)

![](https://cdn.jsdelivr.net/gh/CAB233/Image@main/xxx.1q994sznmslc.png)

Cron表达式自行查阅官方文档。
