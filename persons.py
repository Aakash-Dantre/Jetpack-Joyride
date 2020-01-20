import math
from colorcode import color

class person:
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self.__velx=0
		self.__vely=0
		self.dr=0
	def printp(self,sh):
		xp=math.floor(self.__x) 
		yp=math.floor(self.__y)
		if sh:
			print(color.CYAN+color.BOLD+"\033[{};{}f (  ^@  )".format(yp,xp))	
			print(color.RED+"\033[{};{}f (  \"|  )".format(yp+1,xp)+color.END)			
		else:
			print(color.CYAN+color.BOLD+"\033[{};{}f ^@".format(yp,xp))	
			print(color.RED+"\033[{};{}f \"|".format(yp+1,xp)+color.END)	
		
				
	def updatex(self):
		self.__x+=self.__velx
		self.__y+=self.dr	
	def update(self):
		self.__x+=self.__velx
		self.__vely+=0.05
		self.__y+=self.__vely
		if(self.__vely> 1.5):self.__vely=1.5
		if(self.__vely<-1.2):self.__vely=-1.2
		if(self.__y<=4):
			self.__y=4
			self.__velx=0
			self.__vely=0
		if(self.__y>=40):
			self.__velx=0
			self.__y=40
			self.__vely=0
		if(self.__x<1):
			self.__x=1
			self.__velx=1
			self.__vely=0
		if(self.__x>=140):
			self.__x=140
			self.__velx=0
			self.__vely=0

	def upy(self,ch):
		self.__vely+=ch		

	def upx(self,ch):
		self.__velx+=ch

	def getx(self):
		return self.__x
	def gety(self):
		return self.__y
	
class boss:
	def __init__(self):
		self.__y=20
	def update(self,dir):
		if dir:
			self.__y += 0.1
		else:
			self.__y -= 0.1
		if self.__y<5:
			self.__y=5
		if self.__y>35:
			self.__y=35	
	def printb(self):
		yp=math.floor(self.__y)
		# print("\033[{};{}f ^@".format(yp,95))	
		# print("\033[{};{}f \"|".format(yp+1,95))				
		print(color.GREEN+color.BOLD+"""\033[{};7f 
 												/\_/\ / (_
 												(0 0)//  (_
 												(oo)/ -- _(
												,__//\ \ _(
												;--   \ _(
												((  ) )    .*
												z(____)...'     """.format(yp)+color.END)



	def gety(self):
		return self.__y