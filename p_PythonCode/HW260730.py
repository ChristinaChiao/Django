#第一題
ub = int(input("請輸入上底："))
db = int(input("請輸入下底："))
h = int(input("請輸入高："))
print(f"梯形面積={(ub + db) * h / 2}")

#第二題
height = int(input("請輸入身高(cm):"))
weight = int(input("請輸入體重(kg):"))
height_m = height/100
BMI = round(weight/(height_m*height_m),2)
if(BMI>=35): 
  print("BMI 值為",{BMI},"。屬重度肥胖")
elif(35>BMI>=30):
  print("BMI 值為",{BMI},"。屬中度肥胖")
elif(30>BMI>=27):
  print("BMI 值為",{BMI},"。屬輕度肥胖")
elif(27>BMI>=24): 
  print("BMI 值為",{BMI},"。屬稍重")
elif(24>BMI>=18.6): 
  print("BMI 值為",{BMI},"。屬正常範圍")
else: 
  print("BMI 值為",{BMI},"。屬體重過輕")
  

#第三題
print("===單位轉換器===")
print("1. 公尺(m)轉英呎(ft)")
print("2. 英呎(ft)轉公尺(m)")
print("3. 公斤(kg)轉英鎊(lb)")
print("4. 英鎊(lb)轉公斤(kg)")
choice = int(input("請輸入1-4:"))
if(choice==1):
  m =float(input("請輸入公尺數"))
  ft = float(m*3.28)
  print(f"{m:6f}公尺={ft:6f}英呎")

elif(choice==2):
  ft =float(input("請輸入英呎數"))
  m = float(ft/3.28)
  print(f"{ft:6f}英呎={m:6f}公尺")

elif(choice==3):
  kg =float(input("請輸入公斤數"))
  lb = float(kg*2.2)
  print(f"{kg:6f}公斤={lb:6f}英鎊")
  
elif(choice==4):
  lb =float(input("請輸入英鎊數"))
  kg = float(lb/2.2)
  print(f"{lb:6f}英鎊={kg:6f}公斤")

else:
  print("無此選項")