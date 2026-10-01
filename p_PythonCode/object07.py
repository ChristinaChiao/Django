#super用於呼叫父類別的方法或建構方法
#coding=utf-8

class Father:
	def __init__(self):
		  self.x = 50
	def printInfo(self):
		  print(f"父類別方法：x={self.x}")

class Child(Father):
	def __init__(self):
		  super().__init__() #呼叫父類別的__init__方法，繼承self.x=50
		  self.x = 100 #子類別自己的屬性
  
	def printInfo(self):
  		super().printInfo() #呼叫父類別的printInfo方法
      print(f"子類別方法：y={self.y}")
		
C = Child()
C.printInfo()
