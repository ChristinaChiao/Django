print("......1......")
#建立Dictinoary

dict_data = {"name":"John","code":6734,"dept":"sales"}#無順序性，一個key一個值
print(dict_data)

print("......2......")
#再新增
print(dict_data)
dict_data["one"] = "This is one"
print(dict_data)

dict_data2 = {}#原本空的
dict_data2["one"] = "one"
dict_data2[2] = "two"
print(dict_data2)

print("......3......")
#修改
print(dict_data)
dict_data['code'] = 8888
print(dict_data)

print("......4......")
#取Key的值
print(dict_data['code'])
print(dict_data['dept'])#列印部門
print(dict_data['name'])

print("......5......")
#刪除
print(dict_data)
del dict_data['dept']
print(dict_data)

print("......6......")
#走訪(取key，透過key，再產生value給我使用)
print(dict_data)
for key in dict_data:
  print(key), #選起來ctrl+/註解掉
  
for key in dict_data:
  print(f"{key}=>{dict_data[key]}"),
    
print("......7......")
#利用items()，取得key and value)
for k, v in dict_data.items():
  print(k)
  print(v)
  print("↓"),
  
for k, v in dict_data.items():
  print(f"{k}=>{v}"),

print("......8......")
#method01: try except:
#method02: 透過get(方法)去取得Key，不至於網頁崩壞
print(dict_data.get("sample"))#預設顯示none
print(dict_data.get("sample", "N"))
print(dict_data.get("name", "N"))