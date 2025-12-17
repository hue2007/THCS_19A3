chuoi = input("Nhập chuỗi: ")
ket_qua = ""
gap_khoang_trang = False

for kytu in chuoi:
    if kytu != " ":
        ket_qua += kytu
        gap_khoang_trang = False
    else:
        if not gap_khoang_trang:
            ket_qua += kytu
            gap_khoang_trang = True

print(ket_qua.strip())
