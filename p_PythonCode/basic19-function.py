#f(x)=x**2+x+1 f(2)=2**2+2+1=7
#f(x,y)=x**2+y**2+1 f(2,3)=2**2+3**2+1=14

#宣告函數：建立跟使用
def f1(x): #x為區域變數，僅在函數內使用
    return x**2+x+1 #回傳東西，算式

def f2(x, y):
    return x**2+y**2+1
  
def f3(begin, end): #begin, end為區域變數
    sum = 0
    for i in range(begin, end+1):
        sum += i #sum = sum + i
    return sum
  
#################使用#####################
  
num1 = f1(2) #呼叫function名稱，先跑右邊
print(f'num1 = {num1}')

x = float(input('請輸入x值:'))
print('f1(x)的值為', f1(x))
y = float(input('請輸入y值:'))
print(f'f2(x, y)的值為= {f2(x, y)}')

num1 = f3(1 , 3)
print(f'1~3的總和為{num1}')