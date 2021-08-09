import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules


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
def Build_ToplevelcommentId_List(commentId):
    	
	for i in range(1,length):
		if store_data['snippet.topLevelComment.id'][i] !='nan' and store_data['object_type'][i] == 'data':
			if (store_data['snippet.totalReplyCount'][i])>=1:
				if store_data['snippet.topLevelComment.id'][i] not in commentId:
					commentId.append(str(store_data['snippet.topLevelComment.id'][i]))

	for i in range(1,length2):
		if store_data2['snippet.topLevelComment.id'][i] !='nan' and store_data2['object_type'][i] == 'data':
			if (store_data2['snippet.totalReplyCount'][i])>=1:
				if store_data2['snippet.topLevelComment.id'][i] not in commentId:
					commentId.append(str(store_data2['snippet.topLevelComment.id'][i]))

	for i in range(1,length3):
		if store_data3['snippet.topLevelComment.id'][i] !='nan' and store_data3['object_type'][i] == 'data':
			if (store_data3['snippet.totalReplyCount'][i])>=1:
				if store_data3['snippet.topLevelComment.id'][i] not in commentId:
					commentId.append(str(store_data3['snippet.topLevelComment.id'][i]))

##############################################################################################################
def Build_Video_Id_List(video_id,temp1_id,video_count):
    	
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
def Build_Top_Level_User_Id_List(user_id, temp2_id, user_count, comment_count):
    	
	for i in range(0,length):
		if str(store_data['object_type'][i]) == 'data':
			comment_count+=1
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
		if str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]) in temp2_id.keys():
			continue
		elif str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]) == 'nan':
			continue
		elif str(store_data3['object_type'][i]) == 'data':
			temp2_id.update({store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]:user_count})
			user_count+=1
			user_id.append(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i])

##############################################################################################################
def Build_Reply_Comment_User_Id_List(user_count, comment_count):
    	
	for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
		if str(reply_data['object_type'][i]) == 'data':
			comment_count+=1
		if str(reply_data['snippet.authorChannelId.value'][i]) in temp2_id.keys():
			continue
		elif str(reply_data['object_type'][i]) == 'data':
			temp2_id.update({reply_data['snippet.authorChannelId.value'][i]:user_count})
			user_count+=1
			user_id.append(reply_data['snippet.authorChannelId.value'][i])

	print('User Count = '+str(user_count))
	print('Comment Count ='+str(comment_count))

##############################################################################################################
def Build_Top_Level_CommentIds_VideoId(parentId_videoId):
    
	for i in range(0,len(comment_con_videoId['commentId'])):
		parentId_videoId.update({comment_con_videoId['commentId'][i]:comment_con_videoId['parent.videoId'][i]})

##############################################################################################################
def Build_Reply_UserId_With_VideoId_2_Dimension_List(r_userId_to_videoId, parentId_videoId):
	
	for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
		if str(reply_data['object_type'][i]) == 'data' and str(reply_data['snippet.parentId'][i]) != 'nan':
			#print(reply_data['snippet.authorChannelId.value'][i],parentId_videoId[str(reply_data['snippet.parentId'][i])])
			r_userId_to_videoId.append([str(reply_data['snippet.authorChannelId.value'][i]),parentId_videoId[str(reply_data['snippet.parentId'][i])]])

##############################################################################################################
def Build_Association_Two_dimensional_Array():

	for i in range(0,length):
		if store_data['object_type'][i] == 'data':
			user_key = str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i])
			if user_key != 'nan':
				column = temp2_id[user_key]
				row = temp1_id[store_data['snippet.videoId'][i]]
				#print('('+str(row)+','+str(column)+')',end='')
				association[row][column] = 1
	#print(association)

	for i in range(0,length2):
		if store_data2['object_type'][i] == 'data':
			user_key = str(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i])
			if user_key != 'nan':
				column = temp2_id[user_key]
				row = temp1_id[store_data2['snippet.videoId'][i]]
				#print('('+str(row)+','+str(column)+')',end='')
				association[row][column] = 1

	for i in range(0,length3):
		if store_data3['object_type'][i] == 'data':
			user_key = str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i])
			if user_key != 'nan':
				column = temp2_id[user_key]
				row = temp1_id[store_data3['snippet.videoId'][i]]
				#print('('+str(row)+','+str(column)+')',end='')
				association[row][column] = 1

	for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
		if reply_data['object_type'][i] == 'data':
			user_key = str(reply_data['snippet.authorChannelId.value'][i])
			if user_key != 'nan':
				column = temp2_id[user_key]
				temp = parentId_videoId[reply_data['snippet.parentId'][i]]
				#print(temp)
				row = temp1_id[temp]
				association[row][column] = 1

##############################################################################################################
def Association_Rule_Mining():
    
	df = pd.DataFrame(association,columns=user_id)#建立dataframe
	print('Association Dataframe:')
	print(df)

	print("finish")
	min_support = 0.02
	frequent_itemsets_ap = apriori(df, min_support=min_support, use_colnames=True)#計算support
	print('Apriori Support = '+str(min_support))
	print(frequent_itemsets_ap)

	print("finish")
	frequent_itemsets_fp = fpgrowth(df, min_support=min_support, use_colnames=True)#計算support
	print('Fp Growth Support = '+str(min_support))
	print(frequent_itemsets_fp)

	print("finish")

	rules_ap = association_rules(frequent_itemsets_ap, metric="confidence", min_threshold=0.001)
	rules_fp = association_rules(frequent_itemsets_fp, metric="confidence", min_threshold=0.001)
	print(type(rules_ap))
	print(rules_ap)
	print(type(rules_fp))
	print(rules_fp)
	rules_ap.sort_values(by = ['support'],inplace = True,ascending = False)
	#rules_ap.sort_values(['confidence'])
	rules_ap.to_csv(r''+Channelquery+'rules_ap.csv',index = False)

##############################################################################################################
if __name__ == "__main__":


	commentId = []#build toplevelcommentId list

	video_id = []#建立獨立的影片ID
	temp1_id = {}#建立影片ID順序的字典
	video_count=0
	user_id = []#建立獨立的使用者ID
	temp2_id = {}#建立使用者對應順序字典
	user_count = 0
	comment_count = 0
	parentId_videoId = {}#由toplevelcommentId找videoId
	r_userId_to_videoId = []#2維 replyUserId to videoId
	association = [[0 for i in range(0,user_count)] for j in range(0,video_count)]

	Build_ToplevelcommentId_List(commentId)
	Build_Video_Id_List(video_id, temp1_id, video_count)
	Build_Top_Level_User_Id_List(user_id, temp2_id, user_count, comment_count)
	Build_Reply_Comment_User_Id_List(user_count, comment_count)
	Build_Reply_UserId_With_VideoId_2_Dimension_List(r_userId_to_videoId, parentId_videoId)
