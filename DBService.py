# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:22:47 2017

@author: user
"""

import sqlite3,os

class DBService:
    
    #2017-10-12 add by Mayday
    def __init__(self):
        self.path = os.path.dirname(__file__)
    
    #2017-10-12 add by Mayday
    # <summary> Read all table name </summary>
    # <return> All table name list </return>
    def readAllTableName(self):
        connection = sqlite3.connect(self.path + '/' + 'PM25.sqlite')
        queryStr = '''SELECT type,name FROM sqlite_master WHERE type = "table"
                      AND name LIKE "A%"'''
        result = connection.execute(queryStr).fetchall()
        
        return result
    
    # <summary>Create site table</summary>
    # <param name = "id_lst">   Site id list        </param>
    # <param name = "lat_lst">  Site latitude list  </param>
    # <param name = "lon_lst">  Site longitude list </param>
    # <param name = "note_lst"> Site name list      </param>
    def createSiteData(self,id_lst,lat_lst,lon_lst,note_lst,):
        self.id_lst = id_lst
        self.lat_lst = lat_lst
        self.lon_lst = lon_lst
        self.note_lst = note_lst
        connection = sqlite3.connect('PM25.sqlite')
        
        #create site table
        sqlStr = """create table if not exists SiteInfo(
                    stId varchar primary key not null,
                    stLatitude float,
                    stLongitude float,
                    stNote varchar)"""
        connection.execute(sqlStr)
        
        for i in range(0,len(id_lst)):
            sqlStr="insert into SiteInfo values('{}',{},{},'{}')".format(
                    self.id_lst[i],self.lat_lst[i],self.lon_lst[i],self.note_lst[i],)
            connection.execute(sqlStr)
        connection.commit()
        connection.close()
    
    # <summary>Read stie information</summary>
    # <return>Site information</return>
    def readSiteData(self):
        queryStr = 'select SiteInfo.* from SiteInfo'
        connection = sqlite3.connect(self.path + '/' + 'PM25.sqlite')
        cursor = connection.execute(queryStr)
        result = cursor.fetchall()
        
        return result
    
    # <summary>create air table</summary>
    # <param name = "timeStr">  table name             </param>
    # <param name = "id_lst">   Site Id list           </param>
    # <param name = "pm25_lst"> PM2.5 value list       </param>
    # <param name = "pm10_lst"> PM10 value list        </param>
    # <param name = "t_lst">    Temperature value list </param>
    # <param name = "h_lst">    Humidity value list    </param>
    def createAirData(self,timeStr,id_lst,pm25_lst,pm10_lst,t_lst,h_lst):
        connection = sqlite3.connect(self.path + '/' + 'PM25.sqlite')
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
    
    # 2017-10-12 add by Mayday
    # <summary>Read air data by station name </summary>
    # <param name = "table_name"> Table name </param>
    # <param name = "stNote"> Station name   </param>
    # <return> Air data belonging to station name </return>
    def readAirDataByNote(self,table_name,stNote):
        connnection = sqlite3.connect(self.path + '/' + 'PM25.sqlite')
        queryStr = """SELECT {}.* FROM {},SiteInfo
                      WHERE SiteInfo.stId = {}.stId and SiteInfo.stNote = "{}"
                   """.format(table_name,table_name,table_name,stNote)
        cursor = connnection.execute(queryStr)
        result = cursor.fetchone()
        
        return result
    
    # 2017-10-12 add by Mayday
    # <summary> Read PM25 data by Id </summary>
    # <param name ="table_name"> Table name </param>
    # <param name ="Id"> Data Id </param>
    # <teturn> one PM25 data belonging to id</return>
    def readPM25ById(self,table_name,Id):
        connection = sqlite3.connect(self.path + '/' + 'PM25.sqlite')
        queryStr = 'SELECT stId,PM25 FROM {} WHERE stId = "{}"'.format(
                table_name,Id)
        cursor = connection.execute(queryStr)
        result = cursor.fetchone()
        
        return result
    
    # 2017-10-13 add by Mayday
    # <summary> Get site note by site Id </summary>
    # <param name = "Id"> site id </param>
    # <return> Site note </return>
    def readSiteNoteById(self,Id):
        connnection = sqlite3.connect(self.path + '/' + 'PM25.sqlite')
        queryStr = 'SELECT stNote FROM SiteInfo WHERE stId = "{}"'.format(Id)
        cursor = connnection.execute(queryStr)
        result = cursor.fetchone()
        
        return result 
    
    # <summary>Read all area data</summary> 
    # <param name = "timeStr"> table name </param>
    # <return> sorted all area data </return>
    def readAreaData(self,timeStr):
        connection = sqlite3.connect(self.path + '/' + 'PM25.sqlite')
        queryStr="""SELECT AirInfo_{}.stId, SiteInfo.stLatitude,
                    SiteInfo.stLongitude, SiteInfo.stNote 
                    FROM AirInfo_{}, SiteInfo 
                    WHERE SiteInfo.stId = AirInfo_{}.stId
                    ORDER BY SiteInfo.stLatitude ASC, SiteInfo.stLongitude ASC""".format(
                    timeStr,timeStr,timeStr)
                    
        cursor = connection.execute(queryStr)
        result = cursor.fetchall()
        
        return result
    
    # <summary>Read PM25 and PM10 by Id</summary>
    # <param name = "timeStsr">table name </param>
    # <param name = "Id">      Site Id    </param>
    # <return>one PM25 and PM10 </return>
    def readPM25PM10(self,timeStr,Id):
        connection = sqlite3.connect(self.path + '/' + 'PM25.sqlite')
        queryStr = 'SELECT AirInfo_{}.PM25, AirInfo_{}.PM10 FROM AirInfo_{} \
                      WHERE stId = "{}"'.format(timeStr,timeStr,timeStr,Id)
        cursor = connection.execute(queryStr)
        r_data = cursor.fetchall()
        
        return r_data
    
    # <summary>select Alpha n by Id</summary>
    # <param name = "n"> 樣本數     </param>
    # <return>Alpha n</return>
    def selectGAlpha(self,n):
        queryStr = 'select GrubbsTValue.alpha from GrubbsTValue where N = {}'.format(n)
        connection = sqlite3.connect(self.path + '/' + 'PM25.sqlite')
        cursor = connection.execute(queryStr)
        
        return cursor.fetchall()