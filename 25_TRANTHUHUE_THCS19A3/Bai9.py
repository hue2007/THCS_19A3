n = int(input("Nhập số hàng (cũng là số cột): "))
ma_tran = []
for i in range(n):
    dong = []
    for j in range(n):
        phan_tu = int(input("Nhập phần tử: "))
        dong.append(phan_tu)
    ma_tran.append(dong)
tong = 0
for i in range(n):
    tong = tong + ma_tran[i][n - 1 - i]

print("Tổng các phần tử trên đường chéo phụ là:", tong)


