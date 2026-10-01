class A:
  x=[] #類別屬性，所有物件共享同一個列表，靜態屬性
a1 = A()
a2 = A()
a1.x.append(1) #append 1 to the list
a2.x.append(2) #append 2 to the list
print(a1.x) 
print(a2.x) 
    #-------------        -------------------
    #|  class A  |        |  object a1 ->x  | 
    #------------- 共同-->-------------------- -->[1, 2]
    #                     |  object a2 ->x  | 
    #                     -------------------
  
##################################
class B:
  def __init__(self):
    self.y=[] #實例屬性，每個物件都有自己的列表

b1 = B()
b2 = B()
b1.y.append(1) #append 1 to the list
b2.y.append(2) #append 2 to the list
print(b1.y)
print(b2.y)

    #-------------        -------------------
    #|  class B  |        |  object b1 ->y  | -->[1]
    #------------- 各自-->-------------------- 
    #                     |  object b2 ->y  | -->[2]
    #                     -------------------
  