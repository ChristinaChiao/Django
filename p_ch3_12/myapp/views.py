from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import * #所有
from django.forms.models import model_to_dict # 將模型實例轉換為字典格式
from django.core.paginator import Paginator # 分頁功能

def search_list(request): #一個網頁一個請求
  # datas = Students.objects.all() #取得所有學生資料
  # # datas = Students.objects.all().order_by('-cid') #所有學生資料遞減
  # for data in datas: #Debug用，發佈前請註解掉
  #     print(type(datas)) #data 為Students物件
  #     print(model_to_dict(data)) #將資料轉換為字典格式並印出
  # if not datas:
  #   errormessage = "No data found."
  # return render(request, "search_list.html", {"datas": datas, "errormessage": errormessage if not datas else ""}) #將學生資料傳遞給模板
  if 'cname' in request.GET:
      cname = request.GET['cname']
      print(f"Recived cname:{cname}")
      datas = Students.objects.filter(cname__icontains=cname).order_by('-cid') # 根據姓名進行模糊查詢並按學號遞減排序
      # 根據姓名進行模糊查詢
  else:
      datas = Students.objects.all().order_by('-cid') # 如果沒有提供姓名，則返回所有學生資料並按學號遞減排序
  if not datas:
      errormessage = "No data found."
  return render(request, "search_list.html", locals()) #將學生資料傳遞給模板

def search_name(request): #一個網頁一個請求，對應URL為 /search_name
  #再從View返回到前端網頁
  return render(request, "search_name.html", locals()) #返回search_name.html模板

def index(request): 
  if 'site_search' in request.GET: #搜尋語法
      site_search = request.GET['site_search']
      site_search = site_search.strip() # 去除前後空白
      print(f"site_search: {site_search}") #debug
      keywords = site_search.split() # 將搜尋關鍵字拆分為列表
      print(f"keywords: {keywords}") #debug
      from django.db.models import Q
      query = Q() #初始化查詢條件
      for keyword in keywords:
        print(f"keyword: {keyword}") #debug
        query |= Q(cname__icontains=keyword)#|or->只要有一個符合，就符合
        query |= Q(cbirthday__icontains=keyword)
        query |= Q(cemail__icontains=keyword)
        query |= Q(cphone__icontains=keyword)
        query |= Q(caddr__icontains=keyword)
      resultlist = Students.objects.filter(query).order_by('-cid') # 根據查詢條件取得學生資料
  else:
      resultlist = Students.objects.all()
      
  # orm 語法
  data_count = resultlist.count() # 計算學生資料的總數
  print(data_count)
  
  # for data in resultlist:
  #     print(model_to_dict(data)) #將資料轉換為字典格式並印出   
  
  #分頁設定，每頁顯示2    
  paginator = Paginator(resultlist, 2) # 每頁顯示2筆資料
  page_number = request.GET.get('page') #取得當前頁碼，如page2
  page_obj = paginator.get_page(page_number) #取得當前頁的對應資料
  #說明:
  #page_obj 包含當前頁的資料以及分頁相關資訊
  #page_obj.number 當前頁碼
  #page_obj.paginator.num_pages 總頁數
  #page_obj.paginator.page_range 總頁碼範圍列表
  #page_obj.object_list 包含當前頁的資料列表
  
  #page_obj.has_next() 判斷是否有下一頁
  #page_obj.has_previous() 判斷是否有上一頁
  #page_obj.next_page_number() 下一頁的頁碼
  #page_obj.previous_page_number() 上一頁的頁碼

  
  return render(request, "index.html", locals()) 

def post(request):
  if request.method == "POST":
      cname = request.POST.get("cname")
      csex = request.POST.get("csex")
      cbirthday = request.POST.get("cbirthday")
      cemail = request.POST.get("cemail")
      cphone = request.POST.get("cphone")
      caddr = request.POST.get("caddr")
      print(f"Received POST data: cname={cname}, csex={csex}, cbirthday={cbirthday}, cemail={cemail}, cphone={cphone}, caddr={caddr}")
      add = Students.objects.create(
          cname=cname,
          csex=csex,
          cbirthday=cbirthday,
          cemail=cemail,
          cphone=cphone,
          caddr=caddr
      )#新增資料
      add.save()#存到資料庫
      return redirect('index') #導向首頁
  else:
      return render(request, "post.html", locals())
    
def edit(request, id):
  if request.method == "POST":
      cname = request.POST.get("cname")
      csex = request.POST.get("csex")
      cbirthday = request.POST.get("cbirthday")
      cemail = request.POST.get("cemail")
      cphone = request.POST.get("cphone")
      caddr = request.POST.get("caddr")
      print(f"id:{id}")
      print(f"cname={cname}, csex={csex}, cbirthday={cbirthday}, cemail={cemail}, cphone={cphone}, caddr={caddr}")
      update = Students.objects.get(cid=id) #單筆更新
      update.cname = cname
      update.csex = csex
      update.cbirthday = cbirthday
      update.cemail = cemail
      update.cphone = cphone
      update.caddr = caddr
      update.save()
      # update = Students.objects.filter(cid=id).update(
      #     cname=cname,
      #     csex=csex,
      #     cbirthday=cbirthday,
      #     cemail=cemail,
      #     cphone=cphone,
      #     caddr=caddr
      # ) 多筆更新
      return redirect('index') #導向首頁
  else:
      obj_data = Students.objects.get(cid=id) #根據ID取得學生資料
      print(model_to_dict(obj_data)) #將資料轉換為字典格式並印出
    
      return render(request, "edit.html", locals())

def delete(request, id):
  if request.method == 'POST':
     delete_obj = Students.objects.get(cid=id)
     delete_obj.delete()
     return redirect('index') #導向首頁
  
  else:
      obj_data = Students.objects.get(cid=id) #根據ID取得學生資料
      print(model_to_dict(obj_data)) #將資料轉換為字典格式並印出
    
      return render(request, "delete.html", locals())