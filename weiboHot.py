import requests
from lxml import etree


def get_html(url):
    r = requests.get(url)
    print(r.status_code)
    html = etree.HTML(r.text)
    return html


def get_results():
    html = get_html('https://s.weibo.com/top/summary?cate=realtimehot')
    results = html.xpath('//td[@class="td-02"]/a/text()')
    return results


if __name__ == '__main__':
    print(get_results())
