from flask import render_template, flash, redirect, request
from app import app
import threading,serial,time
received = {}
packet = []
send_flag = 0
loginflag = 0
send_order = ['Start','msgid','X','Y','Z','toolangle','WaterPump','VacuumPump','seedbox','calibrate']
Data = {'Start':11111,'msgid':0,'X':0, 'Y':0,'Z':0, 'tool':0,'WaterPump':0,'VacuumPump':0,'seedbox':2,'calibrate':3}
plant_details = []
msgid = 0

def comm():
   global send_flag,received
   while 1:
      time.sleep(0.01)
      if send_flag :
         if 'Plant' in received.keys():
            send_flag = 0
            print("Starting Planting sequence...")
            #plant(received)
         else:
            print("Flag set")
            send_flag = 0
            Data['msgid'] += 1
            for key,value in received.items():
               Data[key] = int(value)
            print(Data)

   '''
   ser = serial.Serial('COM7',115200)
   time.sleep(2)
   print("connected to: " + ser.portstr)
   ser.flush()
   while True:
      if send_flag:
         try:
            for val in data:
               string = str(val) + '\n'
               ser.write(string.encode('ascii'))
               x = ser.readline()
               print(x)
            
         except Exception as e:
            print(e)
         
         
      if ser.in_waiting > 10:
         x = ser.readline()
         print(x)
   '''
   
t = threading._start_new_thread(comm,())

def plant(vals):
   global Data
   for key,value in vals.items():
      if key is 'radio':
         plant_details[0] = value
   return Data
   

@app.route('/')
def login():
   return render_template('login.html')

@app.route('/validate',methods = ['POST'])
def validate():
    if request.method == 'POST':
        result = request.form
        if result['uname'] == 'admin' and result['psw'] == 'farmbot2019':
            loginflag = 1
            return redirect("/index", code=302)
        else:
            return redirect("/", code=302)
    return redirect("/login", code=302)

@app.route('/index') 
def controls():
   return render_template('index.html')

@app.route('/result',methods = ['POST'])
def result():
   global send_flag,received
   if request.method == 'POST':
      result = request.form
      received = result
      send_flag = 1
      print(result)
      return redirect("/index", code=302)
      #return render_template("result.html",result = result)

