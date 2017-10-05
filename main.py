# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:06:34 2017

@author: user
"""
#==============================import package==============================#

from excelService import Service        #excel class
from DBService import DBService         #DB class
from Helper import Helper               #data helper class
from dataAnaly import dataAnaly         #data analy package
import requests,time                    #html package , time package
#from FB import getInfo

#=================================Method===================================#
def getAirValue():
    
    for i in range(0,len(url_lst)):
        htmlStr = requests.get(url_lst[i]).text
        tempStr = htmlStr.split(":")[-1]
        if i%4 == 0:
            pm25_lst.append(int(tempStr[:-3]))
        if i%4 == 1:
            pm10_lst.append(int(tempStr[:-3]))
        if i%4 == 2:
            t_lst.append(float(tempStr[:-3]))
        if i%4 == 3:
            h_lst.append(float(tempStr[:-3]))

#==============================Main Programe===============================#
db = DBService()
data = Helper()
excel = Service()

#sensor list
sensor_lst = ['pm2.5','pm10','temperature','humidity']
'''
#the following execute at first time
#get all cols data from excel
all_id_lst = excel.getId()      #stId       
all_lat_lst = excel.getLat()    #stLatitude
all_lon_lst = excel.getLon()    #stLongitude
all_note_lst = excel.getNote()  #stNote

id_lst,url_lst = data.urlHelper(all_id_lst,sensor_lst) 
lat_lst,lon_lst,note_lst = data.dataHelper(all_id_lst,all_lat_lst,
                                           all_lon_lst,all_note_lst)
db.createSiteData(id_lst,lat_lst,lon_lst,note_lst)
'''

#the following execute after the first time
result = db.readSiteData()
all_id_lst = []
for item in result:
    all_id_lst.append(item[0])
id_lst,url_lst = data.urlHelper(all_id_lst,sensor_lst)

#Air value lists
pm25_lst = []                   #pm2.5 lsit
pm10_lst = []                   #pm10 list
t_lst = []                      #temperatuer lsit
h_lst = []                      #humidity list
getAirValue()                   #get all air value

timeStr = time.strftime('%Y_%m_%d_%H_%M')                           #get current time
db.createAirData(timeStr,id_lst,pm25_lst,pm10_lst,t_lst,h_lst)      #Create AriInfo table
data = db.readAreaData(timeStr)                                     #Read AriInfo table

#data analy instance
analy = dataAnaly()
y = analy.getAreaData(timeStr)                  #get near area 
analy.getAreaAirInfo(timeStr)                   #get near area air information

analy.s_PM25()                                  #cal near area air PM25 標準差 
analy.s_PM10()                                  #cal near area air PM10 標準差
analy.avg_PM25()                                #cal near area average PM25
analy.avg_PM10()                                #cal near area average PM10
x = analy.grubbsTest()                          #cal final value

for i in range(0,len(x)):
    print('{}. {}'.format(i,x[i]))

#fb = getInfo()
#fb.post_to_page(x[0])
#excel.outputExcel(id_lst,note_lst,pm25_lst,pm10_lst,t_lst,h_lst)
