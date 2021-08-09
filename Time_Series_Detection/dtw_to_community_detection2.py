import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import math
import cv2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
import community
import networkx.algorithms.community as nxcom


Channelquery = input("比特王出任務、少康戰情室、關鍵時刻，Choose one to search:")

store_data = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_'+Channelquery+'.csv',encoding='utf-8')
reply_data = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/toplevel_get_reply/'+Channelquery+'.csv',encoding='utf-8')

length = len(store_data['snippet.videoId'])



##############################################################################################################
def Build_ToplevelcommentId_List(commentId):

	for i in range(1,length):
		if store_data['snippet.topLevelComment.id'][i] !='nan' and store_data['object_type'][i] == 'data':
			if (store_data['snippet.totalReplyCount'][i])>=1:
				if store_data['snippet.topLevelComment.id'][i] not in commentId:
					commentId.append(str(store_data['snippet.topLevelComment.id'][i]))

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

##############################################################################################################
def Build_Toplevel_user_Id_List(comment_count, user_count):
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

##############################################################################################################
def Build_Reply_comment_User_Id_List(comment_count, user_count):
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
	#user_count = temp
	print('Comment Count ='+str(comment_count))

##############################################################################################################
def Build_Toplevel_CommentIds_VideoId():
    	
	comment_con_videoId = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/'+Channelquery+'toplevelcommentId.csv',encoding='utf-8')
	parentId_videoId = {}#由toplevelcommentId找videoId
	for i in range(0,len(comment_con_videoId['commentId'])):
		parentId_videoId.update({comment_con_videoId['commentId'][i]:comment_con_videoId['parent.videoId'][i]})
	#print(parentId_videoId)

##############################################################################################################
def Buil_Reply_UserId_With_VideoId_2dimension_List():
	for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
		if str(reply_data['object_type'][i]) == 'data' and str(reply_data['snippet.parentId'][i]) != 'nan':
			#print(reply_data['snippet.authorChannelId.value'][i],parentId_videoId[str(reply_data['snippet.parentId'][i])])
			r_userId_to_videoId.append([str(reply_data['snippet.authorChannelId.value'][i]),parentId_videoId[str(reply_data['snippet.parentId'][i])]])
	#print(r_userId_to_videoId)

##############################################################################################################
class node():
	def __init__(self,name):
		self.name = name
		self.edge = []
		self.neighbour = []
		self.dict = {}
		self.degree = 0
	
	def add(self,who):
		if self.dict.get(who) == None:
			self.neighbour.append(who)	
			self.degree+=1
			self.dict.update({who:1})
		else:
			self.dict[who] = self.dict.get(who) +1
	def get_weight(self,who):
		return self.dict.get(who)
	def get_degree(self):
		return self.degree

##############################################################################################################
def Build_user_and_user_appear_on_same_video():
	node_list = []
	for i in user_id:
		node_list.append(i)
	for i in range(0,len(user_id)):
		node_list[i] = node(user_id[i])

	#for i in range(0,len(node_list)):
	#	print(node_list[i].name)

	now=0
	appear_together = []
	#appear = [[0 for i in range(0,user_count)] for j in range(0,user_count)]
	temp = []#暫存出現在那部video的使用者ID
	for v_id in video_id:#對每部video個別找出出現的使用者
		print(v_id)
		for i in range(0,length):
			if str(store_data['snippet.videoId'][i]) == v_id and str(store_data['object_type'][i]) == 'data' and str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]) != 'nan':
				temp.append(str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]))
		for i in range(0,len(r_userId_to_videoId)):
			if str(r_userId_to_videoId[i][1]) == v_id:
				temp.append(str(r_userId_to_videoId[i][0]))
		#print(temp)
		print('length='+str(len(temp)))
		
		for i in range(0,len(temp)):
			for j in range(i,len(temp)):
				if temp[i] != temp[j]:
					node_list[temp2_id.get(temp[i])].add(temp[j])
					#node_list[temp2_id.get(temp[j])].add(temp[i])
		print("finish")
		print(now)
		temp.clear()
		now+=1

	#print(node_list[0].name)
	#print(node_list[0].neighbour)
	#print(node_list[0].edge)
	with open('appear_'+Channelquery+'.csv','w') as f:
		writer = csv.writer(f)
		for i in range(0,len(node_list)):
			for j in range(i,node_list[i].get_degree()):
				if node_list[i].get_weight(node_list[i].neighbour[j]) >= 50:
					field = [temp2_id.get(node_list[i].name) ,temp2_id.get(node_list[i].neighbour[j]),node_list[i].get_weight(node_list[i].neighbour[j])]
					writer.writerow(field)

