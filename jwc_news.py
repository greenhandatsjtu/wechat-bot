import re

import requests


def get_results():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
    }
    url = 'http://jwc.sjtu.edu.cn/web/sjtu/198076.htm'
    r = requests.get(url, headers=headers)
    pattern = re.compile('main_r_xuxian.*?blank">(.*?)</a.*?center">\s*(.*?)\s*</td', re.S)
    results = re.findall(pattern, r.text)  # 正则表达式找
    return results


if __name__ == '__main__':
    print(get_results())
