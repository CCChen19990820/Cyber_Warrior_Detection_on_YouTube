import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import csv
import math
import datetime
import time
import matplotlib.dates as mdates
#from datetime import datetime


Channelquery = input("中天、三立、東森，Choose one to search:")

store_data = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_'+Channelquery+'柯文哲.csv',encoding='utf-8')
store_data2 = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_'+Channelquery+'蔡英文.csv',encoding='utf-8')
store_data3 = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_'+Channelquery+'韓國瑜.csv',encoding='utf-8')
reply_data = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/toplevel_get_reply/'+Channelquery+'.csv',encoding='utf-8')

length = len(store_data['snippet.videoId'])
length2 = len(store_data2['snippet.videoId'])
length3 = len(store_data3['snippet.videoId'])

##############################################################################################################
def Build_Video_Id_List(temp1_id, video_count, video_id):

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
def Build_Top_Level_User_Id_List(comment_count, user_count, user_appearance, temp2_id, user_id):

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
	#print(user_count)

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
def Build_Reply_comment_User_Id_List(comment_count, user_count, user_appearance, temp2_id, user_id):


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

	comment_con_videoId = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/'+Channelquery+'toplevelcommentId.csv',encoding='utf-8')
	for i in range(0,len(comment_con_videoId['commentId'])):
		parentId_videoId.update({comment_con_videoId['commentId'][i]:comment_con_videoId['parent.videoId'][i]})

##############################################################################################################
def Build_Reply_UserId_With_VideoId_2_Dimension_List():

	for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
		if str(reply_data['object_type'][i]) == 'data' and str(reply_data['snippet.parentId'][i]) != 'nan':
			r_userId_to_videoId.append([str(reply_data['snippet.authorChannelId.value'][i]),parentId_videoId[str(reply_data['snippet.parentId'][i])]])

