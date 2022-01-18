import serial
from datetime import datetime
import time
from pymongo import MongoClient

port = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=2.0)
connection_string="mongodb://makaronas:makaronask2022@150.140.193.156:27017/test?authSource=test&readPreference=primary"
client=MongoClient(connection_string)
dbi=client.get_database("makaronas")
col=dbi.get_collection("test_AQ")


def read_pm_line(_port):
	rv = b''
	while True:
		ch1 = _port.read()
		if ch1 == b'\x42':
			ch2 = _port.read()
			if ch2 == b'\x4d':
				rv += ch1 + ch2
				rv += _port.read(28)
				return rv


loop = 0
rcv_list = []
c=1
p03=p05=p10=p25=p50=p100=0
sp10std=sp25std=sp100std=sp10env=sp25env=sp100env=0
while True:
	#print("aaaaaaaaaaaaaaaa")
	##doc={"sensor":"pms5003_2"}
	#response=col.insert_one(doc)
	#last_id=response.inserted_id
	#print("\n")
	#print(last_id)
	#col.update_one({"_id":last_id},{"$set":{"time":datetime.now()}})
	
	rcv = read_pm_line(port)
	
	pm10std=rcv[4]*256 + rcv[5]
	sp10std=sp10std+pm10std
	
	pm25std=rcv[6] * 256 + rcv[7]
	sp25std=sp25std+pm25std
	
	pm100std= rcv[8] * 256 + rcv[9]
	sp100std=sp100std+pm100std
	
	pm10env= rcv[10] * 256 + rcv[11]
	sp10env=sp10env+pm10env
	
	pm25env= rcv[12] * 256 + rcv[13]
	sp25env=sp10env+pm25env
	
	pm100env= rcv[14] * 256 + rcv[15]
	sp100env=sp10env+pm100env
	
	pgt03um= rcv[16] * 256 + rcv[17]
	p03=p03+pgt03um
	
	pgt05um= rcv[18] * 256 + rcv[19]
	p05=p05+pgt05um
	
	pgt10um= rcv[20] * 256 + rcv[21]
	p10=p10+pgt10um
	
	pgt25um= rcv[22] * 256 + rcv[23]
	p25=p25+pgt25um
	
	pgt50um= rcv[24] * 256 + rcv[25]
	p50=p50+pgt50um
	
	pgt100um= rcv[26] * 256 + rcv[27]
	p100=p100+pgt100um
	
	
	print("\nPM1.0 Standard:"+str(pm10std)+"\nPM2.5 Standard:"+str(pm25std)+"\nPM10.0 Standard:"+str(pm100std))
	print("\nPM1.0 Environmental:"+str(pm10env)+"\nPM2.5 Environmental:"+str(pm25env)+"\nPM10.0 Environmental:"+str(pm100env))
	print("\nParticles>0.3um per 0.1L air:"+str(pgt03um)+"\nParticles>0.5um per 0.1L air:"+str(pgt05um)+"\nParticles>1.0um per 0.1L air:"+str(pgt10um)+"\nParticles>2.5um per 0.1L air:"+str(pgt25um)+"\nParticles>5.0um per 0.1L air:"+str(pgt50um)+"\nParticles>10.0um per 0.1L air:"+str(pgt100um))
	c=c+1
	if c==70:
		doc={"sensor":"pms5003_2"}
		response=col.insert_one(doc)
		last_id=response.inserted_id
		print("\n")
		print(last_id)
		col.update_one({"_id":last_id},{"$set":{"time":datetime.now()}})
		col.update_one({"_id":last_id},{"$set":{"PM1,0_std":sp10std//c}})
		col.update_one({"_id":last_id},{"$set":{"PM2,5_std":sp25std//c}})
		col.update_one({"_id":last_id},{"$set":{"PM10,0_std":sp100std//c}})
		col.update_one({"_id":last_id},{"$set":{"PM1,0_env":sp10env//c}})
		col.update_one({"_id":last_id},{"$set":{"PM2,5_env":sp25env//c}})
		col.update_one({"_id":last_id},{"$set":{"PM10,0_env":sp100env//c}})
		col.update_one({"_id":last_id},{"$set":{"Particles>0,3um_per_0,1L_air":p03//c}})
		col.update_one({"_id":last_id},{"$set":{"Particles>0,5um_per_0,1L_air":p05//c}})
		col.update_one({"_id":last_id},{"$set":{"Particles>1,0um_per_0,1L_air":p10//c}})
		col.update_one({"_id":last_id},{"$set":{"Particles>2,5um_per_0,1L_air":p25//c}})
		col.update_one({"_id":last_id},{"$set":{"Particles>5,0um_per_0,1L_air":p50//c}})
		col.update_one({"_id":last_id},{"$set":{"Particles>10,0um_per_0,1L_air":p100//c}})
		print("\n\n\n\n\n\nI HAVE WRITTEN TO THE DATABASE!!!!!!!!")
		c=0
		sp10std=sp25std=sp100std=sp10env=sp25env=sp100env=0
		p03=p05=p10=p25=p50=p100=0
	
	
	
               
              
