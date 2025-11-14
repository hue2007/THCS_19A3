can_nang = float(input("Nhập cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập chiều cao của bạn (mét): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")