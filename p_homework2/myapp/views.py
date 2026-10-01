from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse("hello") 
#在urls.py裡面設定頁面，就要回傳東西，不管是文字或是頁面

def homework2(request,username):
  print(f"Hello {username}")
  return render(request, "show.html", locals())
#local將全部變數傳給html

def lotto1(request,username):
  import random
  num = random.sample(range(1,6),5) 
  #產生1~6不重複的亂數
  return render(request, "lotto1.html", {"username": username, "num": num})

def lotto2(request):
  import random
  # num1 = random.sample(range(1,42),5) 
  # num2 = random.sample(range(1,42),5) 
  # num3 = random.sample(range(1,42),5) 
  # num4 = random.sample(range(1,42),5) 
  # num5 = random.sample(range(1,42),5) 
  # num6 = random.sample(range(1,42),5) 
  
  num1, num2, num3, num4, num5, num6 = [random.sample(range(1, 42), 5) for _ in range(6)]
  
  num = [num1, num2, num3, num4, num5, num6]
  return render(request, "lotto2.html", locals())


def lotto3(request):
  random_num_lists = [] #產生一個空集合
  import random
  for i in range(1, 7):
      num_list = random.sample(range(1, 43), 6)
      num_list.sort()  # 將每組號碼小到大排序
      # num_list = sorted(num_list)  # 或者使用 sorted() 函數進行排序
      random_num_lists.append(num_list)
      print(random_num_lists)
  return render(request, "lotto3.html", {"random_num_lists": random_num_lists})