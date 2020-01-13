import math
from colorcode import color

class person:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.velx=0
		self.vely=0
		self.dr=0
	def printp(self,sh):
		xp=math.floor(self.x) 
		yp=math.floor(self.y)
		if sh:
			print(color.CYAN+"\033[{};{}f (  ^@  )".format(yp,xp))	
			print(color.RED+"\033[{};{}f (  \"|  )".format(yp+1,xp)+color.END)			
		else:
			print(color.CYAN+"\033[{};{}f ^@".format(yp,xp))	
			print(color.RED+"\033[{};{}f \"|".format(yp+1,xp)+color.END)	
		
				
	def updatex(self):
		self.x+=self.velx
		self.y+=self.dr	
	def update(self):
		self.x+=self.velx
		self.vely+=0.05
		self.y+=self.vely
		if(self.vely> 1.5):self.vely=1.5
		if(self.vely<-1.2):self.vely=-1.2
		if(self.y<=4):
			self.y=4
			self.velx=0
			self.vely=0
		if(self.y>=40):
			self.velx=0
			self.y=40
			self.vely=0
		if(self.x<1):
			self.x=1
			self.velx=1
			self.vely=0
		if(self.x>=140):
			self.x=140
			self.velx=0
			self.vely=0



class boss():
	def __init__(self):
		self.y=20
	def update(self,dir):
		if dir:
			self.y += 0.1
		else:
			self.y -= 0.1
		if self.y<5:
			self.y=5
		if self.y>35:
			self.y=35	
	def printb(self):
		yp=math.floor(self.y)
		print("\033[{};{}f ^@".format(yp,100))	
		print("\033[{};{}f \"|".format(yp+1,100))				

