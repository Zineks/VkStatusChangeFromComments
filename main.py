import vk_api

access_token = ""
vk_session = vk_api.VkApi(token = access_token)
vk = vk_session.get_api()

user_id = 
post_id = 

while True:
	status = vk.status.get(user_id = user_id)['text']
	comm = vk.wall.getComments(owner_id=user_id, post_id=post_id, count=1, sort='desc', offset=0)
	com_text = comm['items'][0]['text']
	if com_text == status:
		pass
	else:
		vk.status.set(text = com_text)
