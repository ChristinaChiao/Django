print("...........1...........")
#range(起始值，結束值，遞增)
# #列印1-5,預設1
for num in range(1,5):
  print(num) #1,2,3,4

print()#遞增列印1,3,5,7,9
print("...........2...........")
for num in range(1,10,2):
  print(num)
  
print()#列印1,4,7
for num in range(1,10,3):
  print(num)
  
print()
#range(起始值，結束值，遞減)
#遞減列印10,7,4,1
print("...........3...........")
for num in range(10,0,-3):
  print(num)
  
print()
print("...........4...........")
for num in range(5): #代表(0,5)----->縮寫，預設0
  print(num)