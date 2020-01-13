import math
from colorcode import color

class sprite:
	def __init__(self,x,y,ch):
		self.x=x
		self.y=y
		self.valid=1
		self.ch=ch
	def printsp(self,co):
		ch=self.ch
		xp=math.floor(self.x) 
		yp=math.floor(self.y)
		print(co+"\033[{};{}f {}".format(yp,xp,ch)+color.END)	


class spr(sprite):
	def __init__(self,x,y,ch):
		sprite.__init__(self,x,y,ch)
		
	def update(self,sp):
		self.x-=sp
		if self.x<=3:
			self.valid=0
class bull(sprite):
	def __init__(self,x,y,vx,vy,ch):
		sprite.__init__(self,x,y,ch)
		self.vx=vx
		self.vy=vy
	def update(self):
		self.x-=self.vx
		self.y-=self.vy	
		if self.x<=3:
			self.valid=0
		if self.y>35 or self.y <3:
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
	
