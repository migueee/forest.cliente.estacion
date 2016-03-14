import MypcDuinoIO
import time
from fractions import Fraction

class dht22:
	
	def read(self,pin,retries):
		mypin=pin
		mytries=retries
		if mytries==0:
			x=self.getdht22(mypin)
		elif mytries<0:
			x=1
			while x>0:
				x=self.getdht22(mypin)
		elif mytries>0:
			for i in range(0,mytries):
				x=self.getdht22(mypin)
				if x==0:
					break
				else:
					time.sleep(0.1)
		return x
					
	def getdht22(self,pin):
		myerror=0
		testpin=pin
		Mybits=''
		Mylist=[]
		count=1
		MyPin = MypcDuinoIO.pin(testpin,1)
		MyPin.low()
		time.sleep(0.0006)
		MyPin.setmode(0)
		for i in range(0,41):
			while MyPin.state()==0:
				pass
			while (MyPin.state()==1 and count<20):
				count += 1
			if count>=20:
					myerror=1
					break
			if count>2:
				Mylist.append('1')
			else:
				Mylist.append('0')
			count=1
		Mybits=''.join(Mylist)
		if len(Mybits)<41:
			self.tempc=0
			self.humid=0
			return 3
		temp=int(Mybits[1:17],2)+int(Mybits[18:33],2)
		if temp>255:
			temp=temp-256
		crc=int(Mybits[33:41],2)
		if temp==crc:
			myerror=0
		else:
			myerror=2
		MyTemp=int(Mybits[18:33],2)
		if MyTemp>32767:
			MyTemp=32768-MyTemp
		self.tempc=MyTemp/10.0
		self.humid=int(Mybits[1:17],2)/10.0
		return myerror
		
	def temperature(self):
		return self.tempc
		
	def humidity(self):
		return self.humid

	def dewpoint(self):
		expo=Fraction('1/8')
		temp=(self.humid/100)**expo
		temp2=temp*(112+(0.9*self.tempc))+(0.1*self.tempc)-112
		return "%.2f"%temp2
