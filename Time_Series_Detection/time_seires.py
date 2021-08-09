import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import csv
import math
import datetime
import matplotlib.dates as mdates
import time
from difflib import SequenceMatcher



Channelquery = input("中天、三立、東森，Choose one to search:")

store_data = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_'+Channelquery+'柯文哲.csv',encoding='utf-8')
store_data2 = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_'+Channelquery+'蔡英文.csv',encoding='utf-8')
store_data3 = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_'+Channelquery+'韓國瑜.csv',encoding='utf-8')
reply_data = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/toplevel_get_reply/'+Channelquery+'.csv',encoding='utf-8')
comment_con_videoId = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/'+Channelquery+'toplevelcommentId.csv',encoding='utf-8')



length = len(store_data['snippet.videoId'])
length2 = len(store_data2['snippet.videoId'])
length3 = len(store_data3['snippet.videoId'])

##############################################################################################################
def Build_Video_Id_List(video_id, temp1_id, video_count):

	for i in range(0,length):
		if str(store_data['snippet.videoId'][i]) in temp1_id.keys():
			continue
		elif str(store_data['snippet.videoId'][i]) == 'nan':
			continue
		elif store_data['object_type'][i] == 'data':
			temp1_id.update({store_data['snippet.videoId'][i]:video_count})
			video_count+=1
			video_id.append(store_data['snippet.videoId'][i])

	for i in range(0,length2):
		if str(store_data2['snippet.videoId'][i]) in temp1_id.keys():
			continue
		elif str(store_data2['snippet.videoId'][i]) == 'nan':
			continue
		elif store_data2['object_type'][i] == 'data':
			temp1_id.update({store_data2['snippet.videoId'][i]:video_count})
			video_count+=1
			video_id.append(store_data2['snippet.videoId'][i])

	for i in range(0,length3):
		if str(store_data3['snippet.videoId'][i]) in temp1_id.keys():
			continue
		elif str(store_data3['snippet.videoId'][i]) == 'nan':
			continue
		elif store_data3['object_type'][i] == 'data':
			temp1_id.update({store_data3['snippet.videoId'][i]:video_count})
			video_count+=1
			video_id.append(store_data3['snippet.videoId'][i])

	print('Video Count = '+str(video_count))

##############################################################################################################
def Build_Top_Level_User_Id_List(user_id, temp2_id, user_appearance, user_count, comment_count, last_count):

	for i in range(0,length):
		if str(store_data['object_type'][i]) == 'data':
			comment_count+=1

		#統計各個user出現次數存到字典
		if str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]) not in user_appearance.keys() and str(store_data['object_type'][i]) == 'data':
			user_appearance.update({store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]:1})
		elif str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]) in user_appearance.keys() and str(store_data['object_type'][i]) == 'data':
			last_count = user_appearance.get(str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i])) + 1
			user_appearance.update({store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]:last_count})

		#建立使用者字典
		if str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]) in temp2_id.keys():
			continue
		elif str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]) == 'nan':
			continue
		elif str(store_data['object_type'][i]) == 'data':
			temp2_id.update({store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]:user_count})
			user_count+=1
			user_id.append(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i])


	for i in range(0,length2):
		if str(store_data2['object_type'][i]) == 'data':
			comment_count+=1

		#統計各個user出現次數存到字典
		if str(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]) not in user_appearance.keys() and str(store_data2['object_type'][i]) == 'data':
			user_appearance.update({store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]:1})
		elif str(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]) in user_appearance.keys() and str(store_data2['object_type'][i]) == 'data':
			last_count = user_appearance.get(str(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i])) + 1
			user_appearance.update({store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]:last_count})

		#建立使用者字典
		if str(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]) in temp2_id.keys():
			continue
		elif str(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]) == 'nan':
			continue
		elif str(store_data2['object_type'][i]) == 'data':
			temp2_id.update({store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]:user_count})
			user_count+=1
			user_id.append(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i])


	for i in range(0,length3):
		if str(store_data3['object_type'][i]) == 'data':
			comment_count+=1

		#統計各個user出現次數存到字典
		if str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]) not in user_appearance.keys() and str(store_data3['object_type'][i]) == 'data':
			user_appearance.update({store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]:1})
		elif str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]) in user_appearance.keys() and str(store_data3['object_type'][i]) == 'data':
			last_count = user_appearance.get(str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i])) + 1
			user_appearance.update({store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]:last_count})

		#建立使用者字典
		if str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]) in temp2_id.keys():
			continue
		elif str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]) == 'nan':
			continue
		elif str(store_data3['object_type'][i]) == 'data':
			temp2_id.update({store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]:user_count})
			user_count+=1
			user_id.append(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i])

