tien_goc = float(input("Nhập số tiền gửi ban đầu: "))
lai_suat_nam = float(input("Nhập lãi suất hàng năm (%): "))
lai_suat_thap_phan = lai_suat_nam / 100
lai_1_thang = tien_goc * lai_suat_thap_phan * (1 / 12)
lai_2_quy = tien_goc * lai_suat_thap_phan * 0.5
lai_3_nam = tien_goc * lai_suat_thap_phan * 3
print(f"Tiền lãi sau 1 tháng: {lai_1_thang:.2f}")
print(f"Tiền lãi sau 2 quý: {lai_2_quy:.2f}")
print(f"Tiền lãi sau 3 năm: {lai_3_nam:.2f}")