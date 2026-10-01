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
from myapp import views
#從myapp導入views.py

urlpatterns = [
    path("", views.home, name="home"), #首頁
    path("admin/", admin.site.urls),
    path('homework2/<str:username>/', views.homework2, name='homework2'),
    #請求/後面要輸入字串，輸入就會變正常
    path('lotto1/<str:username>/', views.lotto1, name='lotto1'),
    path('lotto2/', views.lotto2, name='lotto2'),
    path('lotto3/', views.lotto3, name='lotto3'),
]
