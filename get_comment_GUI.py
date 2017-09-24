import tkinter as tk
import class_get_comment

window = tk.Tk()
window.title('留言捉取')
window.geometry('400x220')
x = class_get_comment.Get_fb_data()

get_posts = []
get_id = x.get_id()

message_ListBox = tk.Listbox(window,width=20,justify='left')
for i in get_id:
	a = x.get_post(i)
	get_posts.append(a)
	message_ListBox.insert('end',a)

message_ListBox.place(x=0,y=20)


def get_inf():
	#var = message_ListBox.get(message_ListBox.curselection())
	var = get_posts_index(message_ListBox.get(message_ListBox.curselection()))
	#var is a index
	id1 = (get_id[var])
	cm = x.get_comment(id1)
	#print(cm)
	post_id_text.delete(0, 'end')
	post_cm_text.delete(0.0, 'end')

	post_id_text.insert('0',get_id[var])
	
	for cmm in cm:
		post_cm_text.insert(1.0,cmm+"\n")
	post_cm_text.insert('end',"----------------------\n")



check_btn = tk.Button(window,text='Get it',width=19,command=get_inf)
check_btn.place(x=0,y=190)

def get_posts_index(var):
	index = message_ListBox.get(0,"end").index(var)
	return index

post_id_text = tk.Entry(window,width=35)
post_id_text.place(x=145,y=0)

post_cm_text = tk.Text(window,width=35, bd=2, font='微軟正黑體')
post_cm_text.place(x=145,y=22)


window.mainloop()