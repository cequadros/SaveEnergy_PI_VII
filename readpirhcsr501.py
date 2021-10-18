import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.OUT) 
GPIO.setup(16, GPIO.IN) 
 
while (True):
    if(GPIO.input(16) == 1):
       GPIO.output(12,0) 
       print("algo foi detectado!")
    else: 
       GPIO.output(12,1)