##############################################################################################################
def Build_Reply_comment_user_id_list(comment_count, user_count):

	for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
		if str(reply_data['object_type'][i]) == 'data':
			comment_count+=1
	#	if reply_data['snippet.authorChannelId.value'][i] == 'UC-OfcFYXBywVpbHVaM1Y-Jw' and reply_data['object_type'][i] == 'data':
	#		print(reply_data['snippet.publishedAt'][i],end="//")

		#統計各個user出現次數存到字典
		if str(reply_data['snippet.authorChannelId.value'][i]) not in user_appearance.keys() and str(reply_data['object_type'][i]) == 'data':
			user_appearance.update({reply_data['snippet.authorChannelId.value'][i]:1})
		elif str(reply_data['snippet.authorChannelId.value'][i]) in user_appearance.keys() and str(reply_data['object_type'][i]) == 'data':
			last_count = user_appearance.get(str(reply_data['snippet.authorChannelId.value'][i])) + 1
			user_appearance.update({reply_data['snippet.authorChannelId.value'][i]:last_count})

		#建立使用者字典
		if str(reply_data['snippet.authorChannelId.value'][i]) in temp2_id.keys():
			continue
		elif str(reply_data['object_type'][i]) == 'data':
			temp2_id.update({reply_data['snippet.authorChannelId.value'][i]:user_count})
			user_count+=1
			user_id.append(reply_data['snippet.authorChannelId.value'][i])
	print('User Count = '+str(user_count))
	#user_count = temp
	print('Comment Count ='+str(comment_count))

##############################################################################################################
def Build_Top_Level_CommentIds_VideoId():

	for i in range(0,len(comment_con_videoId['commentId'])):
		parentId_videoId.update({comment_con_videoId['commentId'][i]:comment_con_videoId['parent.videoId'][i]})
	#print(parentId_videoId)

##############################################################################################################
def Build_reply_userId_with_videoId_2_dimension_list():

	for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
		if str(reply_data['object_type'][i]) == 'data' and str(reply_data['snippet.parentId'][i]) != 'nan':
			#print(reply_data['snippet.authorChannelId.value'][i],parentId_videoId[str(reply_data['snippet.parentId'][i])])
			r_userId_to_videoId.append([str(reply_data['snippet.authorChannelId.value'][i]),parentId_videoId[str(reply_data['snippet.parentId'][i])]])
	#print(r_userId_to_videoId)

