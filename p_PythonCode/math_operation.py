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
    return  x / y  
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