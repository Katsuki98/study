# scrape all songs
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.apple.com/itunes/charts/songs/'
html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content,'html.parser')
ul = soup.find('section','section chart-grid')
li_list = ul.find_all('li')
music = []

for li in li_list:
    post = {}
    a = li.h3.a
    b = li.h4.a
    post['names'] = a.string
    post['artists'] = b.string
    music.append(post)

import pyexcel
pyexcel.save_as(records=music,
    dest_file_name='ITunes top songs.xlsx')

# download all songs
from youtube_dl import YoutubeDL
videos = []
for post in music:
    video = "'" + post['names'] + ' ' + post ['artists'] + "'"
    videos.append(video)

for i in range (len(videos)):
    options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
    }
    dl = YoutubeDL(options)
    dl.download([videos[i]])