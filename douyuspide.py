"""
https://www.douyu.com/gapi/rkc/directory/0_0/2
https://www.douyu.com/gapi/rkc/directory/0_0/3
"""

import requests
from douyu_real_url import DouYu

flag = True


# 请求网页
def page_def(url, ua):
    resp = requests.get(url, headers=ua)
    json_text = resp.json()
    return json_text


# 解析网页
def info_def(json_text):
    douyu_list = []
    for i in range(len(json_text['data']['rl'])):
        data_list = json_text['data']['rl'][i]
        s = DouYu(data_list['rid'])
        temp_dict = {
            'rid': data_list['rid'],  # 房间ID
            'rn': data_list['rn'],  # 房间名
            'nn': data_list['nn'],  # 主播名
            'ol': data_list['ol'],  # 人气值
            'c2name': data_list['c2name'],  # 分类
            'url': 'https://www.douyu.com/' + str(data_list['rid']),
            'real_url': s.get_real_url()
        }

        if temp_dict['ol'] > 50000:
            douyu_list.append(temp_dict)
    return douyu_list


# 写入csv
def csv_def(douyu_list):
    import csv
    with open(r'E:\douyu.csv', 'a', encoding='utf-8-sig', newline='') as cf:
        w = csv.DictWriter(cf, fieldnames=['rid', 'rn', 'nn', 'ol', 'c2name', 'url', 'real_url'])
        w.writeheader()
        w.writerows(douyu_list)
        print("爬取完成！")


# 主函数
def main_def():
    ua = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}
    for i in range(1, 11):
        url = 'https://www.douyu.com/gapi/rkc/directory/0_0/%d' % i
        json_text = page_def(url, ua)
        douyu_list = info_def(json_text)
        print("正在爬取第%d" % i + "页")
        csv_def(douyu_list)


if __name__ == '__main__':
    main_def()

