import classmotor
import time

mymotor=classmotor.motor()

while True:
    print "antihorario"
    for i in range(0,530):
        if i%88==0:
            time.sleep(3)    
        mymotor.antihorario(0.005)
    
    #time.sleep(2)
    
    print "horario"
    for i in range(0,530):
        if i%88==0:
            time.sleep(3)
        mymotor.horario(0.005)

    #time.sleep(2)