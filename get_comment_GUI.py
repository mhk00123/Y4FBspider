import tkinter as tk
import class_get_comment

window = tk.Tk()
window.title('留言捉取')
window.geometry('400x300')
x = class_get_comment.g_inf()

a_p_id = []

message_ListBox = tk.Listbox(window,width=20,justify='left')

for i in x.get_all_posts_id():
	a_p_id.append(i)
	a = x.get_own_posts_message(i)
	message_ListBox.insert('end',a)

message_ListBox.place(x=0,y=20)

def get_posts_index(var):
	index = message_ListBox.get(0,"end").index(var)
	return index

def get_inf():
	var = get_posts_index(message_ListBox.get(message_ListBox.curselection()))
	id1 = a_p_id[var]
	cm1 = x.get_comments(id1)
	p_from = x.get_user(id1)
	
	post_id_text.delete(0, 'end')
	post_cm_text.delete(0.0, 'end')

	post_id_text.insert('0',id1)

	if cm1[0] == 'No comments!!!!':
		post_cm_text.insert(1.0,'No comments!!!!')
	else:
		i = 0
		for cmm in cm1:
			post_cm_text.insert(1.0,'發文者:'+p_from[i]+'\n'+'留言:  '+cmm+'\n'+'-------------------------------\n')


check_btn = tk.Button(window,text='Get it',width=19,command=get_inf)
check_btn.place(x=0,y=190)


post_id_text = tk.Entry(window,width=45)
post_id_text.place(x=145,y=0)

post_cm_text = tk.Text(window,width=35, bd=2, font='微軟正黑體')
post_cm_text.place(x=145,y=22)


window.mainloop()