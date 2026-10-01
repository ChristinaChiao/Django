height = float(input("請輸入身高（公分）："))
weight = float(input("請輸入體重（公斤）："))

height_m = height / 100
bmi = weight / (height_m ** 2)

print(f"你的 BMI 值為：{bmi:.2f}")

if bmi < 18.5:
	print("健康狀況：體重過輕")
elif bmi < 24:
	print("健康狀況：正常範圍")
elif bmi < 27:
	print("健康狀況：過重")
else:
	print("健康狀況：肥胖")
