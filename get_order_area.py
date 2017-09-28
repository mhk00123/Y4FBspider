import sqlite3
import DBService

def get_area_data(timeStr):
	x = DBService.DBService()
	gps = []
	sort_gps = []

	with sqlite3.connect('PM25.sqlite') as con:
		c = con.cursor()
		r_data = x.readAirData(timeStr)

	for item in r_data:
		gps.append([item[0],item[5],item[6]])

	for i in gps:
		order = []
		for j in gps:
			if abs(i[1]-j[1])<=0.1 and abs(i[1]-j[1]) >= 0 : #(0,0.1]
				order.append(j[0])
		sort_gps.append(order)

	return sort_gps