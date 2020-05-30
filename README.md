# wechat-bot
一个自动回复的多功能微信bot

## 使用方法

安装依赖：

```bash
pip install -r requirements.txt
```

然后`python main.py`即可启动bot，微信扫描弹出的二维码使bot登录，然后即可在“文件传输助手”和bot对话。

可在“文件传输助手”输入如下几条命令交互：

+ function：获取所有命令
+ hitokoto：获取一言
+ weibohot：获取当前微博热搜
+ jwcbulletin：获取上海交大教务处网站通知
+ wallpaper：随机获取一张动漫壁纸
+ movie：从豆瓣获取正在上映的电影

## 感谢

[littlecodersh/**ItChat**](https://github.com/littlecodersh/ItChat)