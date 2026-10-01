from django.shortcuts import render #render是Django內建的函式，用於渲染模板
from django.http import HttpResponse #httpResponse是Django內建的函式，用於回傳HTTP響應
from myapp.models import * #import models.py裡的所有class
from django.forms.models import model_to_dict #將資料轉換成字典型態
def test(request):
  ##########取得所有學生資料###########
  # datas = student.objects.all() 
  # for data in datas:
  #  print(type(data)) #印出資料型態
  #  print(model_to_dict(data)) #將資料轉換成字典型態，並印出
  ###########只取出cID、cName、cEmail欄位###########
  # datas = student.objects.values('cID', 'cName', 'cEmail') 
  # print(type(datas)) #在下方印出資料型態,並用for檢查
  # for data in datas:
  #   # print(type(data)) 
  #   print(data)
  ###########取出cSex欄位，並去除重複值##########
  # datas = student.objects.values('cSex').distinct()
  # print(type(datas)) #在下方印出資料型態,並用for檢查
  # for data in datas:
  #   # print(type(data)) 
  #   print(data)
  ###########取得學號3的學生資料##########
  # data = student.objects.get(cID=3) 
  # print(model_to_dict(data))
  ###########取得性別為M的學生資料##########
  # datas = student.objects.filter(cSex='M')
  # print(type(datas)) #在下方印出資料型態,並用for檢查
  # for data in datas:
  #   print(model_to_dict(data))
  ###########取得學號>5且性別為M的學生資料##########
  # __gt = greater than 大於 __gteo 大於等於>=
  # __lt = less than 小於 __lte  小於等於<=
  # __exact = exact 等於
  # __iexact = case-insensitive exact 等於(不分大小寫)
  # , = and 且
  # datas = student.objects.filter(cID__gt=5, cSex='M')
  # for data in datas:
  #   print(model_to_dict(data))
  ###########等於座號 1 號或 >= 9 號的學生資料##########
  # from django.db.models import Q #Q表達式，用於複雜查詢
  # #datas = student.objects.filter(Q(cID__gt=5) & Q(cSex='M'))
  # datas = student.objects.filter(Q(cID=1) | Q(cID__gte=9))
  # for data in datas:  
  #   print(model_to_dict(data)) 
  ###########取得一個範圍的學生資料##########
  # datas = student.objects.filter(cID__range=[4, 6])
  # # datas = student.objects.filter(cID__gte=4, cID__lte=6)
  # for data in datas:
  #   print(model_to_dict(data))
  ###########取得沒有規律的學生資料##########
  # datas = student.objects.filter(cID__in=[1, 3, 5, 9])
  # for data in datas:  
  #   print(model_to_dict(data))
  ###########取得電話欄位為0918開頭##########
  # datas = student.objects.filter(cPhone__startswith='0918')
  # for data in datas:
  #   print(model_to_dict(data))
  ###########取得地址欄位包含'建國'##########
  # datas = student.objects.filter(cAddr__contains='建國')
  # for data in datas:
  #     print(model_to_dict(data))
  ###########生日遞減排序##########
  #datas = student.objects.all().order_by('cBirthday') #遞增
  # datas = student.objects.all().order_by('-cBirthday') #付的，遞減
  # for data in datas:
  #     print(model_to_dict(data))
  ###########性別遞增，再來生日遞減排序##########
  # datas = student.objects.all().order_by('cSex', '-cBirthday')
  # for data in datas:
  #     print(model_to_dict(data))
  ###########性別遞增，再來生日遞減排序##########
  datas = Student.objects.all()[:2] #ID1.2的值
  datas = Student.objects.all()[0:2] #ID1.2的值
  datas = Student.objects.all()[1:3] #1開始到3-1，顯示ID2.3的值
  datas = Student.objects.all()[4:6] #4開始到6-1，顯示ID5.6的值
  datas = Student.objects.all()[3:7] #4開始到7-1，顯示ID4.5.6.7的值
  datas = Student.objects.all()[3:10] #3開始到10-1，顯示ID4.5.6.7.8.9.10的值
  for data in datas:
     print(model_to_dict(data))
  
  return HttpResponse("Hello, world. You're at the test index.") #每一段程式碼都需要這個去回傳訊息，否則會出現錯誤