from time import sleep
from os import system
import math
class person:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.velx=0
		self.vely=0
		self.dr=0
	def printp(self):
		xp=math.floor(self.x) 
		yp=math.floor(self.y)
		print("\033[{};{}f m".format(yp,xp))	
	def updatex(self):
		self.x+=self.velx
		self.y-=self.dr	
	def update(self):
		self.x+=self.velx
		self.vely+=0.05
		self.y+=self.vely
		if(self.vely> 1.5):self.vely=1.5
		if(self.vely<-1.5):self.vely=-1.5
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


class sprite:
	def __init__(self,x,y,ch):
		self.x=x
		self.y=y
		self.valid=1
		self.ch=ch
	def printsp(self):
		ch=self.ch
		xp=math.floor(self.x) 
		yp=math.floor(self.y)
		print("\033[{};{}f {}".format(yp,xp,ch))	


class spr(sprite):
	def __init__(self,x,y,ch):
		sprite.__init__(self,x,y,ch)
		
	def update(self,sp):
		self.x-=sp
		if self.x<=3:
			self.valid=0
	
class dragon(sprite):
	def __init__(self,x,y,ch):
		sprite.__init__(self,x,y,ch)
		
	def update(self):
		self.x-=1
		if self.x<0:
			self.valid=0
	


class magnets(sprite):
	def __init__(self,x,y,ch):
		sprite.__init__(self,x,y,ch)
		
	def update(self,sp):
		self.x-=sp
		if self.x<0:
			self.valid=0
	
