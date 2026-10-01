ch = input("請輸入國文成績：")
print(ch)
print(type(ch))#看類別->字串(預設基本上都是字串)
#string
math = input("請輸入數學成績：")
en = input("請輸入英文成績：")
sum = ch+math+en
sum = int(ch)+int(math)+int(en)#變成變數
avg = sum / 3 #avg = float(sum) / 3
print(f"sum=>{sum}")
print(f"成績總分=>{sum}, 平均成績:{avg:.3f}")