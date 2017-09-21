import urllib
import json
import requests
import pandas as pd 
from dateutil.parser import parse

page_id = '277631202754911'
token = 'EAACEdEose0cBAHmnicc16yjvhgm8Pe14qnpiIv8DOT15ukph1PYNdsNgV2GPQEviZA4DK9ZCBSVTOgHsCDLXI9VwDU6y1RGEMRZC0ZCOXPk2j9azKXeiTgQZCZA3tGeZAFJ0UNc0DGb1QjYxn9qL55C9U61eulhTI77xaPa4PdlDXmLE6LI2qBbwhLPXDlQiiQjubLrXOoZCxgZDZD'
fb_api = 'https://graph.facebook.com/v2.4/'

information_list = []
g_id = []
g_comments = []
#api_request =  urllib.request.Request(fb_graph_url)

def get_post(id):
	r_url = fb_api+id+'?access_token='+token
	res = requests.get(r_url)

	return res.json()['message']

def get_id():
	
	r_url = fb_api+page_id+'?fields=posts&access_token='+token
	res = requests.get(r_url)
	#get_r = json.loads(u_open(u_request(r_url)).read())
	for i in res.json()['posts']['data']:
		if 'message' in i:
			g_id.append(i['id'])
	#print(g_id)
	#res_comment = fb_api+page_id+"?fields=posts{comments}&access_token="+token

def get_comment(id):
	for p_id in id:

		r_url = fb_api+p_id+'?fields=comments&access_token='+token
		res = requests.get(r_url)

		print("POST : "+ res.json()['id'])
		print("PO文 : "+ get_post(res.json()['id']))

		if 'comments' in res.json():
			for i in res.json()['comments']['data']:
				print("留言者:"+i['from']['name'] + " | 留言內容:"+ i['message']) 
		else:
			print("No comments")
		print("--------------------------------------------------------------------------")


get_id()
get_comment(g_id)