##############################################################################################################
def Community_Detection():


	#read csv to construct dataframe
	appear_data_old = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/dtw_normalized/normalized_'+Channelquery+'.csv',encoding='utf-8')
	appear_data_old = appear_data_old.drop(columns = 'Unnamed: 0')
	appear_data_old = appear_data_old.drop(columns = 'Unnamed: 0.1')
	appear_data_old = appear_data_old.sort_values(by='min_distance', ascending=True)
	print(appear_data_old)
	appear_data_list = appear_data_old.values.tolist()
	appear_data_old = pd.DataFrame(appear_data_list,columns=['user1','user2','min_distance','a_count','b_count'])

	print(appear_data_old)


	appear_data = appear_data_old[['user1','user2']]
	print(appear_data)


	#給 edge weight ，建立tuples

	for i in range(0,len(appear_data['user1'])):
		appear_data.loc[i,'user1'] = temp2_id.get(appear_data['user1'][i])
		appear_data.loc[i,'user2'] = temp2_id.get(appear_data['user2'][i])
		#i = math.sqrt(i)
	print(appear_data)
	appear_data = appear_data.head(100)
	print(appear_data)
	total_rows = appear_data.count
	print(total_rows)
	products_list = appear_data.values.tolist()
	appear_data = pd.DataFrame(products_list,columns= ['user1', 'user2'])


	records = appear_data.to_records(index = False)
	print(records)
	user_edge = list(records)#建立edge tuples
	#print(user_edge)
	for i in range(0,len(user_edge)):
		a = records[i]
		#b = {'myweight':appear_data_old['weight'][i]}
		temp = (1 - float(appear_data_old['min_distance'][i]))*10
		b = {'myweight':temp}
		user_edge[i] = (*a,b)


	user_node = []
	signal_user = [0 for x in range(user_count)]

	for i in range(0,len(appear_data)):
		print(appear_data['user1'][i],appear_data['user2'][i])
		signal_user[appear_data['user1'][i]] = 1
		signal_user[appear_data['user2'][i]] = 1
	#print(signal_user)

	for i in range(0,len(signal_user)):
		if signal_user[i] ==1:
			user_node.append(i)

	G = nx.Graph()
	G.add_nodes_from(user_node)
	G.add_edges_from(user_edge)
	print(nx.info(G))

	#nx.draw(G,with_labels=False,node_size=5,node_color='red',linewidth=5)
	#plt.savefig(Channelquery+'.png',dpi = 900)


	#communities = sorted(nxcom.greedy_modularity_communities(G,weight = 'myweight'),key=len,reverse=True)
	communities = sorted(nxcom.asyn_lpa_communities(G,weight = 'myweight'),key=len,reverse=True)
	#communities = sorted(nxcom._naive_greedy_modularity_communities(G),key=len,reverse=True)
	print(len(communities))



	for i in communities:
		for j in i:
			print(user_id[j],end="  ")
			
		print("")

	cluster_df = pd.DataFrame(communities).transpose()
	cluster_df.to_csv(r'~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/dtw/cluster_'+Channelquery+'.csv', encoding="utf-8")

	#find_the_selected_users_comment_store_to_csv
	node_degree = list(G.degree(user_node))
	print(node_degree)

	#找到degree數多的user
	count2=0
	final_user = []
	for i in communities:
		for j in i:
			final_user.append(user_id[j])
		final_user.append('@@@split community@@@')

	###計算留言相似度
	from difflib import SequenceMatcher
	def similar(a, b):
		return SequenceMatcher(None, a, b).ratio()

	string_compare_ratio = []
	#final_user = []
	final_comment = []
	sort_ratio = []
	runtime = 0

	comments = []#最後輸出之list
	comment = []#存every community comment
	empty = []
	count1=0
	Max = 0
	for i in communities:
		for key in i:
			key = user_id[key]
			print(key)
			comment = []
			for i in range(1,length):
				if store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i] == key and store_data['object_type'][i] == 'data' and store_data['snippet.topLevelComment.snippet.textOriginal'][i] != 'nan':
					comment.append(str(store_data['snippet.topLevelComment.snippet.textOriginal'][i]))
					count1+=1
			#for i in range(1,length2):
			#	if store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i] == key and store_data2['object_type'][i] == 'data' and store_data2['snippet.topLevelComment.snippet.textOriginal'][i] != 'nan':
			#		comment.append(str(store_data2['snippet.topLevelComment.snippet.textOriginal'][i]))
			#		count1+=1
			#for i in range(1,length3):
			#	if store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i] == key and store_data3['object_type'][i] == 'data' and store_data3['snippet.topLevelComment.snippet.textOriginal'][i] != 'nan':
			#		comment.append(str(store_data3['snippet.topLevelComment.snippet.textOriginal'][i]))
			#		count1+=1
			for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
				if reply_data['snippet.authorChannelId.value'][i] == key and reply_data['object_type'][i] == 'data' and reply_data['snippet.textOriginal'][i] != 'nan':
					comment.append(str(reply_data['snippet.textOriginal'][i]))
					count1+=1
			comments.append(comment)
			#print(comment)
			ratio_list = []
			for k in range(0,len(comment)):
				for l in range(k,len(comment)):
					if k != l and comment[k]!= None and comment[l] != None:
						runtime+=1
						ratio = similar(comment[k],comment[l])
						#print(ratio,comment[k],comment[l])
						if ratio>=0.2:
							ratio_list.append(round(ratio,5))
			ratio = np.mean(ratio_list)#計算留言相似度平均
			print(ratio)
			temp = [key,ratio]
			for i in comment:
				temp.append(i)
			sort_ratio.append(temp)#list userid+similarity+comment
			ratio_list.clear()
			if len(comment) >= Max:
				Max = len(comment)
		print('runtime'+str(runtime))
		sort_ratio.append(['nan','nan'])#分隔
					
		comments.append(empty)

	#print(comments)
	#for i in comments:
	#	for j in range(len(i),Max):
	#		i.append('nan')
	final_df=pd.DataFrame(sort_ratio)
	final_df = final_df.transpose()
	print(final_df)
	final_df.columns = final_user
	print(final_df)
	final_df.to_csv(r'~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/dtw/comment_similarity_'+Channelquery+'.csv', encoding="utf-8-sig")

##############################################################################################################
if __name__ == "__main__":
	commentId = []
	video_id = []#建立獨立的影片ID
	temp1_id = {}#建立影片ID順序的字典
	video_count=0
	user_id = []#建立獨立的使用者ID
	temp2_id = {}#建立使用者對應順序字典
	user_count = 0
	comment_count = 0
	r_userId_to_videoId = []#2維 replyUserId to videoId
	parentId_videoId = {}#由toplevelcommentId找videoId

	Build_ToplevelcommentId_List(commentId)
	Build_Video_Id_List(temp1_id, video_count, video_id)
	Build_Toplevel_user_Id_List(comment_count, user_count)
	Build_Reply_comment_User_Id_List(comment_count, user_count)
	Build_Toplevel_CommentIds_VideoId()
	Buil_Reply_UserId_With_VideoId_2dimension_List()
	Build_user_and_user_appear_on_same_video()
	Community_Detection()
