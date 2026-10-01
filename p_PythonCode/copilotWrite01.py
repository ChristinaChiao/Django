#我想讓使用者輸入身高和體重，然後計算BMI值並判斷其健康狀況。
height = float(input("請輸入身高(cm):"))
weight = float(input("請輸入體重(kg):"))
height_m = height / 100  # 將身高轉換為公尺
BMI = round(weight / (height_m * height_m), 2)  # 計算BMI值並四捨五入到小數點後兩位
if BMI >= 35:
    print(f"BMI 值為 {BMI}。屬重度肥胖")
elif 30 <= BMI < 35:
    print(f"BMI 值為 {BMI}。屬中度肥胖")
elif 27 <= BMI < 30:
    print(f"BMI 值為 {BMI}。屬輕度肥胖")
elif 24 <= BMI < 27:
    print(f"BMI 值為 {BMI}。屬稍重")
elif 18.6 <= BMI < 24:
    print(f"BMI 值為 {BMI}。屬正常範圍")
else:
    print(f"BMI 值為 {BMI}。屬體重過輕")

    