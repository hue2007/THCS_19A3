ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")
co_quyen_truy_cap = (ten_dang_nhap == "admin") and (mat_khau != "password123")
print(f"Quyền truy cập được chấp nhận: {co_quyen_truy_cap}")