# AQ-Gateway
## Implementation of an Air Quality monitoring system
##### This is a guide for an Air Quality monitoring system. The archtecture of the system is shown <a href="https://www.dropbox.com/s/tpa260gga2w65ue/sundesmologia.jpg?dl=0">here</a>.
<ul>
<li>The sensor we use is the PMS5003 digital and universal particle concentration sensor.</li> 
<li>To get the measures from the sensor we use the STM32L072Z microcontroller which is programmed via the Mbed Studio.The code(pms5003.cpp) and the header(pms5003.h) used to program the microcontroller come from repositories that can be found <a href="https://github.com/janjongboom/mbed-pms5003">here</a> (Github) or <a href="https://os.mbed.com/users/janjongboom/code/pms5003/">here</a> (MbedOS).</li>
<li>The Digi Xbee 3 Wireless Protocol is used to transmit the data from the sensor to the receiver so that they can be monitored and handled remotely. The Xbee router is connected to the microcontroller through UART(in order for the data to be forwarded correctly we  connect rx->rx and tx->tx) and the measurements are being sent to the Xbee coordinator that is connected to a remote computer through a serial port (usb).</li>
<li>The program serial.py is used to read the serial output from the Xbee coordinator and write the values to a csv file called measurements.csv</li>
<li>The program serialapp.py can be used to append more measurements to an already existing file.</li>
<li>serialplot.py is used to visualize the measurements.</li>
<li>serialplotrt.py is used to visualize the measurements in real time but if you want real time visualization you have to use serial2.py to store the data.</li>
<li>serail2.py also uploads the measurements to a MongoDB Database.</li>




</ul>
