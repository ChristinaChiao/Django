from django.db import models

# Create your models here.
class userprofile(models.Model): 
  #models寫完，要設定settings "DATABASES",安裝pip install mysqlclient，用於連接MySQL資料庫 並執行 python manage.py makemigrations 及 python manage.py migrate
  
    # 讓 Django 自動處理自增主鍵（使用 BigAutoField），或直接不寫 id 欄位由 Django 預設生成
    id = models.BigAutoField(primary_key=True) 
    username = models.CharField(max_length=100, blank=False)
    userSex = models.CharField(max_length=10, blank=False)
    userschool = models.CharField(max_length=20, blank=False)
    userinterest = models.TextField(blank=False) 
    userthought = models.TextField(blank=False) 
    