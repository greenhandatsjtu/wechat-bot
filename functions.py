import time


def time_now():
    """返回时间字典"""
    nowtime = time.localtime()
    now = dict()
    now['day'] = time.strftime('%Y-%m-%d', nowtime)  # 年-月-日
    now['month'] = nowtime.tm_mon  # 月份
    now['hour'] = nowtime.tm_hour  # 小时
    now['minute'] = nowtime.tm_min  # 分钟
    now['second'] = time.strftime('%H:%M:%S', nowtime)  # 小时：分：秒
    return now
