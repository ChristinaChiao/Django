# class 類別(無實體): 紅豆餅模板、藍圖、設計圖
# -- 通常類別會是大寫，包含屬性(變數-int, float, list, str)和方法
# object物件(有實體): 紅豆餅、房子

#屬性：名詞、容器
#方法：動詞、行為、功能
class MyClass: # -->只是一個設計
  def __init__(self): #初始化方法
    self.text = 'ABC' #字串屬性
  def clear(self): #方法
    self.text = '' #清除text中的內容
    
    #-------------------         -------------------
    #|  class MyClass  |         |   object obj1   | 
    #-------------------  NEW--> -------------------
    #|ABC=text, clear()|         |ABC=text, clear()|
    #-------------------         -------------------
    
#_______________________________________________________#
obj1 = MyClass() # -->建立一個物件
print(f"text={obj1.text}")#取值，obj1=>text

#設定值：物件.屬性
obj1.text = 'DEF'
print(f"text={obj1.text}")
    #-------------------         -------------------
    #|   object obj1   |         |   object obj1   | 
    #-------------------  NEW--> -------------------
    #|ABC=text, clear()|         |DEF=text, clear()|
    #-------------------         -------------------

#方法使用：
obj1.clear() #呼叫方法
print(f"text={obj1.text}")
    #-------------------         -------------------
    #|   object obj1   |         |   object obj1   | 
    #-------------------  NEW--> -------------------
    #|DEF=text, clear()|         | text='', clear()|
    #-------------------         -------------------

#_______________________________________________________#  
class Student:
  def __init__(self):
    self.sno=" "  #屬性，學號
    self.sname =" " #屬性，姓名
  def iam(self): #方法，介紹自己
    print(f"My student number is {self.sno} and my name is {self.sname}")
    #-------------------        --------------------
    #|  class Student  |        |   object s1      | 
    #-------------------  NEW-->--------------------
    #|sno, sname, iam()|        |a0001, John, iam()|
    #-------------------        --------------------
  
s1 = Student() #建立物件
s1.sno = "a0001" #設定學號
s1.sname = "John" #設定姓名
s1.iam() #呼叫方法

s2 = Student()
s2.sno = "a0002"
s2.sname = "Alice" 
s2.iam()