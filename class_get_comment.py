#Define main function

import urllib
import json
import requests
import pandas as pd 
from dateutil.parser import parse

#global Var
page_id = '277631202754911'
token = 'EAACEdEose0cBAIzsYZBZAShVMNiZAUhk2GZBqQ9BS2SlavWzJCW2KviVweVjO6oR4nqfdjZBrgyXJcNL7Y2r19mQCgEyTMCIqhRUXB9pZAsPS6ZCzl8z5l6uqofo8BzWbLFqXqW7krZA1WUDJdtEfNQRZA0TgOVZCBNQMc9PKluakgZCADIaEIKgPvnTuCcE3MvPvZBPtxSr9PVZCsgZDZD'
fb_api = 'https://graph.facebook.com/v2.4/'

#global get list
information_list = []
g_id = []
g_comments = []

#fb cm data
All_posts = []
All_comments = []
post_usr = []
comments_usr = []
post_time = []
comments_time = []


class Get_fb_data:
	"""docstring for get_fb_data"""
	def __init__(self):
		pass

	def get_id(self):
		r_url = fb_api+page_id+'?fields=posts&access_token='+token
		res = requests.get(r_url)
		for i in res.json()['posts']['data']:
			if 'message' in i:
				g_id.append(i['id'])
		return g_id

	def get_post(self,id):
		r_url = fb_api+id+'?access_token='+token
		res = requests.get(r_url)
		All_posts.append(res.json()['message'])
		return res.json()['message']

	def get_comment(self,id):
		All_comments.clear()
		comments_usr.clear()
		comments_time.clear()
		
		r_url = fb_api+id+'?fields=comments&access_token='+token
		res = requests.get(r_url)
		#return r_url

		#All_posts.append(self.get_post(res.json()['id']))
		if 'comments' in res.json():
			for i in res.json()['comments']['data']:
				All_comments.append(i['message'])
				comments_usr.append(i['from']['name'])
		else:
			All_comments.append("沒有留言")
		return All_comments



"""#Test
if __name__ == '__main__':
	e = Get_fb_data()
	e.get_post(g_id[2])
	print(g_id)
	#print(All_posts)"""