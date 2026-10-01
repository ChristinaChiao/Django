from django.shortcuts import render

# Create your views here.
def homework3(request):
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
    
    return render(request, "homework3_re.html", locals())
  else:
    return render(request, "homework3.html", locals())