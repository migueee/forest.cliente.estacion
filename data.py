import pingo
import time
import httplib
import dht22

#declarar Estacion como variable 
estacion=1

board=pingo.detect.get_board()
MyDHT22=dht22.dht22()

pot=board.pins['A0']
pot.mode=pingo.ANALOG

pot2=board.pins['A1']
pot2.mode=pingo.ANALOG

connection = httplib.HTTPConnection("201.187.32.220")

def dir(pin):
	dir=float(pin.ratio()*70)
        if(dir>=53.04  and dir<=57): d=1 #print "N"
	if(dir>=10 and dir<=13.9): d=1 #print "N"
        if(dir>=13.91  and dir<17.82): d=2 #print "NE"
        if(dir>=17.82  and dir<25.66): d=3 #print "E"
        if(dir>=25.66 and dir<29.57): d=4 #print "SE"
        if(dir>=29.57  and dir<37.41): d=5 #print "S"
        if(dir>=37.41  and dir<41.32): d=6 #print "SO"
        if(dir>=41.32  and dir<49.13): d=7 #print "O"
        if(dir>=49.13 and dir<53.04): d=8 #print "NO"
        return d

def vel(pin):
        valor= format( float(pin.ratio()), '.4f')
        valor= int(float(valor)*10000)-1905
        velocidad=round((valor*40.3)/1905)
        
        #v=format( float(pin.ratio()), '.3f')
        #v= float(v)*1000
        #v= ( v-206)/4
        return int(velocidad)


#tomo 10 muestras de direccion y velocidad

array=[0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    d=dir(pot)
    array[i]=vel(pot2)
    time.sleep(0.5)
        
array.sort()
v=array[9]

#obtener temperatura y humedad
temp=0
hum=0
while temp!=0 and hum!=0:
    temp=MyDHT22.temperature()
    hum=MyDHT22.humidity()
    time.sleep(2)
    
temp="%.0f"%temp
hum="%.0f"%hum

#fecha y hora
fecha=time.strftime('%d-%m-%y')
hora=time.strftime('%H:%M:%S')
h=hora.split(':')
hora= int(h[0])*240 +int(h[1])*4
if(h[2]>=0 and h[2]<15):hora+=0
if(h[2]>=15 and h[2]<30):hora+=1
if(h[2]>=30 and h[2]<45):hora+=2
if(h[2]>=45 and h[2]<60):hora+=3

connection.request("GET","/WS/service.php?user=migue&option=save_"+str(estacion)+"_"+str(temp)+"_"+str(hum)+"_"+str(hora)+"_"+str(fecha)+"_1_"+str(v)+"_"+str(d))
#connection.request("GET","/WS/service.php?user=migue&option=save_5_50_90_1_20-08-2015_10_81_1")

response=connection.getresponse()
data=response.read()
connection.close()

print data








