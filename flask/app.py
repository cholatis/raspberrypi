from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, jsonify

############## GPIO ##################
from gpiozero import Servo
from time import sleep
 
myGPIO=17
myGPIO2=27

myCorrection=0
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
# Move Up-Down
servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

# Move Left-Right
servo2 = Servo(myGPIO2,min_pulse_width=minPW,max_pulse_width=maxPW)

############### GPIO #################
def mymove(axis, value):
    if(value == 0 or value == 20):
        #do nothing
        print("do nothing "+axis+" "+str(value))
    else:
        if axis == "l":
            value = float(value) + 1
            value2=(float(value)-10)/10 # This formula for range 0 to 20 and calculate to -1 to 1 value
            servo2.value = value2
            print(axis + " " +str(value2))
            sleep(0.5)
        elif axis == "r":
            value = float(value) - 1
            value2=(float(value)-10)/10
            servo2.value = value2
            print(axis + " " +str(value2))
            sleep(0.5)
        elif axis == "u":
            value = float(value) + 1
            value2=(float(value)-10)/10
            servo.value = value2
            print(axis + " " +str(value2))
            sleep(0.5)
        elif axis == "d":
            value = float(value) - 1
            value2=(float(value)-10)/10
            servo.value = value2
            print(axis + " " +str(value2))
            sleep(0.5)

    print(value)
    return value
        


BASE_URL = ''

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('./json.html')

@app.route('/addnumber')
def addnumber():
    return render_template('./addnumber.html')

@app.route('/leftright')
def leftright():
    return render_template('./leftright.html')

@app.route('/servomove')
def servomove():
    return render_template('./servomove.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type = int)
    b = request.args.get('b', 0, type = int)
    print(str(a+b))
    return jsonify(result = a + b)

@app.route('/moveleft')
def moveleft():
    tmpmovelr = request.args.get('movelr', 0, type = str)
    print(tmpmovelr)
    return jsonify(movelr=mymove("l", tmpmovelr))

@app.route('/moveright')
def moveright():
    tmpmovelr = request.args.get('movelr', 0, type = str)
    print(tmpmovelr)
    return jsonify(movelr=mymove("r", tmpmovelr))

@app.route('/moveup')
def moveup():
    tmpmoveud = request.args.get('moveud', 0, type = str)
    print(tmpmoveud)
    return jsonify(moveud=mymove("u", tmpmoveud))

@app.route('/movedown')
def movedown():
    tmpmoveud = request.args.get('moveud', 0, type = str)
    print(tmpmoveud)
    return jsonify(moveud=mymove("d", tmpmoveud))
