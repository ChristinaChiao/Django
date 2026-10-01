pw = input("請輸入密碼：")
if (pw == "1234"):
  print("Welcome")
else:
  print("Wrong")
  
#########################上下兩種寫法
pw = int (input("請輸入密碼："))
if (pw == 1234):
  print("Welcome")

else:
  print("Wrong")