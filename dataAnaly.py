from DBService import DBService

class dataAnaly:
    
    #Get neighbor point id
    def getAreaData(self,timeStr):
        self.db = DBService()
        gps = []
        self.neighbor_gps = []
        
        r_data = self.db.readAllAirData(timeStr)
        
        for item in r_data:
            gps.append([item[0],item[5],item[6]])
        
        #cal neighbor point
        for i in gps:
            temp = []
            temp.append(i[0])
            
            for j in gps:
                if abs(i[1]-j[1]) <= 0.1 and abs(i[1]-j[1]) > 0:
                    if abs(i[2]-j[2]) <= 0.1  and abs(i[2]-j[2]) > 0:
                        temp.append(j[0])
                        
            self.neighbor_gps.append(temp)
        #return self.neighbor_gps
    
    def getAreaAirInfo(self,timeStr):
         
        self.neighbor_pm25pm10 = []
        for item in self.neighbor_gps:
            temp = []
            
            for i in item:
                r_data = self.db.readPM25PM10(timeStr,i)
                temp.append(r_data)
                
            self.neighbor_pm25pm10.append(temp)
        return self.neighbor_pm25pm10