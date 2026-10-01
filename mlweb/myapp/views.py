# Create your views here.
from django.shortcuts import render
from django.conf import settings

import os
import joblib
import pandas as pd


# 模型檔案的位置
MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    "LinearRegressionModel.pkl"
)

# 載入模型
model = joblib.load(MODEL_PATH)


def index(request):

    # 預測結果預設為空值
    prediction = None

    if request.method == "POST":

        try:
            # 取得使用者輸入的資料
            area = float(request.POST.get("area"))
            house_age = float(request.POST.get("house_age"))
            rooms = int(request.POST.get("rooms"))
            floor = int(request.POST.get("floor"))
            mrt_distance = float(request.POST.get("mrt_distance"))
            school_distance = float(request.POST.get("school_distance"))
            parking = int(request.POST.get("parking"))

            # 取得使用者選擇的行政區
            district = request.POST.get("district")

            # 建立行政區欄位
            # 一開始全部設定為 0
            district_data = {
                "行政區_台北市信義區": 0,
                "行政區_台北市大安區": 0,
                "行政區_台南市東區": 0,
                "行政區_新北市新店區": 0,
                "行政區_新北市板橋區": 0,
                "行政區_桃園市中壢區": 0,
                "行政區_高雄市左營區": 0,
            }

            # 將使用者選擇的行政區設定為 1
            if district in district_data:
                district_data[district] = 1

            # 建立要預測的新房屋資料
            new_house = pd.DataFrame({
                "坪數": [area],
                "屋齡": [house_age],
                "房間數": [rooms],
                "樓層": [floor],
                "捷運距離公尺": [mrt_distance],
                "學校距離公尺": [school_distance],
                "有車位": [parking],

                "行政區_台北市信義區": [
                    district_data["行政區_台北市信義區"]
                ],
                "行政區_台北市大安區": [
                    district_data["行政區_台北市大安區"]
                ],
                "行政區_台南市東區": [
                    district_data["行政區_台南市東區"]
                ],
                "行政區_新北市新店區": [
                    district_data["行政區_新北市新店區"]
                ],
                "行政區_新北市板橋區": [
                    district_data["行政區_新北市板橋區"]
                ],
                "行政區_桃園市中壢區": [
                    district_data["行政區_桃園市中壢區"]
                ],
                "行政區_高雄市左營區": [
                    district_data["行政區_高雄市左營區"]
                ],
            })

            # 顯示要預測的資料，方便測試
            print(new_house)

            # 進行房價預測
            result = model.predict(new_house)

            # 取得第一筆預測結果
            prediction = round(float(result[0]), 2)

        except Exception as e:
            print("預測發生錯誤：", e)
            prediction = "預測失敗，請檢查輸入資料或模型欄位"

    return render(
        request,
        "myapp/index.html",
        {
            "prediction": prediction
        }
    )