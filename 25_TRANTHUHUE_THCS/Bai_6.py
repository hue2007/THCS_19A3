nam = int(input("Nhập một năm: "))
la_nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
print(f"Năm {nam} là năm nhuận? {la_nam_nhuan}")