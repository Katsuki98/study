from urllib.request import urlopen
from bs4 import BeautifulSoup

# 1. Download web page
url = 'http://dantri.com.vn'
# # 1.1 Create connection
# conn = urlopen(url)
# # 1.2 Read
# data = conn.read()
# # 1.3 Decode
# html_content = data.decode('utf-8')
html_content = urlopen(url).read().decode('utf-8')
# print(html_content)

# save html to file
# f = open("dantri.html", "wb")
# f.write(html_content)
# f.close()

# 2. Extract ROI (Region Of Interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())
# find by 'class'
ul = soup.find('ul','ul1 ulnew')
# print(ul.prettify())

# 3. Extract data
li_list = ul.find_all('li')
abc = []
for li in li_list:

# print(li.prettify())
# h4 = li.find('h4')
# a = h4.find('a')
    post = {}
    a = li.h4.a
    # print(a.string)
    # print(url + a['href'])
    # print('* ' *30)
    post['title'] = a.string
    post['url'] = url + a['href']
    abc.append(post)

import pyexcel
pyexcel.save_as(records=abc,
     dest_file_name="dantri.xlsx")