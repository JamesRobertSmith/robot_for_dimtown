import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 "
                  "Safari/537.36 "
    }
url = "https://dimtown.com/dmmt/tujihuace"
# 获取url_list

res = requests.get(url=url, headers=headers)
html = res.text
soup = BeautifulSoup(html, 'lxml')
page_set = soup.find('ul', attrs={"class": "update_area_lists cl", "id": "index_ajax_list"}).find_all('div', attrs={
    "class": "kzpost-data"})
data_set = []
for page in page_set:
    data = {
        "url": page.find('a').get('href'),
        "title": page.find('a').get('title'),
        "popular": int(page.find('span', attrs={"class": "fl-eye"}).text),
        "like": int(page.find('span', attrs={"class": "fr-thumbs"}).text)
    }
    data_set.append(data)






