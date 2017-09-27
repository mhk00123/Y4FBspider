# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:06:34 2017

@author: user
"""
#==============================import package==============================#

from excelService import Service        #excel class
from DBService import DBService         #DB class
from bs4 import BeautifulSoup as bs     #html parse package
import requests,time                    #html package , time package

#=================================Method===================================#
def urlService():
    #url handle
    for Id in all_id_lst:
        for sensor in sensor_lst:
            #get url 
            url = 'http://www.airq.org.tw/Home/GetCurrentValueApi?station={}&sensor={}'.format(Id,sensor)
            #get html text
            html = requests.get(url).text
            parse = bs(html,'html.parser')
            
            #remove invalid id
            if str(parse.find('title')).find('錯誤') != -1:
                error_id_lst.append(Id)
            else:
                url_lst.append(url)
                id_lst.append(Id)

def getUsefulValue():
    # remove repeat id            
    tempId=[]            
    for idx in range(0,len(id_lst),4):
        tempId.append(id_lst[idx])
        
    id_lst.clear()
    for item in tempId:
        id_lst.append(item)
    
    #get all useful info
    for item in id_lst:
        for idx in range(0,len(all_id_lst)):
            if(item == all_id_lst[idx]):
                note_lst.append(all_note_lst[idx])
                lat_lst.append(all_lat_lst[idx])
                lon_lst.append(all_lon_lst[idx])

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

#get all cols data from excel 
excel = Service()
all_id_lst = excel.getId()      #stId       
all_lat_lst = excel.getLat()    #stLatitude
all_lon_lst = excel.getLon()    #stLongitude
all_note_lst = excel.getNote()  #stNote

#sensor list
sensor_lst = ['pm2.5','pm10','temperature','humidity']

id_lst = []                     #useful stId list
url_lst = []                    #useful url list
lat_lst = []                    #useful latitude list
lon_lst = []                    #useful longitude list
note_lst = []                   #useful note list
error_id_lst = []                  #useful error list

#Get all useful info
urlService()
getUsefulValue()

#Air value lists
pm25_lst = []                   #pm2.5 lsit
pm10_lst = []                   #pm10 list
t_lst = []                      #temperatuer lsit
h_lst = []                      #humidity list
getAirValue()                   #get all air value

#database instance
db=DBService()
#db.createSiteData(id_lst,lat_lst,lon_lst,note_lst)

timeStr = time.strftime('%Y_%m_%d_%H_%M')                           #get current time
db.createAirData(timeStr,id_lst,pm25_lst,pm10_lst,t_lst,h_lst)      #Create AriInfo table
data = db.ReadAirData(timeStr)

for item in data:
    print(item[0],item[1],item[2],item[3],item[4])
#excel.outputExcel(id_lst,note_lst,pm25_lst,pm10_lst,t_lst,h_lst)

