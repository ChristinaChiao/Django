#講義P18
print("......1......")
name = "王大明" #name是變數，"字串"
score = 80 #int
score2 = 80.0 #float(浮點後面是6位數)
print(type(name)) #顯示(檢查)變數型態
print(type(score)) 
print(type(score2))

print(name+"的成績為"+ str(score)) #用+做串接。str(變數)->改成字串

print("......2......")#,
print(name, score)#變數跟變數之間,預設的間隔是"空白"
print(name, score, sep="&", end="***")#sep去修改"空白"改&，結尾(end)的接續，從變成下一行改成***
print("hello")

print(name, score, sep=" ", end="\n")#修改成預設
print("hello")

print("......3......")#參數格式化:%
# %s=> str
# %d=> int
# %f=> float
# %c=> char
print("%s的成績為%d"%(name, score))
import math
print("PI=%f"% math.pi)
print("PI=%10.3f"% math.pi)#總長10(個數字)、小數後3碼、"."也算一個數
print("PI=%6.0f"% math.pi)
#參數格式化:format(不用知道是甚麼格式,通通會幫你改成字串)
print("......4......")
print("{}的成績為{}".format(name, score))
print("PI={}" .format(math.pi))
print("PI={:10.3f}" .format(math.pi))
print("PI={:6.0f}" .format(math.pi))

print("......5......")#f-string:python 3.6以後
print(f"{name}的成績為{score}")
print(f"PI={math.pi}")
print(f"PI={math.pi:10.3f}")
print(f"PI={math.pi:6.0f}")
print(f"PI={math.pi:.3}")#保留3位有效數字
print(f"PI={math.pi:.3f}")#保留小數點後3位

x=10
y=20
print(f"x*y={x*y}")
print(f"x*y={x*y}", end="\t")#\t空格
print(f"x+y={x+y}", end="\t")
print(f"x-y={x-y}", end="\t")