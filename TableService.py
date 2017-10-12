# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 05:27:44 2017

@author: Mayday
"""

import matplotlib.pyplot as plt          #繪圖 package
import numpy as np                       #統計 package
from DBService import DBService          #資料庫類別

class TableService():
    
    #2017-10-12 add by Mayday
    def __init__(self):
        self.db = DBService()                   #new database instance
    
    #2017-10-12 add by Mayday
    # <summary>Get all talbe name</summary>
    # <return>Table name list</return>
    def getAllTableName(self):
        tables = self.db.readAllTableName()
        
        result = []
        for item in tables:
            result.append(item[1])
        
        return result 
    
    #2017-10-12 add by Mayday
    # <summary> 取得 x 與 y 軸的數據 </summary>
    # <param name = "table_name"> 表格名稱或表格陣列 </param>
    # <param name = "stId"> 測站名稱 </param>
    # <param name = "tag"> 時間模式 </param>
    # <return> X 軸數據, y 軸數據 </return>
    def getXYAxis(self,table_name,stId,tag):
        
        pm25_lst = []
        time_lst = []
        
        if tag == 0:                                 #get the timeline of hour
            h = int(table_name[-1].split('_')[-2])       #get current hour 
            for i in range(h-11,h+1):                #過去 12 小時到現在
                time_lst.append(i)
            
            for i in range(len(table_name)-144,             
                           len(table_name),12):
                x = self.db.readPM25ById(table_name[i],stId)
                pm25_lst.append(x[1])
            
        elif tag ==1:                                #get the timeline of 30 min
            pass
        else:                                        #get the timeline of 5 min
            pass
        
        return time_lst,pm25_lst