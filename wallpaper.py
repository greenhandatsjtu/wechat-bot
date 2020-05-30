import os
import random

import requests

from functions import time_now


def get_wallpaper():
    """利用acgclub的api获取壁纸，返回编号"""
    today = time_now()['day']
    if not os.path.exists('./wallpapers'):
        os.makedirs('./wallpapers')

    # cache
    if os.path.exists('./wallpapers/{}.txt'.format(today)):
        with open('./wallpapers/{}.txt'.format(today), 'r') as f:
            url = f.read()
            url = url.split('\n')
    else:
        r = requests.get('https://rabtman.com/api/v2/acgclub/pictures')
        json = r.json()
        url = list()
        for i in json['data']:
            url += i['imgUrls']  # 获取所有图片的url
        with open('./wallpapers/{}.txt'.format(today), 'w') as f:
            f.write('\n'.join(url))
    k = random.randint(0, len(url))
    print(k)
    r_pic = requests.get(url[k])  # 随机获得一张图片
    number = 1  # 对图片编号
    while os.path.exists('./wallpapers/{}_{}.jpg'.format(today, number)):
        number += 1  # 若存在此编号，则加一
    with open('./wallpapers/{}_{}.jpg'.format(today, number), 'wb') as f:
        f.write(r_pic.content)
    return number


if __name__ == '__main__':
    get_wallpaper()
