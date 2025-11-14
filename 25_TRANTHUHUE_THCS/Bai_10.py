luong_co_ban = float(input("Nhập lương cơ bản: "))
so_ngay_cong = float(input("Nhập số ngày công: "))
luong_mot_ngay = luong_co_ban / 22
luong_thuc_te = luong_mot_ngay * so_ngay_cong
tien_thuong = (0.10 * luong_co_ban) * (so_ngay_cong > 22)
tien_phat = (0.05 * luong_co_ban) * (so_ngay_cong < 22)
tong_luong_thuc_nhan = luong_thuc_te + tien_thuong - tien_phat
print("--- Bảng lương chi tiết ---")
print(f"Lương thực tế ({so_ngay_cong} ngày): {luong_thuc_te:.0f} VNĐ")
print(f"Tiền thưởng: {tien_thuong:.0f} VNĐ")
print(f"Tiền phạt: {tien_phat:.0f} VNĐ")
print(f"Tổng lương thực nhận: {tong_luong_thuc_nhan:.0f} VNĐ")