print("......1......")
#建立list
list_data = ['abcd', 786, 2.23, 'John', 70.2, 786]
print(list_data)

#取得元素
print(list_data[0])#第一個元素
print(list_data[2])#第三個元素
print(list_data[1:3])#第二個跟第三個元素
#結束在第四個元素，但不包含第四個元素
print(list_data[2:])#第三個元素以後

print("......2......")
#update
print(list_data)#印出原始
list_data[2] = "new number" #覆蓋
print(list_data)#印出修改後的樣子

print("......3......")
#delete
print(list_data)#印出原始
del list_data[2]
print(list_data)#印出修改後的樣子

print("......4......")
#append
print(list_data)#印出原始
list_data.append("ccccc")
print(list_data)#印出修改後的樣子

print("......5......")
#走訪(依序給予序列中的值，並印出)
for element in list_data:
  print(element)