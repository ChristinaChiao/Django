
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # 網址交給 myapp 處理
    path("", include("myapp.urls")),
]