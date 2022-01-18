import serial, time, struct, csv, os
from pymongo import MongoClient
from datetime import datetime
from usbiss.spi import SPI
import opc
from opc import OPCR1
#import opc_r1
from time import sleep

def logfilename():
    #now = datetime.datetime.now()
    return 'OPC_R1'
    # \
     #           (now.year, now.month, now.day,
      #           now.hour, now.minute, now.second)


try:
    path = str(os.environ['outputPath_opc'])
except:
    print("could not find env variable ")
    path = ""

debug = 1
writeLog = 1


# Build the connector
#spi = SPI("COM22")
spi = SPI("/dev/ttyACM0")

print("------------------------------------")
print("open serial port and connect to SPIt")
print("------------------------------------")
connection_string="mongodb://makaronas:makaronask2022@150.140.193.156:27017/test?authSource=test&readPreference=primary"
client=MongoClient(connection_string)
dbi=client.get_database("makaronas")
col=dbi.get_collection("test_AQ")
# Set the SPI mode and clock speed
spi.mode = 1
spi.max_speed_hz = 500000
alpha = OPCR1(spi, firmware=[17,0])


print(alpha.read_firmware)

sleep(1)

sleep(5)

#alpha.toggle_fan(True)
IsOn = False
while IsOn is False:
    IsOn = alpha.toggle_Peripheral(True)
    print("the opc is now " + str(IsOn))
    sleep(0.5)

sleep(5)


print("------------------------------------")
print("create csv file")
print("------------------------------------")

if writeLog:

    csv_file = os.path.join(path, logfilename())
    csv_file = open(csv_file, mode='w')

    fieldnames = ["PM1", "PM2.5", "PM10","Temperature","Relative humidity"]


    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    csv_file.flush()


print("------------------------------------")
print("starting reading loop")
print("------------------------------------")
p10=p25=p100=pt=prh=0
c=0
sleep(2)
buffer = []
readLoop = True
index = 0

while readLoop:

    data = alpha.histogram()

    if debug and len(data) != 0:
        # read the information string
        #print(repr(alpha.read_info_string()))
        # Read the histogram
        #print(data)
        #print(len(data))
    	sleep(0.5)

    index += 1

    if writeLog and len(data) != 0:

        if debug: print("writing data to csv file!")

        writer.writerow({'Temperature':data["Temperature"], 'Relative humidity':data['Relative humidity'],'PM1':data["PM1"], 'PM2.5':data["PM2.5"], 'PM10':data["PM10"]})


        csv_file.flush()
        #print(data["PM1"])
        p10=p10+data["PM1"]
        p25=p25+data["PM2.5"]
        p100=p100+data["PM10"]
        pt=pt+data["Temperature"]
        prh=prh+data["Relative humidity"]
        c=c+1
        print(data["PM2.5"])
        print(data["PM10"])
        print(data["Temperature"])
        print(data['Relative humidity'])
        print(c)
        #doc={"sensor":"OPC-R1"}
        #response=col.insert_one(doc)
        #last_id=response.inserted_id
        print("\n")
        if c==45:
        	doc={"sensor":"OPC-R1"}
        	response=col.insert_one(doc)
        	last_id=response.inserted_id
        	print(last_id)
        	col.update_one({"_id":last_id},{"$set":{"time":datetime.now()}})
        	col.update_one({"_id":last_id},{"$set":{"PM1,0_env":p10/c}})
        	col.update_one({"_id":last_id},{"$set":{"PM2,5_env":p25/c}})
        	col.update_one({"_id":last_id},{"$set":{"PM10,0_env":p100/c}})
        	col.update_one({"_id":last_id},{"$set":{"Temperature":pt/c}})
        	col.update_one({"_id":last_id},{"$set":{"Relative_humidity":prh/c}})
        	print("\n\n\n\n\n\nI HAVE WRITTEN TO THE DATABASE!!!!!!!!")
        	p10=p25=p100=pt=prh=c=0
    if index == 60*45*2:
        readLoop = False


# Turn the device off
alpha.off()

