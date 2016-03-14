import os

class pin:
	GPIO_MODE_PATH= os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
	GPIO_PIN_PATH=os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
	GPIO_FILENAME="gpio"
	thepin=''

	def __init__(self,mypin,mode):
		self.gpio=mypin
		self.mode=mode
		self.pinMode=(os.path.join(self.GPIO_MODE_PATH, 'gpio'+str(self.gpio)))
		self.pinData=(os.path.join(self.GPIO_PIN_PATH, 'gpio'+str(self.gpio)))
		file=open(self.pinMode,'r+')
		file.write(str(self.mode))
		file.close
		self.file=open(self.pinData,'r+',0)
		
	def high(self):
		self.file.write("1")
		self.thepin=1
		
	def low(self):
		self.file.write("0")
		self.thepin=0
	
	def toggle(self):
		if self.thepin==0:
			self.high()
		else:
			self.low()
	
	def state(self):
		self.file.seek(0)
		return int(self.file.read(1))
		
	def setmode(self,x):
		self.mode=x
		file2=open(self.pinMode,'r+')
		file2.write(str(self.mode))
		file2.close
			
	def __del__(self):
		self.file.close
		
class adc:
	ADC_PATH=os.path.normpath('/proc/')
	raw=0
	
	def __init__(self,pin):
		self.adc=pin
		if self.adc==0 or self.adc==1:
			self.adcMult=2/62
		else:
			self.adcMult=3.3/4095
		self.adcData=(os.path.join(self.ADC_PATH, 'adc'+str(self.adc)))
		self.file=open(self.adcData,'r')
		
	def raw(self):
		self.file.seek(0)
		value=self.file.read(9)
		value=int(value[5:len(value)])
		return value
		
	def volts(self):
		self.file.seek(0)
		value=self.file.read(9)
		value=int(value[5:len(value)])
		if value==0:
			return 0
		else:
			return '%.4f'%(value*self.adcMult)
		
	def __del__(self):
		self.file.close	
