from math_operation import test, mul, add, minus, divide, operation1
test()
test()
#2 
num1 = mul(3, 4)
num2 = add(5, 6)
num3 = minus(10, 2)
num4 = divide(2, 3)
print(f'num1 ={num1}, num2 ={num2}, num3 ={num3}, num4 ={num4}')
#3-1
list_nums = operation1(10, 5)
for data in list_nums:
  print(f"data = {data}")