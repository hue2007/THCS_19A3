n = int(input("Nhập số phần tử: "))
danh_sach = []

i = 0
while i < n:
    danh_sach.append(int(input("Nhập số: ")))
    i += 1

tong = int(input("Nhập tổng cần tìm: "))

i = 0
while i < n:
    j = i + 1
    while j < n:
        if danh_sach[i] + danh_sach[j] == tong:
            print(danh_sach[i], danh_sach[j])
        j += 1
    i += 1
