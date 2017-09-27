# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:22:47 2017

@author: user
"""

import sqlite3

class DBService:
    
    def createSiteData(self,id_lst,lat_lst,lon_lst,note_lst,):
        self.id_lst = id_lst
        self.lat_lst = lat_lst
        self.lon_lst = lon_lst
        self.note_lst = note_lst
        connection = sqlite3.connect('PM25.sqlite')
        
        for i in range(0,len(id_lst)):
            sqlStr="insert into SiteInfo values('{}',{},{},'{}')".format(
                    self.id_lst[i],self.lat_lst[i],self.lon_lst[i],self.note_lst[i],)
            connection.execute(sqlStr)
        connection.commit()
        connection.close()
        
    def createAirData(self,timeStr,id_lst,lat_lst,lon_lst,pm25_lst,pm10_lst,t_lst,h_lst):
        self.timeStr = timeStr
        connection = sqlite3.connect('PM25.sqlite')
        sqlStr = """CREATE TABLE AirInfo_{} 
                    (stId VARCHAR NOT NULL,
                    Latitude FLOAT,
                    Longitude FLOAT,
                    PM25 INTEGER,
                    PM10 INTEGER,
                    Temperature FLOAT,
                    Humidity FLOAT,
                    PRIMARY KEY(stId),
                    FOREIGN KEY(stId) REFERENCES SiteInfo(stId))""".format(self.timeStr)
        connection.execute(sqlStr)
        connection.commit()
        
        for i in range(0,len(id_lst)):
            sqlStr = "INSERT INTO AirInfo_{} VALUES('{}',{},{},{},{},{},{})".format(
                    self.timeStr,id_lst[i],lat_lst[i],lon_lst[i],pm25_lst[i],pm10_lst[i],t_lst[i],h_lst[i])
            connection.execute(sqlStr)
        connection.commit()
        connection.close()
    
    def ReadAirData(self,timeStr):
        
        connection = sqlite3.connect('PM25.sqlite')
        sqlStr = "select * from AirInfo_{} ORDER BY Latitude ASC, Longitude ASC".format(timeStr)
        cursor = connection.cursor()
        cursor.execute(sqlStr)
        data = cursor.fetchall()
        
        return data
        
        
        