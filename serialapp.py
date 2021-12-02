import time
import serial
file=open("measurements.csv","a")
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
c=0
print("connected to: " + ser.portstr)
print()
file.write("\n")
while True:
	line = ser.readline();
	if line:
    		#print(line)
    		pr=line.split()
    		print(pr)
    		if len(pr)==3 and str(pr[2].decode('utf-8'))=="(standard)":
    			c=1
    		if len(pr)>3 and c==1:
    			if len(pr)==9:
    				file.write(str(pr[2].decode('utf-8'))+"\t"+str(pr[5].decode('utf-8'))+"\t"+str(pr[8].decode('utf-8'))+"\t")
    				print(pr)
    				i+=1
    			elif len(pr)==7 and i!=0:
    				file.write(str(pr[6].decode('utf-8'))+"\t")
    				
    			elif len(pr)==8 and i!=0:
    				file.write(str(pr[7].decode('utf-8'))+"\t")
    				file.write("\n") 
ser.close()
file.close()    		
