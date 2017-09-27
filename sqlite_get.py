import sqlite3
import DBService

x = DBService.DBService()
	
gps = []
sort_gps = []

with sqlite3.connect('PM25.sqlite') as con:
	c = con.cursor()
	k = x.ReadAirData('2017_09_27_17_10')

	for item in k:
		gps.append([item[0],item[1],item[2]])

#print(gps)
for i in gps:
	order = []
	for j in gps:
		if abs(i[1] - j[1]) <= 0.1 and abs(i[1] - j[1]) >=0: 
			order.append(j[0])
	sort_gps.append(order)

j=0
for i in sort_gps:
	print(j)
	print(i)
	j+=1