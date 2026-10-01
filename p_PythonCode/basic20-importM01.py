import math_operation #建立好模型，在這邊import
math_operation.test() #使用方式：模型名稱math_operation.函數名稱
math_operation.test()
#2 
num1 = math_operation.mul(3, 4)
num2 = math_operation.add(5, 6)
num3 = math_operation.minus(10, 2)
num4 = math_operation.divide(2, 3)
print(f'num1 ={num1}, num2 ={num2}, num3 ={num3}, num4 ={num4}')

list_nums = math_operation.operation1(10, 5)
for data in list_nums:
  print(f"data = {data}")