import pandas as pd # 匯入 pandas 模組
from sklearn.linear_model import LinearRegression # 匯入線性回歸模型

#建立資料
df = pd.DataFrame({
    '坪數': [10, 20, 30, 40, 50],
    '房價': [300, 500, 700, 900, 1100]
})
print(df)

#建立x,y  
x = df[['坪數']] #將資料中的坪數欄位取出作為特徵值
y = df['房價'] #將資料中的房價欄位取出作為目標值
print(x)
print(y)

#建立線性回歸模型
model = LinearRegression()

#訓練模型(使用特徵值x和目標值y來訓練線性回歸模型)
model.fit(x, y)

print("截距:", model.intercept_)
print("斜率:", model.coef_[0])
###############################################
#畫圖
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"] # 設定字體為微軟正黑體
plt.rcParams['figure.figsize'] = (8, 6) # 設定圖形大小
plt.scatter(x, y) # 畫出散佈圖
plt.plot(x, model.predict(x), color='red') # 畫出預測回歸線
plt.xlabel('坪數') # 設定x軸標籤
plt.ylabel('房價') # 設定y軸標籤
plt.title('坪數與房價的線性回歸') # 設定圖表標題
plt.show()

###############################################
#使用模型進行預測
new_data = pd.DataFrame({
    "坪數": [35]
})

price = model.predict(new_data)

print("35坪預測房價：", price[0])