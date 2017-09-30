from DBService import DBService
import numpy as np

class dataAnaly:
    
    #Get neighbor point id
    def getAreaData(self,timeStr):
        self.db = DBService()
        gps = []
        self.area_gps = []
        self.note = []
        r_data = self.db.readAllAirData(timeStr)
        
        for item in r_data:
            gps.append([item[0],item[5],item[6],item[7]])
            self.note.append(item[7])
        
        #cal area point
        for i in gps:
            temp = []
            temp.append(i[0])
            
            for j in gps:
                if abs(i[1]-j[1]) <= 0.1 and abs(i[1]-j[1]) > 0:
                    if abs(i[2]-j[2]) <= 0.1  and abs(i[2]-j[2]) > 0:
                        temp.append(j[0])
                        
            self.area_gps.append(temp)
        #return self.neighbor_gps
    
    def getAreaAirInfo(self,timeStr):
         
        self.area_pm25 = []
        self.area_pm10 = []
        for item in self.area_gps:
            temp25 = []
            temp10 = []
            for i in item:
                r_data = self.db.readPM25PM10(timeStr,i)
                temp25.append(r_data[0][0])
                temp10.append(r_data[0][1])
                
            self.area_pm25.append(temp25)
            self.area_pm10.append(temp10)
        
        #return self.neighbor_pm25,self.neighbor_pm10
    
    #PM25 標準差
    def s_PM25(self):
        self.s_pm25_lst = []
        for item in self.area_pm25:
            self.s_pm25_lst.append(np.std(item))
            
    #PM10 標準差
    def s_PM10(self):
        self.s_pm10_lst = []
        for item in self.area_pm10:
            self.s_pm10_lst.append(np.std(item))
    
    #PM25 Average
    def avg_PM25(self):
        self.avg_pm25_lst = []
        for item in self.area_pm25:
            self.avg_pm25_lst.append(np.mean(item))
    
    #PM10 Average    
    def avg_PM10(self):
        self.avg_pm10_lst = []
        for item in self.area_pm10:
            self.avg_pm10_lst.append(np.mean(item))
    
    #cal grubbsTest value         
    def grubbsTest(self):
        
        self.area_final = []
        index = 0                                       #item index
        for item in self.area_pm25:
            An = self.db.selectGAlpha(len(item))
            x = str(An)[2:-3]
            if(x == ''):
                x = float(0)
            else:
                x = float(x)
            Gn = abs((item[0] - self.avg_pm25_lst[index])/self.s_pm25_lst[index])
            final = x - Gn
            if final < 0:
                self.area_final.append(self.note[index])
                
            index += 1
            
        return self.area_final