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

Channelquery = input("中天、三立、東森，Choose one to search:")


store_data = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_'+Channelquery+'柯文哲.csv',encoding='utf-8')
store_data2 = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_'+Channelquery+'蔡英文.csv',encoding='utf-8')
store_data3 = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_'+Channelquery+'韓國瑜.csv',encoding='utf-8')
reply_data = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/toplevel_get_reply/'+Channelquery+'.csv',encoding='utf-8')

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
	'''
	with open('三立commentId.csv','w',encoding='utf-8') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['commentId'])
		for i in commentId:
			writer.writerow([i])
	'''

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
			#print(store_data['snippet.videoId'][i],video_count)
	#print(video_count)

	for i in range(0,length2):
		if str(store_data2['snippet.videoId'][i]) in temp1_id.keys():
			continue
		elif str(store_data2['snippet.videoId'][i]) == 'nan':
			continue
		elif store_data2['object_type'][i] == 'data':
			temp1_id.update({store_data2['snippet.videoId'][i]:video_count})
			video_count+=1
			video_id.append(store_data2['snippet.videoId'][i])
			#print(store_data['snippet.videoId'][i],video_count)
	#print(video_count)

	for i in range(0,length3):
		if str(store_data3['snippet.videoId'][i]) in temp1_id.keys():
			continue
		elif str(store_data3['snippet.videoId'][i]) == 'nan':
			continue
		elif store_data3['object_type'][i] == 'data':
			temp1_id.update({store_data3['snippet.videoId'][i]:video_count})
			video_count+=1
			video_id.append(store_data3['snippet.videoId'][i])
			#print(store_data['snippet.videoId'][i],video_count)
	print('Video Count = '+str(video_count))

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
			#print(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i],user_count)
	#print(user_count)

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
	#print(user_count)

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
	#print(user_count)


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
		for i in range(0,length2):
			if str(store_data2['snippet.videoId'][i]) == v_id and str(store_data2['object_type'][i]) == 'data' and str(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]) != 'nan':
				temp.append(str(store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i]))
		for i in range(0,length3):
			if str(store_data3['snippet.videoId'][i]) == v_id and str(store_data3['object_type'][i]) == 'data' and str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]) != 'nan':
				temp.append(str(store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i]))
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
	#appear_data = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/appear_'+Channelquery+'.csv',encoding='utf-8')
	appear_data_old = pd.read_csv('appear_'+Channelquery+'.csv',encoding='utf-8')
	appear_data_old.columns = ['from','to','weight']
	appear_data = appear_data_old[['from','to']]
	total_rows = appear_data_old.count
	print(total_rows)


	#給 edge weight ，建立tuples
	for i in appear_data_old['weight']:
		i = i/2
		#i = math.sqrt(i)
	records = appear_data.to_records(index = False)
	print(records)
	user_edge = list(records)#建立edge tuples
	#print(user_edge)
	for i in range(0,len(user_edge)):
		a = records[i]
		b = {'myweight':appear_data_old['weight'][i]}
		user_edge[i] = (*a,b)


	user_node = []
	signal_user = [0 for x in range(user_count)]

	for i in range(0,len(appear_data)):
		signal_user[appear_data['from'][i]] = 1
		signal_user[appear_data['to'][i]] = 1
	#print(signal_user)

	for i in range(0,len(signal_user)):
		if signal_user[i] ==1:
			user_node.append(i)

	G = nx.Graph()
	G.add_nodes_from(user_node)
	G.add_edges_from(user_edge)
	print(nx.info(G))


	#communities = sorted(nxcom.greedy_modularity_communities(G),key=len,reverse=True)
	communities = sorted(nxcom.asyn_lpa_communities(G,weight = 'myweight'),key=len,reverse=True)
	#communities = sorted(nxcom._naive_greedy_modularity_communities(G),key=len,reverse=True)
	print(len(communities))

	for i in communities:
		for j in i:
			print(user_id[j],end="  ")
		print("")
	
	#Draw_community_network_graph
	set_node_community(G, communities)
	set_edge_community(G)
	node_color = [get_color(G.nodes[v]['community']) for v in G]
	# Set community color for edges between members of the same community (internal) and intra-community edges (external)
	external = [(v, w) for v, w in G.edges if G.edges[v, w]['community'] == 0]
	internal = [(v, w) for v, w in G.edges if G.edges[v, w]['community'] > 0]
	internal_color = ['black' for e in internal]



	#draw graph
	karate_pos = nx.spring_layout(G,weight='myweight',scale=5,k=0.5,iterations=80)

	# Draw external edges
	nx.draw_networkx(G,with_labels=False,pos=karate_pos,node_size=4,edgelist=external,edge_color="silver",linewidths=0.08)
	#nx.draw_networkx(G,with_labels=False,pos=karate_pos,node_size=4,edge_color="silver",linewidths=0.08)

	# Draw nodes and internal edges
	nx.draw_networkx(G,with_labels=False,pos=karate_pos,node_size=4,node_color=node_color,edgelist=internal,edge_color=internal_color,linewidths=0.08)
	#nx.draw_networkx(G,with_labels=False,pos=karate_pos,node_size=4,linewidths=0.08)

	plt.savefig(Channelquery+'.png',dpi = 600)

	#Find_The_Selected_User_comment_store_to_csv()
	Find_The_Selected_User_comment_store_to_csv(G, user_node)




