import pingo
import time

class motor:

    def __init__(self):
        self.board = pingo.detect.get_board() #MyBoard()
        self.pin1=self.board.pins[8]
        self.pin1.mode = pingo.OUT
        self.pin2=self.board.pins[9]
        self.pin2.mode = pingo.OUT
        self.pin3=self.board.pins[10]
        self.pin3.mode = pingo.OUT
        self.pin4=self.board.pins[11]
        self.pin4.mode = pingo.OUT

    def antihorario(self,t):
        #print "antihorario"
        self.pin1.hi()
        self.pin2.hi()
        self.pin3.lo()
        self.pin4.lo()
        time.sleep(t)
    
        self.pin1.lo()
        self.pin2.hi()
        self.pin3.hi()
        self.pin4.lo()
        time.sleep(t)

        self.pin1.lo()
        self.pin2.lo()
        self.pin3.hi()
        self.pin4.hi()
        time.sleep(t)

        self.pin1.hi()
        self.pin2.lo()
        self.pin3.lo()
        self.pin4.hi()
        time.sleep(t)

    def horario(self,t):
        #print "horario"
        self.pin1.hi()
        self.pin2.lo()
        self.pin3.lo()
        self.pin4.hi()
        time.sleep(t)

        self.pin1.lo()
        self.pin2.lo()
        self.pin3.hi()
        self.pin4.hi()
        time.sleep(t)

        self.pin1.lo()
        self.pin2.hi()
        self.pin3.hi()
        self.pin4.lo()
        time.sleep(t)

        self.pin1.hi()
        self.pin2.hi()
        self.pin3.lo()
        self.pin4.lo()
        time.sleep(t)
       

#while True:
   # for i in range(0,530):
      #  antihorario(0.005)
    #time.sleep(2)
    #for i in range(0,530):
       # horario(0.005)

