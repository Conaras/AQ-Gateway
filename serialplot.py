import pandas as pd
import matplotlib.pyplot as plt
import csv

df=pd.read_csv('measurements.csv',sep='\t')
#df=df.astype(float)
#df[['PM1.0 Standard']].plot()
#plt.show()

plt.figure()



y1 = df['PM1.0 Standard']
y2 = df['PM2.5 Standard']
y3 = df['PM10.0 Standard']
y4 = df['PM1.0 Environmental']
y5 = df['PM2.5 Environmental']
y6 = df['PM10.0 Environmental']
y7 = df['Particles > 0.3um / 0.1L air']
y8 = df['Particles > 0.5um / 0.1L air']
y9 = df['Particles > 1.0um / 0.1L air']
y10 = df['Particles > 2.5um / 0.1L air']
y11 = df['Particles > 5.0um / 0.1L air']
y12 = df['Particles > 10.0um / 0.1L air']

x=range(len(y2))
for n in x:
	print(n)

plt.plot(x,y1,'-og',label="PM1.0 Standard")
plt.plot(x,y2,'-or',label="PM2.5 Standard")
plt.plot(x,y3,'-ob',label="PM10 STandard")
plt.plot(x,y4,'-om',label="PM1.0 Environmental")
plt.plot(x,y5,'-oy',label="PM2.5 Environmental")
plt.plot(x,y6,'-ok',label="PM10 Environmental")
plt.plot(x,y7,'-sc',label="Particles > 0.3um / 0.1L air")
plt.plot(x,y8,'-s',color='#3256a8',label="Particles > 0.5um / 0.1L air")
plt.plot(x,y9,'-s',color='#a84326',label="Particles > 1.0um / 0.1L air")
plt.plot(x,y10,'-s',color='#a88932',label="Particles > 2.5um / 0.1L air")
plt.plot(x,y11,'-s',color='#32a2a8',label="Particles > 5.0um / 0.1L air")
plt.plot(x,y12,'-s',color='#a86f32',label="Particles > 10.0um / 0.1L air")
plt.legend(loc='upper right')
plt.show()
