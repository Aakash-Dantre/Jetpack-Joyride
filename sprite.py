import math
from colorcode import color

class sprite:
	def __init__(self,x,y,ch):
		self.__x=x
		self.__y=y
		self.valid=1
		self.ch=ch
	def printsp(self,co):
		ch=self.ch
		xp=math.floor(self.__x) 
		yp=math.floor(self.__y)
		print(co+"\033[{};{}f {}".format(yp,xp,ch)+color.END)	
	def upd(self,dx,dy):
		self.__x+= dx
		self.__y+= dy
	def getx(self):
		return self.__x
	def gety(self):
		return self.__y

class spr(sprite):
	def __init__(self,x,y,ch):
		sprite.__init__(self,x,y,ch)
		
	def update(self,sp):
		self.upd(-sp,0)
		xc=self.getx()
		if xc<=3:
			self.valid=0
class bull(sprite):
	def __init__(self,x,y,vx,vy,ch):
		sprite.__init__(self,x,y,ch)
		self.vx=vx
		self.vy=vy
	def update(self):
		self.upd(-self.vx,-self.vy)	
		xc=self.getx()
		yc=self.gety()
		self.vy-=0.07
		if xc<=3:
			self.valid=0
		if yc>35 or yc <3:
			self.valid=0

class dragon(sprite):
	def __init__(self,x,y,ch):
		sprite.__init__(self,x,y,ch)
		
	def update(self):
		self.upd(-1,0)
		xc=self.getx()
		if xc<0:
			self.valid=0
	

class magnets(sprite):
	def __init__(self,x,y,ch):
		sprite.__init__(self,x,y,ch)
		
	def update(self,sp):
		self.upd(-sp,0)
		xc=self.getx()
		if xc<0:
			self.valid=0
	