##############################################################################################################
def set_node_community(G, communities):
    for c, v_c in enumerate(communities):
    	for v in v_c:
			# Add 1 to save 0 for external edges
            G.nodes[v]['community'] = c + 1

##############################################################################################################
def set_edge_community(G):
    for v, w, in G.edges:
        if G.nodes[v]['community'] == G.nodes[w]['community']:
        	# Internal edge, mark with community
            G.edges[v, w]['community'] = G.nodes[v]['community']
        else:
            # External edge, mark as 0
            G.edges[v, w]['community'] = 0

##############################################################################################################
def get_color(i, r_off=1, g_off=1, b_off=1):
    r0, g0, b0 = 0, 0, 0
    n = 16
    low, high = 0.1, 0.9
    span = high - low
    r = low + span * (((i + r_off) * 3) % n) / (n - 1)
    g = low + span * (((i + g_off) * 5) % n) / (n - 1)
    b = low + span * (((i + b_off) * 7) % n) / (n - 1)
    return (r, g, b)

##############################################################################################################
def Find_The_Selected_User_comment_store_to_csv(G, user_node):

	node_degree = list(G.degree(user_node))
	print(node_degree)

	#找到degree數多的user
	count2=0
	final_user = []
	for i in node_degree:
		if i[1]>5:
			#print(i[0],end="")
			for key, value in temp2_id.items():
				if i[0] == value:
					final_user.append(key)
					print(key)
					count2+=1

	comments = []
	comment = []
	count1=0
	Max = 0
	for key in final_user:
		comment = []
		for i in range(1,length):
			if store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i] == key and store_data['object_type'][i] == 'data' and store_data['snippet.topLevelComment.snippet.textOriginal'][i] != 'nan':
				comment.append(str(store_data['snippet.topLevelComment.snippet.textOriginal'][i]))
				count1+=1
		for i in range(1,length2):
			if store_data2['snippet.topLevelComment.snippet.authorChannelId.value'][i] == key and store_data2['object_type'][i] == 'data' and store_data2['snippet.topLevelComment.snippet.textOriginal'][i] != 'nan':
				comment.append(str(store_data2['snippet.topLevelComment.snippet.textOriginal'][i]))
				count1+=1
		for i in range(1,length3):
			if store_data3['snippet.topLevelComment.snippet.authorChannelId.value'][i] == key and store_data3['object_type'][i] == 'data' and store_data3['snippet.topLevelComment.snippet.textOriginal'][i] != 'nan':
				comment.append(str(store_data3['snippet.topLevelComment.snippet.textOriginal'][i]))
				count1+=1
		for i in range(0,len(reply_data['snippet.authorChannelId.value'])):
			if reply_data['snippet.authorChannelId.value'][i] == key and reply_data['object_type'][i] == 'data' and reply_data['snippet.textOriginal'][i] != 'nan':
				comment.append(str(reply_data['snippet.textOriginal'][i]))
				count1+=1
		comments.append(comment)
		if len(comment) >= Max:
			Max = len(comment)
	#print(comments)
	for i in comments:
		for j in range(len(i),Max):
			i.append('nan')
	com_dataframe = pd.DataFrame(comments).transpose()
	com_dataframe.columns = final_user
	print(count1)
	print(com_dataframe)
	com_dataframe.to_csv(r'~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/finalcomment/'+Channelquery+'comment.csv', encoding="utf-8-sig")
					

	for i in final_user:
		name = input('============================================================================================\n輸入:')
		print('============================================================================================')
		print(i)
		for j in com_dataframe[i]:
			if j != 'nan':
				print(j)
				print('--------------------------------------------------')

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
	parentId_videoId = {}#由toplevelcommentId找videoId
	r_userId_to_videoId = []#2維 replyUserId to videoId

	Build_ToplevelcommentId_List(commentId)
	Build_Video_Id_List(temp1_id, video_count, video_id)
	Build_Toplevel_user_Id_List(comment_count, user_count)
	Build_Reply_comment_User_Id_List(comment_count, user_count)
	Build_Toplevel_CommentIds_VideoId()
	Buil_Reply_UserId_With_VideoId_2dimension_List()
	Build_user_and_user_appear_on_same_video()
	Community_Detection()