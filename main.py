from urllib.parse import urlencode

import itchat
from itchat.content import *

import functions
import hitokoto
import jwc_news
import movie
import wallpaper
import weiboHot

function = {  # 用于返回列表告诉用户已有功能及关键词
    'hitokoto': '获取一言',
    'weibohot': '获取当前微博热搜',
    'jwcbulletin': '获取教务处通知',
    'wallpaper': '获取壁纸',
    'movie': '获取热映电影'
}
# 构造调用一言api所需url
url_base = 'https://v1.hitokoto.cn/?'
params = {
    'c': 'a',
    'charset': 'utf-8',
    'encode': 'json'
}
url = url_base + urlencode(params)


@itchat.msg_register(TEXT, isFriendChat=True)
def reply(msg):
    print(msg['Text'])
    if msg['Text'] == 'function':
        function_text = str()
        for i, j in function.items():
            function_text = function_text + i + ': ' + j + '\n'
        msg.user.send(function_text)
        print('发送成功')
    elif msg['Text'] == 'hitokoto':
        content = hitokoto.get_content(url)
        msg.user.send(content)
        print('发送成功')
    elif msg['Text'] == 'weibohot':
        results = weiboHot.get_results()
        now = functions.time_now()['second']
        msg.user.send('下面是' + now + '时的微博热搜:\n')
        msg.user.send('\n'.join(results[0:10]))
        print('发送成功')
    elif msg['Text'] == 'jwcbulletin':
        results = jwc_news.get_results()
        print(results)
        results_text = str()
        for i in results[0:10]:
            results_text = results_text + i[1] + '  ' + i[0] + '\n'
        msg.user.send(results_text)
        print('发送成功')
    elif msg['Text'] == 'wallpaper':
        today = functions.time_now()['day']
        number = wallpaper.get_wallpaper()
        msg.user.send('@img@%s' % './wallpapers/{}_{}.jpg'.format(today, number))
        print('./wallpapers/{} {}.jpg'.format(today, number))
        print('发送成功')
    elif msg['Text'] == 'movie':
        movies = movie.getMovie()
        msg.user.send('\n'.join(movies))
        print('发送成功')


itchat.auto_login()
itchat.run()
