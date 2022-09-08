import requests
import os
from bs4 import BeautifulSoup
from robot import data_set, headers
# 获取图集

for data in data_set:
    url = data.get("url")
# success
    res = requests.get(url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
# success
    images_url = soup.find('div', attrs={"class": "content_left"}).select('p img')
    path = "./resources/{}".format(data.get('title'))
    if not os.path.exists(path):
        os.makedirs(path)
    for image_url in images_url:
        url = image_url.get('src')
        image = requests.get(url, headers=headers).content
# success
        with open(path+"/page{}.jpg".format(images_url.index(image_url)), 'wb+') as f:
            f.write(image)

# 测试
# url = data_set[0].get("url")
# res = requests.get(url, headers=headers)
# html = res.text
# soup = BeautifulSoup(html, 'lxml')
# images_url = soup.find_all('img', attrs={"width": "1080", "height": "1550"})
# url = images_url[0]
# url = url.get('src')
# image = requests.get(url, headers=headers).content
# with open("./resources/page1.jpg", 'wb+') as f:
#     f.write(image)

# print("{}{}".format("好", "耶"))
# print(data_set[0].get('title'))
# for data in data_set:
#     print(data)
