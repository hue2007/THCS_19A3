n = int(input("Nhập số phần tử của danh sách: "))
danh_sach = []
for i in range(n):
    so = int(input("Nhập số: "))
    danh_sach.append(so)
lon_nhat = danh_sach[0]
for x in danh_sach:
    if x > lon_nhat:
        lon_nhat = x
lon_thu_hai = None
for x in danh_sach:
    if x != lon_nhat:
        if lon_thu_hai is None or x > lon_thu_hai:
            lon_thu_hai = x
if lon_thu_hai is None:
    print("Không tồn tại giá trị lớn thứ hai")
else:
    print("Giá trị lớn thứ hai là:", lon_thu_hai)
