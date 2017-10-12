# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:44:15 2017

@author: user
"""

from win32com import client as office
import os

class Service:
    
    # <summary>Read site id from excel file</summary>
    # <return>Site id list</return>
    def getId(self):
        self.path = os.path.dirname(__file__)
        self.excel = office.gencache.EnsureDispatch('Excel.Application')
        self.wb = self.excel.Workbooks.Open(self.path+"\\佈點資料.xlsx")
        self.ws = self.wb.Worksheets('工作表1')
        self.lastrow = self.ws.Cells(self.ws.Rows.Count,"A").End(-4162).Row + 1
        
        id_list=[]
        
        for row in range(2,self.lastrow):
            data=self.ws.Range("A"+str(row)).Value
            id_list.append(data)
    
        #self.excel.Quit()
        return id_list

    # <summary>Read site latitude from excel file</summary>
    # <return>Site latitude list</return>
    def getLat(self):
        lat_lst=[]
        
        for row in range(2,self.lastrow):
            data=self.ws.Range("B"+str(row)).Value
            lat_lst.append(data)
        
        #self.excel.Quit()
        return lat_lst
    
    # <summary>Read site longitude from excel file</summary>
    # <return>Site longitude list</return>
    def getLon(self):
        lon_lst=[]
        
        for row in range(2,self.lastrow):
            data = self.ws.Range("C"+str(row)).Value
            lon_lst.append(data)
            
        #self.excel.Quit()
        return lon_lst
    
    # <summary>Read site name from excel file</summary>
    # <return>Site name list</return>
    def getNote(self):
        note_lst=[]
        
        for row in range(2,self.lastrow):
            data=self.ws.Range("D"+str(row)).Value
            note_lst.append(data)
            
        #self.excel.Quit()
        return note_lst
    
    # <summary>Output site and air value to excel</summary>
    # <param name = "id_lst">   Site id value list     </param>
    # <param name = "note_lst"> Site name list         </param>
    # <param name = "pm25_lst"> PM2.5 value list       </param>
    # <param name = "pm10_lst"> PM10 value list        </param>
    # <param name = "t_lst">    Temperature value list </param>
    # <param name = "h_lst">    Humidity value list    </param>
    def outputExcel(self,id_lst,note_lst,pm25_lst,pm10_lst,t_lst,h_lst):
        self.ws = self.wb.Worksheets('數據')
        cols = ['A','B','C','D','E','F']
        
        for i in range(0,len(cols)):
            data = 0
            for row in range(2,(len(id_lst)+2)):
                if i%6 == 0:
                    self.ws.Range('A{}'.format(row)).Value = id_lst[data]
                if i%6 == 1:
                    self.ws.Range('B{}'.format(row)).Value = note_lst[data]
                if i%6 == 2:
                    self.ws.Range('C{}'.format(row)).Value = pm25_lst[data]
                if i%6 == 3:
                    self.ws.Range('D{}'.format(row)).Value = pm10_lst[data]
                if i%6 == 4:
                    self.ws.Range('E{}'.format(row)).Value = t_lst[data]
                if i%6 == 5:
                    self.ws.Range('F{}'.format(row)).Value = h_lst[data]
                data += 1
        
        self.excel.Quit()
                