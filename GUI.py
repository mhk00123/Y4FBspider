# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 01:50:57 2017

@author: Mayday
"""

#===================================GUI package===============================#
import tkinter as tk                         #視窗 package
import matplotlib                            #繪圖 package
matplotlib.use("TkAgg")                      #同上
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg            #同上
from matplotlib.figure import Figure
from matplotlib import style
style.use('ggplot')
import numpy as np


from DBService import DBService              #Database class
from TableService import TableService        #Table service class
from dataAnaly import dataAnaly              #Data analy class 

#==================================Function===================================#
def getSite():
    global all_site_lst
    x = db.readSiteData()
    for item in x:
        all_site_lst.append(item[3])

def lstClick(evt):
    global txtSite,txtPM25,txtPM10,txtTemp,txtHumi,interval,tb
    
    #選測站已後時間鈕有效
    btn5.config(state = 'normal')
    btn30.config(state = 'normal')
    btnHour.config(state = 'normal')
    
    w = evt.widget                          #listbox instance
    index = int(w.curselection()[0])        #list item's index
    value = w.get(index)                    #user selected item
    txtSite.set(value)
    
    tb = table.getAllTableName()
    x = db.readAirDataByNote(tb[-1],value)   #get air data by selected item
    txtColor(x[1],x[2],x[3],x[4])
    txtPM25.set(x[1])
    txtPM10.set(x[2])
    txtTemp.set("%.2f" % x[3])
    txtHumi.set("%.2f" % x[4])
    
    interval = 60
    time_lst,value_plot_lst = table.getXYAxis(tb,x[0],interval)
    showPic(value,time_lst,value_plot_lst,interval)
    
    x_lst,value_bar_lst = table.getXYAxis(tb[-1],x[0],interval = 0)
    showPic(txtSite.get(),x_lst,value_bar_lst,interval = 0)
    
def showPic(title,x_lst,y_lst,interval):
    global figSelf
    
    if interval == 60:
        picSelf.clear()                         #需要先清除畫布物件
        picSelf.plot(x_lst,y_lst)               #填入新數據
        picSelf.set_aspect('auto',adjustable = 'box')
    elif interval == 30 or interval == 5:
        picSelf.clear()                             #需要先清除畫布物件
        group = np.arange(len(x_lst))
        picSelf.plot(group,y_lst)
        picSelf.set_xticks(group)
        picSelf.set_xticklabels(x_lst,rotation = 45,
                                fontsize = (8))
    else:
        picArea.clear()
        group = np.arange(len(x_lst))
        picArea.bar(group,y_lst)
        picArea.set_xticks(group)
        picArea.set_xticklabels(x_lst,rotation = 45)
        
    #pic.set_xlabel("時間")                   #圖表 X 軸標題
    picSelf.set_ylabel("PM2.5")              #圖表 Y 軸標題
    picArea.set_ylabel("PM2.5")
    picSelf.set_title(txtSite.get())         #圖表標題
    canvasSelf.draw()                        #畫布容器重畫
    canvasArea.draw()
    
def txtColor(pm25,pm10,temp,humi):          #改變文字顏色
    if pm25 <= 15:
        lblPM25Val.config(fg = 'green')
    elif pm25 > 15 and pm25 <= 35:
        lblPM25Val.config(fg = 'gold')
    elif pm25 > 35 and pm25 <= 54:
        lblPM25Val.config(fg = 'orange')
    elif pm25 > 54 and pm25 <= 150:
        lblPM25Val.config(fg = 'red')
    elif pm25 >150 and pm25 <=250:
        lblPM25Val.config(fg = 'purple')
    else:
        lblPM25Val.config(fg = 'darkred')
        
    if pm10 <= 54:
        lblPM10Val.config(fg = 'green')
    elif pm10 >54 and pm10 <= 125:
        lblPM10Val.config(fg = 'gold')
    elif pm10 >125 and pm10 <= 254:
        lblPM10Val.config(fg = 'orange')
    elif pm10 >254 and pm10 <= 354:
        lblPM10Val.config(fg = 'red')
    elif pm10 >354 and pm10 <= 424:
        lblPM10Val.config(fg = 'purple')
    else:
        lblPM10Val.config(fg = 'darkred')

def min5Click():
    global txtSite,interval,tb
    
    interval = 5
    x = db.readAirDataByNote(tb[-1],txtSite.get())
    time_lst,value_lst = table.getXYAxis(tb,x[0],interval)
    showPic(txtSite.get(),time_lst,value_lst,interval)


def min30Click():
    global txtSite,interval,tb
    
    interval = 30
    x = db.readAirDataByNote(tb[-1],txtSite.get())
    time_lst,value_lst = table.getXYAxis(tb,x[0],interval)
    showPic(txtSite.get(),time_lst,value_lst,interval)

def minHourClick():                                        #一小時按鈕事件
    global txtSite,interval,tb
    
    interval = 60
    x = db.readAirDataByNote(tb[-1],txtSite.get())          #取得測站 Id
    time_lst,value_lst = table.getXYAxis(tb,x[0],interval)
    showPic(txtSite.get(),time_lst,value_lst,interval)

#=================================GUI Generate================================#
db = DBService()                                            #資料庫物件
ana = dataAnaly()                                           #資料分析物件
table = TableService()                                      #資料表處理物件
tb = []                                                     #表格名稱陣列, 初始空陣列

#------------------------------------------------Windows-----------------------
window = tk.Tk()                                            #產生視窗
window.geometry("1280x900")                                 #設定視窗大小
window.title("GPMS")                                        #視窗標題

leftFrame = tk.Frame(window,height = 900,width = 310)       #左框架比例 3
leftFrame.grid(row = 0,column = 0,padx = 5)                 #邊距 5,位置=0列 0欄
leftFrame.grid_propagate(0)                                 #固定框架大小

rightFrame = tk.Frame(window,height = 900,width = 710)      #右框架比例 7
rightFrame.grid(row = 0,column = 1,padx = 5)                #邊距 5,位置=0列 1欄
rightFrame.grid_propagate(0)                                #固定框架大小

labelFrame = tk.Frame(leftFrame,height = 285,width = 310,   #左上文字區, 高度比例 1
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

locationFrame = tk.Frame(leftFrame,height = 600,            #測站清單元件
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
                     height = 600,width = 310,              #清單寬高
                     font =("微軟正黑體",20),                 #清單字型, 大小
                     relief = 'groove')                     #style = groove
siteLst.bind('<<ListboxSelect>>',lstClick)                  #list box click event
siteLst.pack()                                              #清單排版

#---------------------------------------------Button---------------------------
btnFrame = tk.Frame(rightFrame,height = 30,width = 710,     #時間間隔鈕框架
                    relief = 'groove',bd = 2)               #邊框 = 2, style = groove
btnFrame.pack()                                             #框架排版
btnFrame.pack_propagate(0)                                  #固定框架大小

interval = 0                                                #間隔係數, 初始為 0
btn5 = tk.Button(btnFrame,text = "一小時",                   #5 分鐘鈕
                 font = ("微軟正黑體",12),                    #字體、大小
                 command = minHourClick)                    #Click 事件
btn5.place(relx = 0.15,rely = 0.05)                         #對齊係數
btn5.config(state = 'disabled')                             #初始無法按

btn30 = tk.Button(btnFrame,text ="30分鐘",                  #30 分鐘鈕
                  font = ("微軟正黑體",12),                  #字體、大小
                  command = min30Click)                    #Click 事件
btn30.place(relx = 0.45,rely = 0.05)                       #對齊係數
btn30.config(state = 'disabled')                           #初始無法按


btnHour = tk.Button(btnFrame,text = "5分鐘",                #一小時鈕
                    font = ("微軟正黑體",12),                #字體大小
                    command = min5Click)                   #Click 事件
btnHour.place(relx = 0.75,rely = 0.05)                     #對齊係數
btnHour.config(state = 'disabled')                         #初始無法按

#-----------------------------------------Canvas 右上--------------------------
selfPicFrame = tk.Frame(rightFrame,                         #圖表框架
                        height = 390,width = 710,           #寬、高
                        bd = 2,relief = 'groove')           #框線寬 = 2, style =groove
selfPicFrame.pack(padx = 5,pady = 5)                        #框架邊距
selfPicFrame.pack_propagate(0)                              #固定框架大小

figSelf = Figure(figsize=(10,5), dpi=100)                   #生成畫布(大小, 解析)
picSelf = figSelf.add_subplot(111)                          #繪圖物件(列, 欄, Id)
picSelf.plot([],[])                                         #填充空數據
canvasSelf = FigureCanvasTkAgg(figSelf,selfPicFrame)        #將畫布置入視窗
canvasSelf.show()                                           #顯示畫布
canvasSelf.get_tk_widget().pack()                           #畫布排版

#---------------------------------------Canvas 右下----------------------------
areaPicFrame = tk.Frame(rightFrame,                         #該點區域框架
                        height = 460,width = 710,           #寬、高
                        bd = 2,relief = 'groove')           #框架寬 = 2, style = groove
areaPicFrame.pack(padx = 5,pady = 5)                        #框架邊距
areaPicFrame.pack_propagate(0)                              #固定框架大小

figArea = Figure(figsize=(10,5), dpi=100)                   #生成畫布(大小, 解析)
picArea = figArea.add_subplot(111)                          #繪圖物件(列, 欄, Id)
picArea.bar([],[])                                          #填充空數據
canvasArea = FigureCanvasTkAgg(figArea,areaPicFrame)        #將畫布置入視窗
canvasArea.show()                                           #顯示畫布
canvasArea.get_tk_widget().pack()                           #畫布排版


window.mainloop()