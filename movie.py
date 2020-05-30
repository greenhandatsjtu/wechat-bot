import requests
from bs4 import BeautifulSoup


def getMovie():
    """获取豆瓣热映电影和评分，返回列表"""
    url = 'https://movie.douban.com/cinema/nowplaying/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)\
             Chrome/52.0.2743.116 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.select('#nowplaying .list-item')
    score = list()
    for i in results[0:10]:
        score.append(i['data-title'] + ': ' + i['data-score'])
    return score


if __name__ == '__main__':
    movies = getMovie()
    print(movies)
