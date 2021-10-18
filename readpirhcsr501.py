import time #sleep
import sys #exit
import signal #signal
import server
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.OUT) 
GPIO.setup(16, GPIO.IN) 
GPIO.setwarnings(False)
 
while (True):
    if(GPIO.input(16) == 1):
       GPIO.output(12,0) 
       print("algo foi detectado!")
    else: 
       GPIO.output(12,1)

      def signal_handler(signal, frame):
    app.exit()

class App():
    def __init__(self):
        print("Projeto Integrado VII")
        signal.signal(signal.SIGINT, signal_handler)
            
        self.server = server.Server()   
        self.server.onCmd = self.onCmd

        while True:
            print("AR Condicionado ligado")  
			self.server.send(arcondicionado)
    
    def onCmd(self, cmd):
        if cmd[0:3] == "log":
            self.server.log = True if cmd[3:4] == "1" else False       
        elif cmd[0] == "v":
            time.sleep(900)   
			print("Ar Condicionado Desligado")   
            self.server.send(arcondicionado)       
        
    def exit(self):
        print("\rYou pressed Ctrl+C!")
        self.server.exit()
        sys.exit(0)
        
if __name__ == '__main__':
    app = App()
