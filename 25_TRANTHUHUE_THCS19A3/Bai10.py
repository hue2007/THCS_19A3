m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
ma_tran = []
for i in range(m):
    dong = []
    for j in range(n):
        phan_tu = int(input("Nhập phần tử: "))
        dong.append(phan_tu)
    ma_tran.append(dong)
tong_max = 0
for j in range(n):
    tong_max = tong_max + ma_tran[0][j]
hang_max = 0
for i in range(1, m):
    tong_hang = 0
    for j in range(n):
        tong_hang = tong_hang + ma_tran[i][j]

    if tong_hang > tong_max:
        tong_max = tong_hang
        hang_max = i
print("Hàng có tổng lớn nhất là hàng:", hang_max)
print("Tổng lớn nhất là:", tong_max)
