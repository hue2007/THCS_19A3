m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

ma_tran = []

# Nhập ma trận
for i in range(m):
    dong = []
    for j in range(n):
        dong.append(int(input("Nhập phần tử: ")))
    ma_tran.append(dong)

# Kiểm tra ma trận vuông
if m != n:
    print("Ma trận không phải là ma trận vuông nên không phải ma trận đơn vị")
else:
    la_don_vi = True

    for i in range(m):
        for j in range(n):
            if i == j:
                if ma_tran[i][j] != 1:
                    la_don_vi = False
            else:
                if ma_tran[i][j] != 0:
                    la_don_vi = False

    if la_don_vi:
        print("Ma trận là ma trận đơn vị")
    else:
        print("Ma trận không phải là ma trận đơn vị")
