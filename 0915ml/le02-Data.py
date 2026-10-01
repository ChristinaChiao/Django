# pip install pandas scikit-learn matplotlib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split # train_test_split: # 用於將數據集拆分為訓練集和測試集的函數
from sklearn.linear_model import LinearRegression # LinearRegression: # 用於建立線性回歸模型的類    
from sklearn.metrics import mean_absolute_error # mean_absolute_error: # 用於計算平均絕對誤差的函數
from sklearn.metrics import mean_squared_error # mean_squared_error: # 用於計算均方誤差的函數
from sklearn.metrics import r2_score # r2_score: # 用於計算決定係數的函數

#將模型匯出成pickle檔案, 內容有繁體中文, 並且不輸出index欄位, 編碼為utf-8
import pickle 

# 預測
# 將模型匯入成pickle檔案, 內容有繁體中文, 並且不輸出index欄位, 編碼為utf-8
with open("LinearRegressionModel.pkl", "rb") as f:
    model = pickle.load(f) # 將pickle文件反序列化並加載為模型，rb是開啟模組

# 如果預測效果好，大部分點會靠近紅色對角線。
# 預測新房子
# 例如：
# 中壢區
# 35 坪
# 屋齡 8 年
# 3 房
# 12 樓
# 捷運 400 公尺
# 學校 600 公尺
# 有車位

new_house = pd.DataFrame({
    "坪數":[35],
    "屋齡":[8],
    "房間數":[3],
    "樓層":[12],
    "捷運距離公尺":[400],
    "學校距離公尺":[600],
    "有車位":[1],
    "行政區_台北市信義區":[0],
    "行政區_台北市大安區":[0],
    "行政區_台南市東區":[0],
    "行政區_新北市新店區":[0],
    "行政區_新北市板橋區":[0],
    "行政區_桃園市中壢區":[1],
    "行政區_高雄市左營區":[0]
})
print(new_house)

price = model.predict(new_house)

print("預測房價：%.1f 萬元" % price[0])