# -*- coding: utf-8 -*-
"""

Spyder Editor



This is a temporary script file.
"""
    
import serial,time
import threading 
  


    
Data = {'Start':11111,'msgid':12,'X':2310, 'Y':112,'Z':0, 'toolangle':10,'WaterPump':0,'VacuumPump':0,'seedbox':2,'calibrate':0}
sendlist = [Data['Start'],Data['msgid'],Data['X'],Data['Y'],Data['Z'],Data['toolangle'],Data['WaterPump'],Data['VacuumPump'],Data['seedbox'],Data['calibrate']]


ser = serial.Serial('COM7',9600)
time.sleep(2)
print("connected to: " + ser.portstr)
ser.flush()




try:
    for val in sendlist:
        string = str(val) + '\n'
        ser.write(string.encode('ascii'))
        x = ser.readline()
        print(x)
        
except Exception as e:
    print(e)
    
while 1:
    if ser.in_waiting > 10:
        x = ser.readline()
        print(x)
    
ser.close()
