# Tạo file sản phẩm ban đầu
with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("1,Laptop,1200\n")
    f.write("2,Chuột máy tính,25\n")
    f.write("3,Bàn phím,75\n")

# Nhập ID và giá mới
id_can_sua = input("Nhập ID sản phẩm cần cập nhật: ")
gia_moi = input("Nhập giá mới: ")

ds_moi = []

# Đọc và cập nhật
with open("san_pham.txt", "r", encoding="utf-8") as f:
    for dong in f:
        thong_tin = dong.strip().split(",")
        if thong_tin[0] == id_can_sua:
            thong_tin[2] = gia_moi
        ds_moi.append(",".join(thong_tin))

# Ghi lại file
with open("san_pham.txt", "w", encoding="utf-8") as f:
    for dong in ds_moi:
        f.write(dong + "\n")

print("Cập nhật giá thành công!")