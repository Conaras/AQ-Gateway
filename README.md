# AQ-Gateway
## Implementation of an Air Quality monitoring system
This is a guide for an Air Quality monitoring system. The archtecture of the system can be found <a href="https://www.dropbox.com/s/tpa260gga2w65ue/sundesmologia.jpg?dl=0">here</a>.
<ul>
<li>The sensor we use is the PMS5003 digital and universal particle concentration sensor.</li> 
<li>To get the measures from the device we use the STM32L072Z microcontroller which is programmed via the Mbed Studio. </li>
The code(pms5003.cpp) and the header(pms5003.h) used to program the microcontroller come from repositories that can be found <a href="https://github.com/janjongboom/mbed-pms5003">here</a> (Github) or <a href="https://os.mbed.com/users/janjongboom/code/pms5003/">here</a> (MbedOS)</li>
<li>The program serial.py is used to read the serial output from the Xbee coordinator and write the values to a csv file called measurements.csv</li>
<li>The program serialapp.py can be used to append more measurements to an already existing file.</li>





</ul>
