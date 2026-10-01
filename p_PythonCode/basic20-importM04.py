import math_operation as m  #建立好模型，在這邊import
m.test() 
m.test()
#2 
num1 = m.mul(3, 4)
num2 = m.add(5, 6)
num3 = m.minus(10, 2)
num4 = m.divide(2, 3)
print(f'num1 ={num1}, num2 ={num2}, num3 ={num3}, num4 ={num4}')

list_nums = m.operation1(10, 5)
for data in list_nums:
  print(f"data = {data}")