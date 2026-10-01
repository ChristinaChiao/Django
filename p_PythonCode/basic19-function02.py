#1 0input, 0 output
def test():
  print("Hello World")

#2 多input, 1 output
def mul(x, y):
  return x * y
def add(x, y):
  return x + y
def minus(x, y):
  return x - y  
def divide(x, y):
  if y==0:
    return "除數不能為零"
  else:
    return  x / y  #return float(x)/float(y) 
#3 多input, 4 output
def operation1(x,y):
  mu1 = x*y
  add = x + y
  minus = x - y
  divide = x / y 
  return [add, minus, mu1, divide]

def operation1(x,y):
  mu1 = x*y
  add = x + y
  minus = x - y
  divide = x / y 
  return add, minus, mu1, divide
############################
#1 
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
#3-2
mu1, add, minus, divide = operation1(10, 5)
print(f"mu1 = {mu1}, add = {add}, minus = {minus}, divide = {divide} ")