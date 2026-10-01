# ----------------------------------------------------
# 套件安裝說明：
# pip install pandas scikit-learn matplotlib
# ----------------------------------------------------

import pickle
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ====================================================
# 1. 資料讀取與檢視
# ====================================================
# 讀取原始 CSV 資料
df = pd.read_csv("LinearRegressionData.csv", encoding="utf-8")

# 檢視前 5 筆資料與基本資訊
print("=== 原始資料前 5 筆 ===")
print(df.head()) 
# print(df.info())      # 查看數據集結構與型態
# print(df.describe())  # 查看數值型欄位的統計資訊

# ====================================================
# 2. 特徵工程（類別變數處理）
# ====================================================
# 將「行政區」轉換為獨熱編碼 (One-Hot Encoding)
# drop_first=True 可刪除第一個類別欄位，避免多重共線性問題 (Dummy Variable Trap)
df = pd.get_dummies(df, columns=["行政區"], drop_first=True)

print("\n=== 特徵編碼後資料前 5 筆 ===")
print(df.head())

# 輸出預處理後的完整資料（utf-8-sig 可避免 Excel 開啟時中文亂碼）
df.to_csv("LinearRegressionData_processed.csv", index=False, encoding="utf-8-sig")

# ====================================================
# 3. 定義特徵矩陣 (X) 與目標變數 (y)
# ====================================================
# 特徵 X：刪除不相關欄位（編號）與預測目標（房價萬元）
X = df.drop(["房價萬元", "編號"], axis=1) # axis=1 表示刪除欄位

# 目標 y：房價萬元
y = df["房價萬元"]

print("\n=== 特徵矩陣 X 前 5 筆 ===")
print(X.head())
print("\n=== 目標變數 y 前 5 筆 ===")
print(y.head())

# ====================================================
# 4. 切分訓練集與測試集
# ====================================================
# 切分比例：80% 訓練集、20% 測試集
# random_state=100：固定隨機種子，確保每次執行切分結果一致
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2, 
    random_state=100
)

# 匯出訓練集資料備份
X_train.to_csv("LinearRegressionData_train_x.csv", index=False, encoding="utf-8-sig")
y_train.to_csv("LinearRegressionData_train_y.csv", index=False, encoding="utf-8-sig")

# ====================================================
# 5. 建立與訓練模型
# ====================================================
# 初始化線性回歸模型並進行擬合
model = LinearRegression()
model.fit(X_train, y_train)

# ====================================================
# 6. 模型匯出
# ====================================================
# 將訓練完成的模型序列化保存為 pickle 檔
with open("LinearRegressionModel.pkl", "wb") as f:
    pickle.dump(model, f)

print("\n模型已成功訓練並匯出至 LinearRegressionModel.pkl！")