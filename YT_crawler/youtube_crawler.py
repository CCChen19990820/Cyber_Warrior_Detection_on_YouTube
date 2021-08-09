import requests
import re,time
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import csv
import pandas as pd


video_dic = {}
query = input("ex.蔡英文:")
js = 'var q=document.documentElement.scrollTop=1000000'
url = 'https://www.youtube.com/user/newsebc/search?query='+query
#url = 'https://www.youtube.com/channel/UCIU8ha-NHmLjtUwU7dFiXUA/search?query='+query
last= None

# 打開瀏覽器
driver = webdriver.Chrome('C:/Users/Jeff/Downloads/chromedriver.exe')
driver.implicitly_wait(3)
driver.get(url)

for i in range(1,50):
    driver.execute_script(js)
    time.sleep(2)

# 已完整展開的頁面
soup = BeautifulSoup(driver.page_source, "html.parser")
#print(soup.text)

# 儲存資料 list    
data = []
data.append(['video_id', 'video_uploadtime', 'video_view' , 'video_title'])

upload = 0
correct = True

# parse 頁面
for i in soup.select("ytd-video-renderer"):
    #video_url = 'https://www.youtube.com' + i.select(".yt-simple-endpoint")[0]["href"].strip()
    video_url = i.select(".yt-simple-endpoint")[0]["href"].strip()
    video_time = i.select(".yt-simple-endpoint")[1]['aria-label'].strip()
    
    
    count1 = video_time.find('上傳者：東森新聞 CH51') + 14
    #count1 = video_time.find('上傳者：三立新聞網SETN') +14
    count2 = video_time.find('觀看次數') + 5
    count3 = video_time.find('上傳者：東森新聞 CH51')
    #count3 = video_time.find('｜三立新聞網SETN.com')
    
    #print(video_url[9:20])
    #print(video_time[count1:])
    #print(video_time[count2:])
    #print(video_time[:count3])
    video_view = str(video_time[count2:])
    video_view = video_view.replace('次','')
    video_view = int(video_view.replace(',',''))
    
    print('%15s %20s %10s %20s' % (video_url[9:20],video_time[count1:count2-5],video_view,video_time[:count3]))
    
    if ' 年前 ' in video_time :
        locate = (video_time.find(' 年前 '))
        print(video_time[count1:locate])
        print(video_time[locate:])
        print(video_time[count1:])
        #print('時間為 %s |end' % (video_time[count1:locate]))
        upload = int(video_time[count1:locate])*365
    elif '個月前' in video_time :
        locate = (video_time.find(' 個月前 '))
        #print(video_time[count1:locate])
        #print(video_time[locate:])
        #print(video_time[count1:])
        #print('時間為' + video_time[count1:locate] + '|end')
        upload =  int(video_time[count1:locate])*30
    else:
        upload = 0
    if upload >= 120 and upload <= 730 and correct == True:
        data.append([video_url[9:20],video_time[count1:(count2)-5],video_view,video_time[:count3]])

    
    time.sleep(.5)

#print(data)
df = pd.DataFrame(data)
#print(df)
df.to_csv(r'C:/Users/Jeff/Desktop/專題資料/東森_'+ query +'.csv', index = False,encoding='utf_8_sig')
print('finish')
driver.close()
