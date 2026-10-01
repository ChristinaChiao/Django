from django.shortcuts import render
from django.http import HttpResponse

def index01(request):
  return HttpResponse("<b>Hello World 22</b>")
 # 字串回傳"Hello World 22"粗體(b)
 
def hello(request):
  return HttpResponse("Hello")

def helloName1(request,username):
  print(username)
  return HttpResponse(f"<b>Hello {username}</b>")
def helloName2(request, username1, username2):
    # print(username1), print(username2)
    return HttpResponse("Hello "+ username1 + " "+username2)
  
from datetime import datetime
def timePage(request,username):
  print(f"Hello {username}")
  now = datetime.now()
  print(f"現在時間: {now}")
  #return HttpResponse("Hello")
  return render(request, "timePage.html", locals())

def timePageCss(request,username):
  print(f"Hello {username}")
  now = datetime.now()
  print(f"現在時間: {now}")
  return render(request, "timePageCss.html", locals())

import random #導入亂數模組
def dice(request):
  no1 = random.randint(1,6) #產生1~6的亂數
  no2 = random.randint(1,6)
  no3 = random.randint(1,6)
  print(f"骰子1: {no1}, 骰子2: {no2}, 骰子3: {no3}")
  # return HttpResponse("<b>骰子</b>") 一開始測試
  # return render(request, "dice.html", locals()) 將全部變數傳給html
  return render(request, "dice.html", {"no1": no1, "no2": no2, "no3": no3}) #要拋甚麼給甚麼變數過去html,{name: value, name: value}

def diceList(request):
  student = {'id':1234, 'name':'John','sex': 'M', 'age':20}
  fruits = ['apple', 'banana', 'orange', 'grape']
  print(f"student: {student}, fruits: {fruits}")
  return render(request, "diceList.html", {"student": student, "fruits": fruits})

def diceList2(request):
  person01 = {'name':'Amy', 'phone':'0912345678', 'email':'amy@gmail'}
  person02 = {'name':'Bob', 'phone':'0987654321', 'email':'bob@gmail'}
  person03 = {'name':'Charlie', 'phone':'0922333444', 'email':'charlie@gmail'}
  persons = [person01, person02, person03]
  # persons = []--->如果遇到整個資料事沒有的就會出現"沒有資料"
  print(persons)
  return render(request, "diceList2.html", {"persons": persons})

def get1(request):
  # name = request.GET["name"]
  # city = request.GET["city"]

  name = request.GET.get("name", None) 
  city = request.GET.get("city", None)
  # 如果沒有name就會是None，避免網頁出錯
  # 透過python：basic07-Dictionary.py的方法
  
  print(f"name: {name}, city: {city}")
  return render(request, "get1.html", {"name": name, "city": city})

def get2(request):
  try: #先跑這個，若沒有就跳到下面except
    name = request.GET["name"]
    city = request.GET["city"]  
    status = True
    print(f"name: {name}, city: {city}")
  except:
    status = False
  print(f"status: {status}")
  # return HttpResponse(f"<b>status: {status}</b>")
  return render(request, "get2.html", locals()) #locals()會把所有變數都傳過去

def get3(request, mode):
  print(f"mode: {mode}")
  if mode == "save":
    username = request.GET.get("username", None)
    password = request.GET.get("password", None)
    print(f"username: {username}, password: {password}")    
    # return HttpResponse("表單已送出") #可以出現這段
    if len(password)>3:
      password = '*' * (len(password)-3) + password[-3:] #密碼前面用*取代，後面三個字元保留
    else:
      password = '*' * len(password) #密碼全部用*取代
    
    
    return render(request, "get3_response.html", locals()) #可以是同一頁(表單已送出)，也可以換頁
  
  elif mode == "load":
    # return HttpResponse(f"Hello get3, mode: {mode}")
    return render(request, "get3.html", locals())
  
def post(request):
  if request.method == "POST":
    # username = request.POST["username"]
    # password = request.POST["password"]
    username = request.POST.get("username", None).strip() #strip去掉輸入時的前後空白
    password = request.POST.get("password", None).strip()
    print(f"username: {username}, password: {password}")
    if username == "admin" and password == "1234": #如果輸入正確的帳號密碼就會登入成功
      # return HttpResponse("登入成功")
      status = True
    else:
      # return HttpResponse("登入失敗")
      status = False  
    return render(request, "post_response.html", {"status": status, "username": username}) #傳送status和username給post_response.html
  else:
    # return HttpResponse("Hello post, 請使用POST方法")
    return render(request, "post.html", locals())
  
def post02(request):
  if request.method == "POST":
    items = request.POST.getlist("items", None) #取得多個checkbox的值
    print(items)
    return render(request, "post02_response.html", locals())
  else:
    return render(request, "post02.html", locals())