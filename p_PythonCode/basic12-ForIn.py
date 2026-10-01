#for in
#string
print("..........1...........")
for letter in "Python":
  print(f"current letter: {letter}")

print()#list
print("..........2...........")
fruits = ["Banaba", "Apple", "Mango"]
for f in fruits:
  print(f"current fruit: {f}")
  
print()#dictionary for in兩種寫法
print("..........3...........")
dict_data = {"Banana":20,"Apple":50,"Mamgo":30}
#取key，透過key，再產生value
for name in dict_data:
  print(f"{name}數量為{dict_data[name]}")

#利用items()，取得key and value
for name, num in dict_data.items():
  print(f"{name}數量為{num}")
  
#########################
print()#list內有多個dictionary
print("..........4...........")
items = [{"name":"Bill","score":30}, #第一個抽屜0 ：{ Key:value , Key:value }
         {"name":"Mary","score":30}, #第一個抽屜1
         {"name":"Harry","score":30},#第一個抽屜2
        ]
print(items) #程式的預設是一整條，除非用下方的for回圈，才會變成斷行，內回圈跑再外回圈
print()#list格式
print("..........5...........")
for data in items:
  print(data)
print()
for data in items:
  print(f"姓名={data["name"]},分數={data["score"]}")