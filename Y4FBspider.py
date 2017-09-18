import requests
import pandas as pd
from bs4 import BeautifulSoup
from dateutil.parser import parse
import time
import csv


#Get API
group_id = '277631202754911'
token = 'EAACEdEose0cBAF0rygdNLAqpsGz7mR2bDspDtpHsbaHELpBBwLKbfaB0uZBmOGJev9tQtwX61bEXhQkW8SPHPVY3ZByZAaOmoNYgTG5GfOlFpUpuojZBke6BXQQ2SaHJGNWUvdfofq2UqFIY6QRj2vf29THMKARHsWoXSK1wNYfEmvzCGLDckgyZCxJ352ZCPZBhc07Do9EKwZDZD'
#Get Requests
res = requests.get('https://graph.facebook.com/v2.4/{}/feed?access_token={}'.format(group_id, token))




local_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
#print(local_time)

post_get_message = []
post_get_create_time =[]
post_get_id = []
post_get_localtime = []

#Get Data
for post in res.json()['data']:
	if post.get('message') == None:
		continue
	post_get_message.append(post.get('message'))
	post_get_create_time.append(parse(post.get('created_time')))
	post_get_id.append(post.get('id'))
	post_get_localtime.append(local_time)

#Data Dict
data_dict = {
	'Message' : post_get_message,
	'created_time' : post_get_create_time,
	'id' : post_get_id,
	'localtime' : post_get_localtime
}

#Frame data use pandas
data_dict_df = pd.DataFrame(data_dict)
#print(data_dict_df)

#Output in .csv
data_dict_df.to_csv('tes.csv', index = False)

#Ouptut in .json
#data_dict_df.to_json("data_get.json")


#Check csv file
with open('tes.csv','r') as file:
	reader = csv.reader(file)
	for row in reader:
		print(row)

