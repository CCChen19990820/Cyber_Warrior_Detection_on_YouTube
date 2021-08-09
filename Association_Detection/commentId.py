import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules


store_data = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_三立柯文哲.csv',encoding='utf-8')
store_data2 = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_三立蔡英文.csv',encoding='utf-8')
store_data3 = pd.read_csv('~/../../mnt/c/Users/Jeff/Desktop/專題資料/Data/Data_三立韓國瑜.csv',encoding='utf-8')
store_data.head()

length = len(store_data['snippet.videoId'])
length2 = len(store_data2['snippet.videoId'])
length3 = len(store_data3['snippet.videoId'])
store_data = pd.concat([store_data,store_data2],join = 'outer')
store_data = pd.concat([store_data,store_data3],join = 'outer')
print(store_data)

##############################################################################################################
def Build_Video_Id_List(video_count):
    
	for i in range(1,length):
		if str(store_data['snippet.videoId'][i]) in temp1_id.keys():
			continue
		elif str(store_data['snippet.videoId'][i]) == 'nan':
			continue
		elif store_data['object_type'][i] == 'data':
			temp1_id.update({store_data['snippet.videoId'][i]:video_count})
			video_count+=1
			video_id.append(store_data['snippet.videoId'][i])
			#print(store_data['snippet.videoId'][i],video_count)
	print(video_count)

##############################################################################################################
def Build_User_Id_List(user_count):

	for i in range(1,length):
		if str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]) in temp2_id.keys():
			continue
		elif str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]) == 'nan':
			continue
		elif str(store_data['object_type'][i]) == 'data':
			temp2_id.update({store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i]:user_count})
			user_count+=1
			user_id.append(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i])
			#print(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i],user_count)
	#print(temp2_id)
	print(user_count)

##############################################################################################################
def Build_Association_two_dimensional_Array():

	for i in range(1,length):
		if store_data['object_type'][i] == 'data':
			user_key = str(store_data['snippet.topLevelComment.snippet.authorChannelId.value'][i])
			if user_key != 'nan':
				column = temp2_id[user_key]
				row = temp1_id[store_data['snippet.videoId'][i]]
				association[row][column] = 1

##############################################################################################################
if __name__ == "__main__":
	
	video_id = []
	temp1_id = {}
	video_count=0
	user_id = []
	temp2_id = {}
	user_count = 0

	Build_Video_Id_List(video_count)

	association = [[0 for i in range(0,user_count)] for j in range(0,video_count)]
	Build_User_Id_List(user_count)
	
	df = pd.DataFrame(association,columns=user_id)#建立dataframe
	print(df)


	frequent_itemsets_ap = apriori(df, min_support=0.01, use_colnames=True)#計算support
	print(type(frequent_itemsets_ap))
	print(frequent_itemsets_ap)
	frequent_itemsets_fp = fpgrowth(df, min_support=0.01, use_colnames=True)#計算support
	print(frequent_itemsets_fp)


	rules_ap = association_rules(frequent_itemsets_ap, metric="confidence", min_threshold=0.001)
	rules_fp = association_rules(frequent_itemsets_fp, metric="confidence", min_threshold=0.001)
	print(rules_ap)
	print(rules_fp)