# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:22:47 2017

@author: user
"""

import sqlite3

class DBService:
    
    def insertData(self,id_lst,lat_lst,lon_lst,note_lst,pm25_lst,pm10_lst,t_lst,h_lst):
        self.id_lst = id_lst
        self.lat_lst = lat_lst
        self.lon_lst = lon_lst
        self.note_lst = note_lst
        self.pm25_lst = pm25_lst
        self.pm10_lst = pm10_lst
        self.t_lst = t_lst
        self.h_lst = h_lst
        connection = sqlite3.connect('PM25.sqlite')
        
        for i in range(0,len(id_lst)):
            sqlStr="insert into SiteInfo values('{}',{},{},'{}',{},{},{},{})".format(
                    self.id_lst[i],self.lat_lst[i],self.lon_lst[i],self.note_lst[i],
                    self.pm25_lst[i],self.pm10_lst[i],self.t_lst[i],self.h_lst[i])
            connection.execute(sqlStr)
        connection.commit()
        connection.close()
        
