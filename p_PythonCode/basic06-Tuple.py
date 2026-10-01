print("......1......")
#建立tuple
tuple_data = ['abcd', 786, 2.23, 'John', 70.2, 786]
print(tuple_data)

#取得元素
print(tuple_data[0])#第一個元素
print(tuple_data[2])#第三個元素
print(tuple_data[1:3])#第二個跟第三個元素
print(tuple_data[2:])#第三個元素以後

#與list不同的是，不能改變(新增、刪除)，因為他是常數

print("......2......")
#走訪(依序給予序列中的值，並印出)
for element in tuple_data:
  print(element)