class SmallMath:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def add(self):
    return self.x + self.y

  def subtract(self):
    return self.x - self.y

  def multiply(self):
    return self.x * self.y

  def divide(self):
    if self.y != 0:
      return self.x / self.y
    else:
      return None
    
s = SmallMath(10, 5)#將10和5傳入SmallMath類別，建立一個物件化s
print(s.add())
print(s.subtract())
print(s.multiply())
print(s.divide())

    #---------------------------               -----------------------------
    #|    class SmallMath      |               |          object s         |
    #---------------------------    物件化      -----------------------------
    #|  x, y, add, subtract,   |  傳入x,y值 --> |  x=10, y=5, add, subtract |
    #|   multiply, divide      |               |      multiply, divide     |
    #---------------------------               ------------------------------
  

