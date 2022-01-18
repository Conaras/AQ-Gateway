import time
import serial
from datetime import datetime
from pymongo import MongoClient
connection_string="mongodb://makaronas:makaronask2022@150.140.193.156:27017/test?authSource=test&readPreference=primary"
client=MongoClient(connection_string)
dbi=client.get_database("makaronas")
col=dbi.get_collection("test_AQ")
file=open("measurements.csv","w")
ser = serial.Serial(
port='/dev/ttyUSB0',\
baudrate=9600,\
parity=serial.PARITY_NONE,\
stopbits=serial.STOPBITS_ONE,\
bytesize=serial.EIGHTBITS,\
timeout=1)
#ser.open()
i=0
j=0
d=0
c=0
e=0
file.write("PM1.0 Standard\tPM2.5 Standard\tPM10.0 Standard\tPM1.0 Environmental\tPM2.5 Environmental\tPM10.0 Environmental\tParticles > 0.3um / 0.1L air\tParticles > 0.5um / 0.1L air\tParticles > 1.0um / 0.1L air\tParticles > 2.5um / 0.1L air\tParticles > 5.0um / 0.1L air\tParticles > 10.0um / 0.1L air\n")
file.close()
count=0
p10s=p25s=p100s=p10e=p25e=p100e=0
p03=p05=p10=p25=p50=p100=0
print("connected to: " + ser.portstr)
print()
while True:
	
	line = ser.readline();
	if line:
    		#print(line)
    		pr=line.split()
    		if j==0:
    			#doc={"sensor":"pms5003_1"}
    			#response=col.insert_one(doc)
    			#last_id=response.inserted_id
    			#print(last_id)
    			j=1
    		#print(pr)
    		file=open("measurements.csv","a")
    		if len(pr)==3 and str(pr[2].decode('utf-8'))=="(standard)":
    			c=1
    		if len(pr)>3 and c==1:
    			if len(pr)==9:
    				file.write(str(pr[2].decode('utf-8'))+"\t"+str(pr[5].decode('utf-8'))+"\t"+str(pr[8].decode('utf-8'))+"\t")
    				
    				#col.update_one({"_id":last_id},{"$set":{"time":datetime.now()}})
    				if d==0:
    					#col.update_one({"_id":last_id},{"$set":{"PM1,0_std":str(pr[2].decode('utf-8'))}})
    					#col.update_one({"_id":last_id},{"$set":{"PM2,5_std":str(pr[5].decode('utf-8'))}})
    					#col.update_one({"_id":last_id},{"$set":{"PM10,0_std":str(pr[8].decode('utf-8'))}})
    					p10s=p10s+int(str(pr[2].decode('utf-8')))
    					p25s=p25s+int(str(pr[5].decode('utf-8')))
    					p100s=p100s+int(str(pr[8].decode('utf-8')))
    					d=1
    				else:
    					#col.update_one({"_id":last_id},{"$set":{"PM1,0_env":str(pr[2].decode('utf-8'))}})
    					#col.update_one({"_id":last_id},{"$set":{"PM2,5_env":str(pr[5].decode('utf-8'))}})
    					#col.update_one({"_id":last_id},{"$set":{"PM10,0_env":str(pr[8].decode('utf-8'))}})
    					p10e=p10e+int(str(pr[2].decode('utf-8')))
    					p25e=p25e+int(str(pr[5].decode('utf-8')))
    					p100e=p100e+int(str(pr[8].decode('utf-8')))
    					d=0
    				print(str(pr[2].decode('utf-8'))+"\t"+str(pr[5].decode('utf-8'))+"\t"+str(pr[8].decode('utf-8'))+"\t")
    				#print(pr)
    				
    				i+=1
    			elif len(pr)==7 and i!=0:
    				file.write(str(pr[6].decode('utf-8'))+"\t")
    				if e==0:
    					#col.update_one({"_id":last_id},{"$set":{"Particles>0,3um_per_0,1L_air":str(pr[6].decode('utf-8'))}})
    					#var=int(str(pr[6].decode('utf-8')))
    					#print(var)
    					p03=p03+int(str(pr[6].decode('utf-8')))
    					e=1
    				elif e==1:
    					#col.update_one({"_id":last_id},{"$set":{"Particles>0,5um_per_0,1L_air":str(pr[6].decode('utf-8'))}})
    					p05=p05+int(str(pr[6].decode('utf-8')))
    					e=2
    				elif e==2:
    					#col.update_one({"_id":last_id},{"$set":{"Particles>1,0um_per_0,1L_air":str(pr[6].decode('utf-8'))}})
    					p10=p10+int(str(pr[6].decode('utf-8')))
    					e=3
    				elif e==3:
    					#col.update_one({"_id":last_id},{"$set":{"Particles>2,5um_per_0,1L_air":str(pr[6].decode('utf-8'))}})
    					p25=p25+int(str(pr[6].decode('utf-8')))
    					e=4
    				elif e==4:
    					#col.update_one({"_id":last_id},{"$set":{"Particles>5,0um_per_0,1L_air":str(pr[6].decode('utf-8'))}})
    					p50=p50+int(str(pr[6].decode('utf-8')))
    					e=0
    				#print(str(pr[6].decode('utf-8'))+"\t")
    			elif len(pr)==8 and i!=0:
    				file.write(str(pr[7].decode('utf-8'))+"\t")
    				#print(str(pr[7].decode('utf-8'))+"\t")
    				#col.update_one({"_id":last_id},{"$set":{"Particles>10,0um_per_0,1L_air":str(pr[7].decode('utf-8'))}})
    				p100=p100+int(str(pr[7].decode('utf-8')))
    				j=0
    				count=count+1
    				if count==60:
    					doc={"sensor":"pms5003_1"}
    					response=col.insert_one(doc)
    					last_id=response.inserted_id
    					print(last_id)
    					col.update_one({"_id":last_id},{"$set":{"time":datetime.now()}})
    					col.update_one({"_id":last_id},{"$set":{"PM1,0_std":p10s//count}})
    					col.update_one({"_id":last_id},{"$set":{"PM2,5_std":p25s//count}})
    					col.update_one({"_id":last_id},{"$set":{"PM10,0_std":p100s//count}})
    					col.update_one({"_id":last_id},{"$set":{"PM1,0_env":p10e//count}})
    					col.update_one({"_id":last_id},{"$set":{"PM2,5_env":p25e//count}})
    					col.update_one({"_id":last_id},{"$set":{"PM10,0_env":p100e//count}})
    					col.update_one({"_id":last_id},{"$set":{"Particles>0,3um_per_0,1L_air":p03//count}})
    					col.update_one({"_id":last_id},{"$set":{"Particles>0,5um_per_0,1L_air":p05//count}})
    					col.update_one({"_id":last_id},{"$set":{"Particles>1,0um_per_0,1L_air":p10//count}})
    					col.update_one({"_id":last_id},{"$set":{"Particles>2,5um_per_0,1L_air":p25//count}})
    					col.update_one({"_id":last_id},{"$set":{"Particles>5,0um_per_0,1L_air":p50//count}})
    					col.update_one({"_id":last_id},{"$set":{"Particles>10,0um_per_0,1L_air":p100//count}})
    					print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"+"\n\n\n\n\n\n\n"+"I HAVE WRITTEN TO THE DATABASE"+"!!!!!!!!!!!!!!!!!!!!!"+"\n\n\n\n\n\n\n")
    					count=0
    					p10s=p25s=p100s=p10e=p25e=p100e=0
    					p03=p05=p10=p25=p50=p100=0
    				file.write("\n")
    				#time.sleep(10) 
    				file.close() 					
    				
ser.close()
   		
