from django.shortcuts import render
from .models import userprofile

# Create your views here.
def homework6(request):
  if request.method == "POST":
    username = request.POST.get("username")
    usersex = request.POST.get("usersex")
    userschool = request.POST.get("userschool")
    userinterest = request.POST.getlist("userinterest", None) #取得多個checkbox的值
    userthought = request.POST.get("userthought")
    print("username:", username)
    print("usersex:", usersex)
    print("userschool:", userschool)
    print("userinterest:", userinterest)
    print("userthought:", userthought)
    # 將使用者輸入的資料存入資料庫，資料庫userprofile對應的欄位分別是username, userSex, userschool, userinterest, userthought
    # userinterest 是多選 checkbox，用逗號串成字串存入 TextField
    userprofile.objects.create(
      username=username,
      userSex=usersex,
      userschool=userschool,
      userinterest=",".join(userinterest or []),
      userthought=userthought,
    )

    return render(request, "homework6_re.html", locals())
  else:
    return render(request, "homework6.html", locals())

def homework6_list(request):
  # 取得所有使用者資料
  datas = userprofile.objects.all()
  # 把逗號字串拆成 list，供模板迭代顯示
  for d in datas:
    d.interest_list = [i for i in (d.userinterest or "").split(",") if i] 
    #i：每個興趣項目，split是用來把字串拆成清單的函式，這個函式公式： "字串".split("分隔符號")
  return render(request, "homework6_list.html", locals())