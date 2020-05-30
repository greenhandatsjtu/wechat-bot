#!/usr/bin/python3
from urllib.parse import urlencode

import requests

url_base = 'https://v1.hitokoto.cn/?'
params = {
    'c': 'a',
    'charset': 'utf-8',
    'encode': 'json'
}
url = url_base + urlencode(params)


def get_content(url):
    results = requests.get(url)
    text = results.json()
    hitokoto = text['hitokoto']
    return hitokoto


def main():
    content = get_content(url)
    return content


if __name__ == '__main__':
    res = get_content(url)
    print(res)
