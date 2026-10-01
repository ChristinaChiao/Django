class Animal:
  def __init__(self, name): #初始化方法，建構方法/建構子/constructor
    self.name = name
  def fly(self): #一般方法
    print(f"{self.name} is flying.")
    
class Bird(Animal): #繼承自Animal類別，不夠可以新增屬性或方法，可以同名覆蓋父類別的東西
  def __init__(self, name): #初始化方法，建構方法/建構子/constructor
    self.name = "red" + name
  def sing(self):  #一般方法
    print(f"{self.name} is singing.")
    
class Bird2(Animal): #繼承自Animal類別
    def mymethod(self):
      print("Hello")
      
print("..........1...........")
p1 = Bird("parrot")
print(p1.name)
p1.fly()
p1.sing() 

print("..........2...........")
p2 = Bird2("sparrow")
print(p2.name)
p2.fly()
p2.mymethod()