import requests
from bs4 import BeautifulSoup
from robot import data_set, headers

data = data_set[1]
url = data.get("url")
# success
res = requests.get(url, headers=headers)
html = res.text
soup = BeautifulSoup(html, 'lxml')
# success
images_url = soup.find('div', attrs={"class": "content_left"}).p.find_all('img')
# for image_url in images_url:
#     url = image_url.get('src')
#     image = requests.get(url, headers=headers).content
# # success
#     with open("./resources/{}-page{}.jpg".format(data.get('title'), images_url.index(image_url)), 'wb+') as f:
#         f.write(image)
print(images_url)