##############################################################################################################
class Time():
	def __init__(self,name):
		self.name = name
		self.timestamp = []
		self.comment = []
		self.timeseries = np.zeros(540000)
		self.dtw_list = []
		self.dict = {}
		self.count = 0
		self.weight = 0
		self.com_count = 0
	def free_timeseries(self):
		del self.timeseries
		
	def add_dtw(self,index):
		self.dtw_list = index
	
	def get_name(self):
		return self.name
	
	def get_dtw(self):
		return self.dtw_list

	def get_dtw_len(self):
		return len(self.dtw_list)
	
	def add_timeseries(self,who):
		self.timeseries[who] = 1
		self.count+=1
	
	def add(self,timepoint):
		self.timestamp.append(timepoint)	
	
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
	
	def get_time_series(self):
		return self.timeseries

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
def Build_timestamp_class():
	start_time = '2019-01-01T00:00:00Z'
	end_time = '2020-01-10T22:00:00Z'
	initial_minute = int(time.mktime(datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ").timetuple())/60)
	final_minute = int(time.mktime(datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ").timetuple())/60)

	for i in user_id:
		time_list.append(i)
	for i in range(0,len(user_id)):
		time_list[i] = Time(user_id[i])

	for i in range(0,length):
		if str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]) != 'nan' and str(store_data['object_type'][i]) == 'data':
			time_list[temp2_id.get(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add(store_data['snippet.topLevelComment.snippet.publishedAt'][i])
			time_list[temp2_id.get(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add_comment(store_data['snippet.topLevelComment.snippet.textOriginal'][i])
			#將留言時間戳記新增在time series上
			timestamp = store_data['snippet.topLevelComment.snippet.publishedAt'][i]
			timestamp = timestamp[0:19]
			minutes = int(time.mktime(datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S").timetuple())/60)
			if minutes >= initial_minute and minutes <= final_minute :
				time_list[temp2_id.get(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add_timeseries(minutes-initial_minute)

	for i in range(0,length2):
		if str(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]) != 'nan' and str(store_data2['object_type'][i]) == 'data':
			time_list[temp2_id.get(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add(store_data2['snippet.topLevelComment.snippet.publishedAt'][i])
			time_list[temp2_id.get(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add_comment(store_data2['snippet.topLevelComment.snippet.textOriginal'][i])
			#將留言時間戳記新增在time series上
			timestamp = store_data2['snippet.topLevelComment.snippet.publishedAt'][i]
			timestamp = timestamp[0:19]
			minutes = int(time.mktime(datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S").timetuple())/60)
			if minutes >= initial_minute and minutes <= final_minute :
				time_list[temp2_id.get(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add_timeseries(minutes-initial_minute)


	for i in range(0,length3):
		if str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]) != 'nan' and str(store_data3['object_type'][i]) == 'data':
			time_list[temp2_id.get(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add(store_data3['snippet.topLevelComment.snippet.publishedAt'][i])
			time_list[temp2_id.get(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add_comment(store_data3['snippet.topLevelComment.snippet.textOriginal'][i])
			#將留言時間戳記新增在time series上
			timestamp = store_data3['snippet.topLevelComment.snippet.publishedAt'][i]
			timestamp = timestamp[0:19]
			minutes = int(time.mktime(datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S").timetuple())/60)
			if minutes >= initial_minute and minutes <= final_minute :
				time_list[temp2_id.get(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i])].add_timeseries(minutes-initial_minute)


	for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
		if str(reply_data['snippet.authorChannelId.value'][i]) != 'nan' and reply_data['object_type'][i] =='data':
			time_list[temp2_id.get(reply_data['snippet.authorChannelId.value'][i])].add(reply_data['snippet.publishedAt'][i])
			time_list[temp2_id.get(reply_data['snippet.authorChannelId.value'][i])].add_comment(reply_data['snippet.textOriginal'][i])
			#將留言時間戳記新增在time series上
			timestamp = reply_data['snippet.publishedAt'][i]
			timestamp = timestamp[0:19]
			minutes = int(time.mktime(datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S").timetuple())/60)
			if minutes >= initial_minute and minutes <= final_minute :
				time_list[temp2_id.get(reply_data['snippet.authorChannelId.value'][i])].add_timeseries(minutes-initial_minute)

##############################################################################################################
def Dynamic_Time_Warping(a,b):

	#print(a,b)
	matrix = np.zeros((2,len(b)))
	for i in range(0,2):
		for j in range(0,len(b)):
			matrix[i][j] = float('Inf')
	
	loc_a = a.copy()
	loc_b = b.copy()
	loc_a[0] = abs(loc_a[0])
	loc_b[0] = abs(loc_b[0])
	for i in range(1,len(a)):
		loc_a[i] = abs(loc_a[i]) + abs(loc_a[i-1])
	for i in range(1,len(b)):
		loc_b[i] = abs(loc_b[i]) + abs(loc_b[i-1])
	
	limit = 5 #最多對到10分鐘以內之stamp
	
	#初始化matrix[0][0]值
	if (a[0]>0 and b[0]<0) or (a[0]<0 and b[0]>0):
		matrix[0][0] = max(abs(a[0]), abs(b[0]))
	elif a[0]<0 and b[0]<0:
		matrix[0][0] = max(abs(a[0] - b[0]) - limit , 0)
	else:
		matrix[0][0] = 0
	
	#初始化matrix第一列
	for i in range(1,len(b)):
		if (a[0]>0 and b[i]<0) or (a[0]<0 and b[i]>0):
			matrix[0][i] = matrix[0][i-1] + max(abs(a[0]), abs(b[i]))
		elif a[0]<0 and b[i]<0:
			matrix[0][i] = matrix[0][i-1] + max(abs(loc_a[0] - loc_b[i]) - limit, 0)
		elif abs(loc_a[0] - loc_b[i]) >limit and a[0]>0 and b[i]>0:
			matrix[0][i] = matrix[0][i-1] + 1
		else:
			matrix[0][i] = matrix[0][i-1]
	
	#第2-n列
	for i in range(1,len(a)):
		for j in range(0,len(b)):
			if (a[i]>0 and b[j]<0) or (a[i]<0 and b[j]>0):
				cost = max(abs(a[i]), abs(b[j]))
			elif a[i]<0 and b[j]<0:
				cost = max(abs(loc_a[i] - loc_b[j]) - limit, 0)
			elif abs(loc_a[i] - loc_b[j]) >limit and a[i]>0 and b[j]>0:
				cost = 1
			else:
				cost = 0

			#print(i,j,a[i],b[j],cost,end="_")
			if j == 0:
				matrix[1][j] = matrix[0][j] + cost
			else:
				matrix[1][j] = min(matrix[0][j],matrix[1][j-1],matrix[0][j-1]) + cost
		matrix[0] = matrix[1]
		#for j in range(0,len(b)):
			#matrix[1][j] = float('Inf')
		#	print(int(matrix[0][j]),end=",")
		#print('')
	return matrix[0][len(b)-1]
	
##############################################################################################################
def f5(a,b):
	
	#print(a,b)
	matrix = np.zeros((2,len(b)))
	for i in range(0,2):
		for j in range(0,len(b)):
			matrix[i][j] = float('Inf')
	
	loc_a = a.copy()
	loc_b = b.copy()
	loc_a[0] = abs(loc_a[0])
	loc_b[0] = abs(loc_b[0])
	for i in range(1,len(a)):
		loc_a[i] = abs(loc_a[i]) + abs(loc_a[i-1])
	for i in range(1,len(b)):
		loc_b[i] = abs(loc_b[i]) + abs(loc_b[i-1])
	#print(loc_a)
	#print(loc_b)
	#print(a,b)
	
	limit = 2 #最多對到10分鐘以內之stamp
	
	#初始化matrix[0][0]值
	if (a[0]>0 and b[0]<0) or (a[0]<0 and b[0]>0):
		matrix[0][0] = abs(b[0])
	elif a[0]<0 and b[0]<0:
		matrix[0][0] = max(abs(a[0] - b[0]) - limit , 0)
	else:
		matrix[0][0] = 0
	
	#計算matrix第一列
	for i in range(1,len(b)):
		if (a[0]>0 and b[i]<0) or (a[0]<0 and b[i]>0):#一正一負
			matrix[0][i] = matrix[0][i-1] + abs(b[i])
		
		elif a[0]<0 and b[i]<0: #兩個都為負
			if loc_a[0] > loc_b[i]:
				matrix[0][i] = matrix[0][i-1]
			elif loc_a[0] <= loc_b[i]:
				b_head = loc_b[i-1] + 1
				head = b_head - loc_a[0]
				if head <0:
					matrix[0][i] = matrix[0][i-1] + max(abs(b[i]) - limit, 0)
				elif head >=0:
					matrix[0][i] = matrix[0][i-1] + max(abs(b[i]) - ((loc_a[0]+limit)-b_head+1), 0)	
				#matrix[0][i] = matrix[0][i-1] + max(abs(loc_b[i] - loc_a[0]) - limit, 0)
		
		elif abs(loc_b[i] - loc_a[0]) >limit and a[0]>0 and b[i]>0:#兩正且不可配對
			matrix[0][i] = matrix[0][i-1] + 1
		else:#兩正可配對
			matrix[0][i] = matrix[0][i-1]
	
	#計算matrix第2 ~ n列
	for i in range(1,len(a)):
		for j in range(0,len(b)):
			#print(a[i],b[j],end='=')
			
			if (a[i]>0 and b[j]<0) or (a[i]<0 and b[j]>0):#一正一負
				if loc_a[i] > loc_b[j] and a[i]>0 and b[j]<0:
					cost = 1
					#print("1",end="/")
				elif loc_a[i] > loc_b[j] and a[i]<0 and b[j]>0:
					if j-1 >= 0:
						cost = min(loc_a[i] - loc_b[j], abs(a[i]))
					else:
						cost = abs(a[i])
					#print("2",end="/")
				elif loc_b[j] > loc_a[i] and a[i]<0 and b[j]>0:
					cost = 1
					#print("3",end="/")
				elif loc_b[j] > loc_a[i] and a[i]>0 and b[j]<0:
					if j-1 >= 0:
						cost = min(loc_b[j] - loc_a[i], abs(b[j]))
					else:
						cost = abs(b[j])
					#print("4",end="/")
				elif loc_a[i] == loc_b[j]:
					cost = 1
			
			elif a[i]<0 and b[j]<0: #兩個都為負
				if loc_a[i] > loc_b[j]:
					if i-1 >= 0:
						a_head = loc_a[i-1] + 1
						head = a_head - loc_b[j]
						if head <0:
							cost = max(loc_a[i] - loc_b[j] - limit, 0)
							#print("5",end="/")
						if head > limit:
							cost = abs(a[i])
						else:
							cost = max(abs(a[i]) - ((loc_b[i]+limit)-a_head+1), 0)	
						#print("6",end="/")
					else:
						cost = max(loc_a[i] - loc_b[j]-limit, 0)
						#print("7",end="/")
				
				elif loc_a[i] <= loc_b[j]:
					if j-1 >=0:
						b_head = loc_b[j-1] + 1
						head = b_head - loc_a[i]
						if head <0:
							cost = max(loc_b[j] - loc_a[i] - limit, 0)
							#print("8",end="/")
						if head >limit:
							cost = abs(b[j])
						else:
							cost = max(abs(b[j]) - ((loc_a[i]+limit)-b_head+1), 0)	
						#print(cost,"9",end="/")
					else:
						cost = max(loc_b[j] - loc_a[i]-limit, 0)
						#print("10",end="/")
		
			elif abs(loc_b[j] - loc_a[i]) >limit and a[i]>0 and b[j]>0:#兩正且不可配對
				cost = 1
				#print("11",end="/")
			else:#兩正可配對
				cost = 0
				#print("12",end="/")
			
			if j == 0:
				matrix[1][j] = matrix[0][j] + cost
			else:
				matrix[1][j] = min(matrix[0][j],matrix[1][j-1],matrix[0][j-1]) + cost
		
		matrix[0] = matrix[1]

	return matrix[0][len(b)-1]
				

##############################################################################################################
def DTW_similarity(time_list):
	

	comment_average = 0#計算平均留言數
	temp = []
	for i in time_list:
		temp.append(i.get_count())
	print('total = '+str(comment_average))
	count_mean = np.mean(temp)
	count_stdev = np.std(temp, ddof = 1)
	comment_average = count_mean + 2*count_stdev
	print('average = '+str(comment_average))

	#去除低於平均留言數的user
	user_list = []
	for i in time_list:
		if i.get_count() >= comment_average :
			user_list.append(i)
	print('finish find')

	del time_list

	countuser = 0
	totaluser = len(user_list)


	for i in user_list:
		temp = i.get_time_series()
		zero_count = 0
		countuser+=1
		temp2 = []
		for j in range(0, len(temp)):
			if int(temp[j]) != 0:
				if zero_count != 0:
					temp2.append(zero_count*-1)
				temp2.append(temp[j])
				zero_count = 0
			else:
				zero_count += 1
		i.free_timeseries()
		#print('yes')
		i.add_dtw(temp2)
		#print(i.get_dtw_len())
		#print(i.get_dtw())


	#儲存最後兩兩帳號的相似度
	similar_ratio = []
	counter = 0
	for i in range(0,len(user_list)):
		print("")
		print(counter,len(user_list))
		counter+=1
		for j in range(i,len(user_list)):
			if i != j:
				rows = user_list[i].get_dtw_len()
				columns = user_list[j].get_dtw_len()
				if rows >= columns:
					first = user_list[j].get_dtw()
					seconds = user_list[i].get_dtw()
				else:
					first = user_list[i].get_dtw()
					seconds = user_list[j].get_dtw()

				a_count = user_list[i].get_count()
				b_count = user_list[j].get_count()
				#計算相似度

				min_distance = Dynamic_Time_Warping(first,seconds)

				temp = [user_list[i].get_name(),user_list[j].get_name(),int(min_distance),a_count,b_count]

				similar_ratio.append(temp)


	df = pd.DataFrame(similar_ratio)
	df.columns = ['user1','user2','min_distance','a_count','b_count']
	print(df)
	df.to_csv(r'~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/dtw/dtw_'+Channelquery+'.csv', encoding="utf-8")

##############################################################################################################
def Appearence_Normalized():

	dtw_df = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/dtw/dtw_'+ Channelquery +'.csv',encoding='utf-8')
	print(dtw_df)


	max_length = 0
	for i in range(0,len(dtw_df['min_distance'])):
		if dtw_df['min_distance'][i] > max_length:
			max_length = dtw_df['min_distance'][i]
	print(max_length)
	for i in range(0,len(dtw_df['min_distance'])):
		new = 1 - ((max_length - dtw_df['min_distance'][i]) / max_length)
		dtw_df.loc[i,'min_distance'] = new
		#print(i,len(dtw_df['min_distance']))

	dtw_df.to_csv(r'~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/dtw_normalized/normalized_'+Channelquery+'.csv', encoding="utf-8")


##############################################################################################################
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
	r_userId_to_videoId = []#2維 replyUserId to videoId
	parentId_videoId = {}#由toplevelcommentId找videoId
	time_list = []

	Build_Video_Id_List(temp1_id, video_count, video_id)
	Build_Top_Level_User_Id_List(comment_count, user_count, user_appearance, temp2_id, user_id)
	Build_Top_Level_CommentIds_VideoId()
	Build_Reply_UserId_With_VideoId_2_Dimension_List()
	Build_timestamp_class()
	DTW_similarity()
	Appearence_Normalized()
	