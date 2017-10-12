# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 01:50:57 2017

@author: Mayday
"""

#===================================GUI package===============================#
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
style.use('ggplot')

from DBService import DBService              #Database class
from TableService import TableService        #Table service class 

#==================================Function===================================#
def getSite():
    global all_site_lst
    x = db.readSiteData()
    for item in x:
        all_site_lst.append(item[3])

def lstClick(evt):
    global txtSite,txtPM25,txtPM10,txtTemp,txtHumi,canvas
    
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)                    #user selected item
    txtSite.set(value)
    
    t = table.getAllTableName()
    x = db.readAirDataByNote(t[-1],value)   #get air data by selected item
    txtColor(x[1],x[2],x[3],x[4])
    txtPM25.set(x[1])
    txtPM10.set(x[2])
    txtTemp.set("%.2f" % x[3])
    txtHumi.set("%.2f" % x[4])
    
    time_lst,value_lst = table.getXYAxis(t,x[0],0)
    
    canvas.get_tk_widget().destory()
    showPic(time_lst,value_lst)
    
def txtColor(pm25,pm10,temp,humi):
    if pm25 <= 35:
        lblPM25Val.config(fg = 'green')
    elif pm25 > 35 and pm25 <= 53:
        lblPM25Val.config(fg = 'orange')
    elif pm25 > 53 and pm25 <70:
        lblPM25Val.config(fg = 'red')
    else:
        lblPM25Val.config(fg = 'purple')

def showPic(x_lst,y_lst):
    global canvas
    
    f = Figure(figsize=(10,5), dpi=100)
    
    a = f.add_subplot(111)
    a.plot(x_lst,y_lst)
    
    canvas = FigureCanvasTkAgg(f,selfPicFrame)
    canvas.show()
    canvas.get_tk_widget().pack()
    
def min5Click():
    pass

def min30Click():
    pass

def minHourClick():
    pass

#=================================GUI Generate================================#
db = DBService()                                            #資料庫物件
table = TableService()                                      #資料表處理物件

#------------------------------------------------Windows-----------------------
window = tk.Tk()                                            #產生視窗
window.geometry("1024x768")                                 #設定視窗大小
window.title("GPMS")                                        #視窗標題

leftFrame = tk.Frame(window,height = 768,width = 310)       #左框架比例 3
leftFrame.grid(row = 0,column = 0,padx = 5)                 #邊距 5,位置=0列 0欄
leftFrame.grid_propagate(0)                                 #固定框架大小

rightFrame = tk.Frame(window,height = 768,width = 710)      #右框架比例 7
rightFrame.grid(row = 0,column = 1,padx = 5)                #邊距 5,位置=0列 1欄
rightFrame.grid_propagate(0)                                #固定框架大小

labelFrame = tk.Frame(leftFrame,height = 250,width = 310,   #左上文字區, 高度比例 1
                      bd = 2,relief='groove')               #邊框寬 2, style = groove
labelFrame.pack(padx = 6,pady = 6,                          #邊距 x , y 各 6
                fill = 'both',expand = 1)                   #填滿父框架
labelFrame.pack_propagate(0)                                #固定框架大小

#-----------------------------------------------Label--------------------------
txtSite = tk.StringVar()                                    #動態測站名稱
txtPM25 = tk.StringVar()                                    #動態 PM2.5 值
txtPM10 = tk.StringVar()                                    #動態 PM10 值
txtTemp = tk.StringVar()                                    #動態溫度值
txtHumi = tk.StringVar()                                    #動態濕度值

txtSite.set("測試標題")
lblSite = tk.Label(labelFrame,font = ("微軟正黑體",20),       #測站標籤, 字型, 大小
                   textvariable = txtSite)                  #動態測站
lblSite.place(relx = 0.35 ,rely = 0.01)                      #對齊係數

lblPM25 = tk.Label(labelFrame, font = ("微軟正黑體",18),      #PM2.5 文字標籤
                   text = "PM2.5：")
lblPM25.place(relx = 0.05,rely = 0.3)                       #對齊係數
txtPM25.set(35)
lblPM25Val = tk.Label(labelFrame, font = ("微軟正黑體",18),   #PM2.5 值標籤
                      fg = 'red', textvariable = txtPM25)   #文字顏色 = 紅, 動態產生
lblPM25Val.place(relx = 0.35,rely = 0.3)                    #對齊係數

lblPM10 = tk.Label(labelFrame, font = ("微軟正黑體",18),      #PM10 文字標籤
                   text = "PM10：")
lblPM10.place(relx = 0.06,rely = 0.6)                       #對齊係數
txtPM10.set(35)
lblPM10Val = tk.Label(labelFrame, font = ("微軟正黑體",18),   #PM10 值標籤
                      fg = 'red', textvariable = txtPM10)   #文字顏色 = 紅, 動態產生
lblPM10Val.place(relx = 0.35,rely = 0.6)                    #對齊係數

lblTemp = tk.Label(labelFrame, font = ("微軟正黑體",18),      #溫度文字標籤
                   text = "溫度：")
lblTemp.place(relx = 0.55,rely = 0.3)                       #對齊係數
txtTemp.set(30.3)
lblTempVal = tk.Label(labelFrame, font = ("微軟正黑體",18),   #溫度值標籤
                      fg = 'red', textvariable = txtTemp)   #文字顏色 = 紅, 動態產生
lblTempVal.place(relx = 0.8,rely = 0.3)                     #對齊係數

lblHumi = tk.Label(labelFrame,font = ("微軟正黑體",18),       #濕度文字標籤
                   text = "濕度：")
lblHumi.place(relx = 0.55,rely = 0.6)                       #對齊係數
txtHumi.set(63.6)
lblHumiVal = tk.Label(labelFrame,font = ("微軟正黑體",18),    #濕度值標籤
                      fg = 'red', textvariable = txtHumi)   #文字顏色 = 紅, 動態產生
lblHumiVal.place(relx = 0.8,rely = 0.6)                     #對齊係數

locationFrame = tk.Frame(leftFrame,height = 512,            #測站清單元件
                         width = 410,relief='groove',       #style = groove
                         bd = 2)                            #框線寬度 = 2
locationFrame.pack(pady = 6,padx = 6)                       #框架邊距 x,y 各 6
locationFrame.pack_propagate(0)                             #固定框架大小

#----------------------------------------------Listbox-------------------------
all_site_lst = []                                           #測站陣列
st_lst = tk.StringVar()                                     #動態測站陣列
getSite()                                                   #從資料庫取得測站
st_lst.set(all_site_lst)                                    #設定測站陣列
siteLst = tk.Listbox(locationFrame,listvariable = st_lst,   #測站綁定清單
                     height = 512,width = 310,              #清單寬高
                     font =("微軟正黑體",20),                 #清單字型, 大小
                     relief = 'groove')                     #style = groove
siteLst.bind('<<ListboxSelect>>',lstClick)                  #list box click event
siteLst.pack()                                              #清單排版

#---------------------------------------------Button---------------------------
btnFrame = tk.Frame(rightFrame,height = 50,width = 710,     #時間間隔鈕框架
                    relief = 'groove',bd = 2)               #邊框 = 2, style = groove
btnFrame.pack()                                             #框架排版
btnFrame.pack_propagate(0)                                  #固定框架大小

btn5 = tk.Button(btnFrame,text = "一小時",                   #5 分鐘鈕
                 font = ("微軟正黑體",14),                    #字體、大小
                 command = minHourClick)                    #Click 事件
btn5.place(relx = 0.15,rely = 0.05)                         #對齊係數

btn30 = tk.Button(btnFrame,text ="30分鐘",                  #30 分鐘鈕
                  font = ("微軟正黑體",14),                  #字體、大小
                  command = min30Click)                    #Click 事件
btn30.place(relx = 0.45,rely = 0.05)                       #對齊係數

btnHour = tk.Button(btnFrame,text = "5分鐘",                #一小時鈕
                    font = ("微軟正黑體",14),                #字體大小
                    command = min5Click)                   #Click 事件
btnHour.place(relx = 0.75,rely = 0.05)                     #對齊係數

#---------------------------------------------Canvans--------------------------
selfPicFrame = tk.Frame(rightFrame,                         #圖表框架
                        height = 355,width = 710,           #寬、高
                        bd = 2,relief = 'groove')           #框線寬 = 2, style =groove
selfPicFrame.pack(padx = 5,pady = 5)                        #框架邊距
selfPicFrame.pack_propagate(0)                              #固定框架大小

x_lst,y_lst = []

f = Figure(figsize=(10,5), dpi=100)
a = f.add_subplot(111)
a.plot(x_lst,y_lst)
cavans = FigureCanvasTkAgg(f,selfPicFrame)
cavans.show()
cavans.get_tk_widget().pack()


areaPicFrame = tk.Frame(rightFrame,                         #該點區域框架
                        height = 355,width = 710,           #寬、高
                        bd = 2,relief = 'groove')           #框架寬 = 2, style = groove
areaPicFrame.pack(padx = 5,pady = 5)                        #框架邊距
areaPicFrame.pack_propagate(0)                              #固定框架大小

window.mainloop()