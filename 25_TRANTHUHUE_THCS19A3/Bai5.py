n = int(input("Nhập số phần tử của danh sách: "))
danh_sach = []
ket_qua = []
for i in range(n):
    so = int(input("Nhập số: "))
    danh_sach.append(so)
for x in danh_sach:
    trung = False
    for y in ket_qua:
        if x == y:
            trung = True
            break
    if not trung:
        ket_qua.append(x)
print("Danh sách sau khi loại bỏ phần tử trùng lặp:")
for x in ket_qua:
    print(x, end=" ")


