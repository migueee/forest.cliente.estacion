import os
import time
import sys
import httplib
import classmotor

mymotor=classmotor.motor()
 
start = 0
end = 8640
estacion=1
folder='forestin_1'
 
#print "Comienza el script....durante 24 Horas"

def captura():
    print "Capturando imagen"
   
    fecha=time.strftime('%d-%m-%y')
    hora=time.strftime('%H:%M:%S')
    img=time.strftime('%d%m%y')+"-"+time.strftime('%H%M%S')+".jpg"
    
    #name = time.strftime("%d%m%y_%H%M%S")+".jpg" 
    os.system("fswebcam -i 0 -d /dev/video0 -r 640x480 -p YUYV -q --title @AlexCorvis84  /home/ubuntu/fotos/"+folder+"/"+img)
    
    time.sleep(1)
    os.system("/home/ubuntu/fotos/./dropbox_uploader.sh upload /home/ubuntu/fotos/"+folder+"/"+img+" "+folder+"/"+img)

    connection = httplib.HTTPConnection("201.187.32.220")

    print "guardando direccion de  imagen en servidor"
    connection.request("GET","/WS/service.php?user=migue&option=img_save_"+folder+"/"+img+"_"+str(fecha)+"_"+str(hora)+"_"+str(estacion))
    response=connection.getresponse()
    data=response.read()
    connection.close() 

    #os.system("python data.py")
    print "eliminando imagen local" 
    rm="rm "+folder+"/"+img
    os.system(rm)
    time.sleep(2)    



while start < end:   
    for i in range(0,530):
        if i%88==0:
            captura()
        mymotor.antihorario(0.005)
        
    for i in range(0,530):
        if i%88==0:
            captura()
        mymotor.horario(0.005)
    
    # despues un ciclo horario y antihorario se enviaran los datos
    #aproximadamente cada 2 minutos
    os.system("python data.py")
    start = start+1

    print "Proceso TIMELAPSE finalizado. Turno para editar el video"
sys.exit()
