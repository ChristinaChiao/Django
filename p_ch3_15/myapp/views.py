from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser  # 假設你的模型名稱是 User
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, 'index.html')  

from django.shortcuts import redirect
def useradd(request):
  if request.method == 'POST':
      # 處理表單提交邏輯
      username = request.POST.get('username')
      password = request.POST.get('password')
      repassword = request.POST.get('repassword')
      phone = request.POST.get('phone')
      email = request.POST.get('email')
      birthday = request.POST.get('birthday')
      print(f"username: {username}, password: {password}, repassword: {repassword}, phone: {phone}, email: {email}, birthday: {birthday}")
      
      UserModel = get_user_model()#取得使用者模型
      #檢查帳號是否已存在
      if UserModel.objects.filter(username=username).exists():
          messages.error(request, "帳號已被使用，請選擇其他帳號")
          return render(request, 'useradd.html')
      #檢查密碼是否一致
      if password != repassword:
          messages.error(request, "密碼不一致，請重新輸入")
          return render(request, 'useradd.html')
        
      #建立使用者，使用orm的create_user方法
      user = UserModel.objects.create_user(
        username=username, 
        password=password, 
        email=email, 
        tel=phone, 
        cBirthday=birthday)
      user.is_active = True # 設定使用者為啟用狀態
      user.is_staff = False # 設定使用者為非管理員
      user.save() # 儲存使用者資料
      messages.success(request, "使用者已成功建立")
      return redirect('/userlogin/')
  else:
    return render(request, 'useradd.html')
  
from django.contrib.auth import authenticate, login, logout
def userlogin(request):
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      print(f"username: {username}, password: {password}")
      #驗證，使用者是否存在且密碼正確
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)#目的：將使用者登入，並在session中建立使用者資訊
        return redirect('/index/')
      else:
        messages.error(request, "帳號或密碼錯誤，請重新輸入")
        return redirect('/userlogin/')
    else:
        return render(request, 'userlogin.html')

def userlogout(request):
  logout(request)
  messages.success(request, "已成功登出")
  return redirect('/index/')

def page(request):
    return render(request, 'page.html')