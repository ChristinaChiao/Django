from django.shortcuts import render #render是Django內建的函式，用於渲染模板
from django.http import HttpResponse #httpResponse是Django內建的函式，用於回傳HTTP響應
from django.forms.models import model_to_dict #將資料轉換成字典型態
from myapp.models import * #import models.py裡的所有class
from django.db.models import Avg, Sum, Count, Max, Min #聚合函數，用於計算平均值、總和、計數、最大值、最小值
def test(request):
  # datas = Scorelist.objects.aggregate(Sum('score'))
  # datas = Scorelist.objects.filter(course='國文').aggregate(Sum('score'))
  # datas = Scorelist.objects.filter(course='國文').aggregate(Avg('score'))
  # datas = Student.objects.aggregate(Count('cID'))
  # datas = Scorelist.objects.filter(course='國文').aggregate(Max('score'))
  # datas = Scorelist.objects.filter(course='國文').aggregate(Min('score'))
  #   print(datas) #一般格式印出
  ########################
  # datas = Scorelist.objects.values_list('cID').annotate(Sum('score'))
  # datas = Scorelist.objects.values_list('cID').annotate(Avg('score'))
  # for data in datas:
  #   print(data) #格式tuple
  # datas = Scorelist.objects.values_list('cID').annotate(Sum('score')).filter(cID__lte=5)
  # #說明：這段程式碼會先將Scorelist依照cID分組，計算每組的總分，然後只取cID小於等於5的資料
  # for data in datas:
  #    print(data) #格式tuple
  ############新增資料############
  #第一種方式：先建立物件，再呼叫save()方法
  # student_exists = Student.objects.filter(cName="Bill").exists() #判斷新增的資料是否存在
  # if not student_exists:
  #   add = Student(cName="Bill", cSex="M", cBirthday="2021-08-08", 
  #                 cEmail="bill@yahoo.com.tw", cPhone="0922222", cAddr=" 新 竹 ", cHeight=180, cWeight=70) 
  #   add.save() 
  #   print("新增成功")
  # else:
  #   print("資料已存在")
  #第二種方式：使用create()方法建立物件並自動儲存
  # student_exists = Student.objects.filter(cName="Bill4").exists() 
  # if not student_exists:
  #   Student.objects.create(cName="Bill4", cSex="M", cBirthday="2021-08-08", 
  #                          cEmail="bill@yahoo.com.tw", cPhone="0922222", cAddr=" 新 竹 ", cHeight=180, cWeight=70) 
  #   print("新增成功")
  # else:
  #   print("資料已存在")
  ############更新資料############
  # try: #捕捉東西是否存在，避免程式出錯
  #   update = Student.objects.get(cID=11) #假設要更新的學生是Bill
  #   update.cHeight=190
  #   update.cWeight=80
  #   update.cSex="M"
  #   update.save() #儲存更新
  #   print("更新資料成功")
  # except Student.DoesNotExist:
  #   print("資料不存在")
  ############一口氣更新多筆資料############
  # try:
  #   update_count = Student.objects.filter(cID__gte=11).update(cAddr="台北市中正區建國南路一段1號", cPhone="0912345678")
  #   print(f"更新{update_count}筆資料成功") #cID大於等於11以後的資料修改
  # except:
  #   print("更新多筆資料失敗")
  ############刪除資料############ 
  student_exists = Student.objects.filter(cID__gte=12).exists() #判斷要刪除的資料是否存在
  if student_exists:
    delete_count = Student.objects.filter(cID__gte=12).delete() #假設要刪除的學生是Bill
    print(f"刪除{delete_count[0]}筆資料成功") #刪除資料
  else:
    print("資料不存在")
  

  return HttpResponse("Hello, world. You're at the test index.") #每一段程式碼都需要這個去回傳訊息，否則會出現錯誤