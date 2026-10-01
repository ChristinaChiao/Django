from django.db import models

# Create your models here.
class student(models.Model): #←資料表，↓細部欄位
    cID = models.AutoField(primary_key=True) #設定學號為主鍵，並自動遞增
    cName = models.CharField(max_length=20, blank=False) #設定姓名為字串，最大長度為20，blank=False不可為空值
    cSex = models.CharField(max_length=1, blank=False, default='F') #設定性別為字串，最大長度為1，預設F
    cBirthday = models.DateField(blank=False) #設定生日為日期
    #cBirthday = models.DateField(auto_now_add=True) #自動新增為當前日期
    #cBirthday = models.DateField(auto_now=True) #自動更新為當前日期
    cEmail = models.CharField(max_length=100, blank=True) 
    cPhone = models.CharField(max_length=50, blank=True) 
    cAddr = models.CharField(max_length=255, blank=True) 
    cHeight = models.IntegerField(blank=True) #設定整數
    cWeight = models.IntegerField(blank=True) 



    