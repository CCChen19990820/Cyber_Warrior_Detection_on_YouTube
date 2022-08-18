# Cyber_Warrior_Detection_on_YouTube

1.introduction

This is my College graduate project. In this project, I'm discussing about thecyber warrior on YouTube video. The cyber warrior usually appear in the vidoes' comments. Thus, I focus on analyzing the user behaviour in the comment. There are three analysis method that I use. Community Detection, Time Series Analysis, and Association Analysis respectively.


2.First, I see the website(https://tw.noxinfluencer.com/youtube-channel-rank/top-100-tw-news%20%26%20politics-youtuber-sorted-by-avgview-weekly) to collect the top famous political channels

3.Run youtube_crawler.py in YT_crawler file, which is to crawl the YT videoes id list.

4.Enter the videoes' id list on Facepager(https://github.com/strohne/Facepager) and get the video information I want in the video comment, including comments, users' id, time, comment id, and so on.

5.Save the data the database.

6.Run the analysis method code you want in three files. In my experiments, I use six channel as exmaple, 中天, 三立, 東森, 比特王出任務, 關鍵時刻, 少康戰情室. I use Community Detection, Time Series Analysis, and Association Detection to research the account interaction on the Youtube video.