##############################################################################################################
class time():
	def __init__(self,name):
		self.name = name
		self.timestamp = []
		self.comment = []
		self.dict = {}
		self.count = 0
		self.weight = 0
		self.com_count = 0
	
	def add(self,timepoint):
			self.timestamp.append(timepoint)	
			self.count+=1
	def add_comment(self,text):
			self.comment.append(text)
			self.com_count+=1
	
	def sort_timestamp(self):
		self.timestamp.sort()

	def get_count(self):
		return self.count

	def get_timestamp(self):
		return self.timestamp

	def get_comment(self):
		return self.comment
	
	def add_weight(self):
		self.weight+=1

	def get_weight(self):
		return self.weight

	def calculate_weight(self):
		for i in range(0,len(self.timestamp)-1):	
			temp = self.timestamp[i]
			year = int(temp[0:4])
			month = int(temp[5:7])
			day = int(temp[8:10])
			hour = int(temp[11:13])
			minu = int(temp[14:16])
			secs = int(temp[17:19])
			#print(temp)
			#print(year,month,day,hour,minu,secs)
			first = datetime.datetime(year,month,day,hour,minu,secs,0)
			
			temp = self.timestamp[i+1]
			year = int(temp[0:4])
			month = int(temp[5:7])
			day = int(temp[8:10])
			hour = int(temp[11:13])
			minu = int(temp[14:16])
			secs = int(temp[17:19])
			#print(temp)
			#print(year,month,day,hour,minu,secs)
			second = datetime.datetime(year,month,day,hour,minu,secs,0)
			
			time_minus = (second-first).seconds
			if time_minus <= 60:
				self.add_weight()

