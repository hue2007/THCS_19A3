
# Bước 1: Tạo danh sách số nguyên
danh_sach_so = [1, 3, 5, 7, 9, 11, 13]

# Bước 2 & 3: Mở file và ghi từng số
with open("so_nguyen.txt", "w", encoding="utf-8") as tap_tin:
    for so in danh_sach_so:
        tap_tin.write(str(so) + "\n")

print("Đã ghi danh sách số nguyên vào file so_nguyen.txt")
