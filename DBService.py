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
        
    def createAirData(self,timeStr,id_lst,pm25_lst,pm10_lst,t_lst,h_lst):
        connection = sqlite3.connect('PM25.sqlite')
        sqlStr = """CREATE TABLE AirInfo_{} 
                    (stId VARCHAR NOT NULL,
                    PM25 INTEGER,
                    PM10 INTEGER,
                    Temperature DOUBLE,
                    Humidity DOUBLE,
                    PRIMARY KEY(stId),
                    FOREIGN KEY(stId) REFERENCES SiteInfo(stId))""".format(timeStr)
        connection.execute(sqlStr)
        connection.commit()
        
        for i in range(0,len(id_lst)):
            sqlStr = "INSERT INTO AirInfo_{} VALUES('{}',{},{},{},{})".format(
                    timeStr,id_lst[i],pm25_lst[i],pm10_lst[i],t_lst[i],h_lst[i])
            connection.execute(sqlStr)
        connection.commit()
        connection.close()
    
    #Read all air data 
    #<param> timeStr = table name </param>
    #<return> sorted all air data </return>
    def readAllAirData(self,timeStr):
        connection = sqlite3.connect('PM25.sqlite')
        queryStr="""SELECT AirInfo_{}.*, SiteInfo.stLatitude,
                    SiteInfo.stLongitude, SiteInfo.stNote 
                    FROM AirInfo_{}, SiteInfo 
                    WHERE SiteInfo.stId = AirInfo_{}.stId
                    ORDER BY SiteInfo.stLatitude ASC, SiteInfo.stLongitude ASC""".format(
                    timeStr,timeStr,timeStr)
                    
        cursor = connection.execute(queryStr)
        result = cursor.fetchall()
        
        return result
    
    #Read PM25 and PM10 by Id
    #<return>one PM25 and PM10 </return>
    def readPM25PM10(self,timeStr,Id):
        connection = sqlite3.connect('PM25.sqlite')
        queryStr = 'SELECT AirInfo_{}.PM25, AirInfo_{}.PM10 FROM AirInfo_{} \
                      WHERE stId = "{}"'.format(timeStr,timeStr,timeStr,Id)
        cursor = connection.execute(queryStr)
        r_data = cursor.fetchall()
        
        return r_data
        
    