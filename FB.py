import facebook

class getInfo:
	token = 'EAACEdEose0cBADZAP4yRIvVlOdQSZCnlxEnMhX0nrtZBLUuuAxNOZC1rcqQvNO9vykcAtcFZAcMfZB5fFKVlZBPlv3wHYpYZBD1lgU1GAu9VqXVcqXzwbVbHXdEJlFdPeQUrsDG5XAuPaEIaJZCoWAYYv0vn5QBDkxODPiwupDGKlJ7LGZBWfqCisldy9KtLQ8oGiL3YCwFZCntZCAZDZD'
	page_id = '277631202754911'    #粉專 ID

	graph = facebook.GraphAPI(access_token = token)
	me_info = graph.get_object('allenabcde')

	#/--------------------------------取得所有貼文--------------------------------/#
	def get_all_posts(self, action='posts'):
		all_posts = []
		posts = self.graph.get_connections(id = self.page_id, connection_name = action)
		for each in posts['data']:
			if 'message' in each:
				all_posts.append(each['message'])
				#print(all_posts)
		return all_posts
	#/--------------------------------取得所有貼文ID--------------------------------/#
	def get_all_posts_id(self, action='posts'):
		all_posts_id = []
		posts = self.graph.get_connections(id = self.page_id, connection_name = action)
		for each in posts['data']:
			if 'message' in each:
				all_posts_id.append(each['id'])
		return all_posts_id

	#/--------------------------------透過ID取得該筆留POST內容--------------------------------/#
	def get_own_posts_message(self,g_id):
		post = self.graph.get_object(id=g_id, fields='message')
		return post['message']

	#/--------------------------------透過ID取得該筆POST所有留言--------------------------------/#
	def get_comments(self, post_id, action='comments'):
		all_comments = []
		cm = self.graph.get_object(id=post_id,fields='comments')
		if 'comments' in cm:
			for each in cm['comments']['data']:
				if 'message' in each:
					all_comments.append(each['message'])
		else:
			all_comments.append("No comments!!!!")
		return all_comments

	#/--------------------------------回傳UserName--------------------------------/#
	def get_user(self, post_id):
		cm_from = []
		cm = self.graph.get_object(id=post_id,fields='comments')
		if 'comments' in cm:
			for each in cm['comments']['data']:
					cm_from.append(each['from']['name'])
		else:
			cm_from.append("No one")
		return cm_from
	#/--------------------------------發文--------------------------------/#
	def post_to_page(self,p_str):
		self.graph.put_object(self.page_id, "feed", message=p_str)