##############################################################################################################
def Build_timestamp_class(malicious_count):

	for i in user_id:
		time_list.append(i)
	for i in range(0,len(user_id)):
		time_list[i] = time(user_id[i])

	for i in range(0,length):
		if str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]) != 'nan' and str(store_data['object_type'][i]) == 'data':
			time_list[temp2_id.get(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add(store_data['snippet.topLevelComment.snippet.publishedAt'][i])
			time_list[temp2_id.get(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add_comment(store_data['snippet.topLevelComment.snippet.textOriginal'][i])

	for i in range(0,length2):
		if str(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]) != 'nan' and str(store_data2['object_type'][i]) == 'data':
			time_list[temp2_id.get(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add(store_data2['snippet.topLevelComment.snippet.publishedAt'][i])
			time_list[temp2_id.get(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add_comment(store_data2['snippet.topLevelComment.snippet.textOriginal'][i])

	for i in range(0,length3):
		if str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]) != 'nan' and str(store_data3['object_type'][i]) == 'data':
			time_list[temp2_id.get(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add(store_data3['snippet.topLevelComment.snippet.publishedAt'][i])
			time_list[temp2_id.get(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add_comment(store_data3['snippet.topLevelComment.snippet.textOriginal'][i])

	for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
		if str(reply_data['snippet.authorChannelId.value'][i]) != 'nan' and reply_data['object_type'][i] =='data':
			time_list[temp2_id.get(reply_data['snippet.authorChannelId.value'][i])].add(reply_data['snippet.publishedAt'][i])
			time_list[temp2_id.get(reply_data['snippet.authorChannelId.value'][i])].add_comment(reply_data['snippet.textOriginal'][i])

	for i in range(0,len(time_list)):
		time_list[i].sort_timestamp()
		out = time_list[i].get_timestamp()
		time_list[i].calculate_weight()
		weight = time_list[i].get_weight()
		weight_count.append(int(time_list[i].get_weight()))
		#for i in out:
		#	print(i)
		
	count_mean = np.mean(weight_count)
	count_stdev = np.std(weight_count, ddof = 1)
	weight_standard = count_mean + 2*count_stdev
	print(weight_count)
	print(count_mean)
	print(count_stdev)
	print(weight_standard)

	for i in range(0,len(time_list)):
		if time_list[i].get_weight() > weight_standard:
			tag_account.append(user_id[i])
			#print(user_id[i],weight,end="   ")
			malicious_count+=1
	print('malicious='+str(malicious_count))

	#畫點陣圖
	formarkerin = ['&','.',',','-','+','=','^','<','>','%','$','#','@','!','?','/','*','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	formarker = 0
	all_comment = []
	for i in tag_account:
		insert_node = time_list[temp2_id.get(i)].get_timestamp()
		user_comment = time_list[temp2_id.get(i)].get_comment()
		x = []
		y = []
		
		for j in range(0,len(insert_node)):
			temp = insert_node[j]
			if int(temp[0:4]) == 2020 and int(temp[5:7])>1:
				continue
			if int(temp[0:4]) >= 2019:
				x.append(temp[0:10])
				y.append(temp[11:19])
		
		# 轉為日期格式
		x = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in x]
		y = [datetime.datetime.strptime(d, '%H:%M:%S') for d in y]
		
		# 設置座標軸的格式
		plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
		plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) #座標軸刻度1天
		
		plt.gca().yaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
		plt.gca().yaxis.set_major_locator(mdates.MinuteLocator(interval=60)) #座標軸刻度10分鐘
		plt.xticks(rotation=45)

		plt.plot(x, y,'.',label = temp2_id.get(i)) # 設定樣式
		#plt.legend(loc=0)
		#plt.tight_layout()
		formarker+=1
		
		#list of list 評論	
		all_comment.append(user_comment)

	df = pd.DataFrame(all_comment)
	dft = df.transpose()
	dft.columns = tag_account
	print(dft)
	#dft.to_csv(r'~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/time_analysis/time'+Channelquery+'comment.csv', encoding="utf-8-sig")

	#plt.savefig(str(Channelquery) + "time.png",dpi = 1200 ,bbox_inches='tight') #存檔，第二個參數表示把圖表外多餘的空間刪除


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def String_Compare(tag_account, runtime):

	for i in tag_account:
		string_temp = time_list[temp2_id.get(i)].get_comment()
		ratio_list = []
		for j in range(0,len(string_temp)):
			for k in range(0,len(string_temp)):
				if j != k and string_temp[j]!= None and string_temp[k] != None:
					runtime+=1
					#ratio = similar(string_temp[j],string_temp[k])
					#ratio_list.append(round(ratio,5))
		ratio = np.mean(ratio_list)
		print(ratio)
		if ratio >=0.2:
			sort_ratio.append([i,ratio])
			#final_comment.append(string_temp)
			#final_user.append(i)
			#string_compare_ratio.append(round(ratio,5))
		ratio_list.clear()
	print('runtime'+str(runtime))


	sort_ratio.sort(key=lambda x: x[1],reverse = True)
	for i in range(0,len(sort_ratio)):
		string_temp = time_list[temp2_id.get(sort_ratio[i][0])].get_comment()
		final_comment.append(string_temp)
		final_user.append(sort_ratio[i][0])
		string_compare_ratio.append(round(sort_ratio[i][1],5))

	print(string_compare_ratio)

	final_df = pd.DataFrame(final_comment)
	#print(final_df)
	final_df = final_df.transpose()
	final_df.columns = final_user
	final_df.append(string_compare_ratio)
	print(final_df)
	final_df.to_csv(r'~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/time_analysis/time_malicious_'+Channelquery+'.csv', encoding="utf-8-sig")


if __name__ == "__main__":
    	
	video_id = []#建立獨立的影片ID
	temp1_id = {}#建立影片ID順序的字典
	video_count=0
	user_id = []#建立獨立的使用者ID
	temp2_id = {}#建立使用者對應順序字典
	user_appearance = {}#建立帳號出現頻率字典
	user_count = 0
	comment_count = 0
	last_count = 0
	parentId_videoId = {}#由toplevelcommentId找videoId
	r_userId_to_videoId = []#2維 replyUserId to videoId
	string_compare_ratio = []
	final_user = []
	final_comment = []
	sort_ratio = []
	runtime = 0
	malicious_count = 0
	tag_account = []
	weight_count = []
	time_list = []

	Build_Video_Id_List(video_id, temp1_id, video_count)
	Build_Top_Level_User_Id_List(user_id, temp2_id, user_appearance, user_count, comment_count, last_count)
	Build_Reply_comment_user_id_list(comment_count, user_count)
	Build_Top_Level_CommentIds_VideoId()
	Build_reply_userId_with_videoId_2_dimension_list()
	Build_timestamp_class(malicious_count)
	String_Compare()