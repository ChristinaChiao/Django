"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myapp import views #從myapp導入views.py

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index01),
    #'請求', 呼叫views裡的index的function(函式)5-6行
    #sayhello要跟views.py的函式名稱相同
    
    path('hello/', views.hello),
    #請求新的分頁叫hello1
    
    path('helloName1/<str:username>/', views.helloName1),
    path('helloName2/<str:username1>/<str:username2>/',views.helloName2),
    
    path('timePage/<str:username>/', views.timePage),
    path('timePageCss/<str:username>/', views.timePageCss),
    #請求/後面要輸入字串，輸入就會變正常
    
    path('dice/', views.dice),
    path('diceList/', views.diceList),
    path('diceList2/', views.diceList2),
    
    path('get1/', views.get1),
    path('get2/', views.get2),
    path('get3/<str:mode>/', views.get3), #模式MODE: save or load
    
    path('post/', views.post),
    path('post02/', views.post02),

]
