n = int(input("Nhập kích thước ma trận vuông n: "))
ma_tran = []
for i in range(n):
    dong = []
    for j in range(n):
        phan_tu = int(input("Nhập phần tử: "))
        dong.append(phan_tu)
    ma_tran.append(dong)

doi_xung = True
for i in range(n):
    for j in range(n):
        if ma_tran[i][j] != ma_tran[j][i]:
            doi_xung = False

if doi_xung:
    print("Ma trận là ma trận đối xứng")
else:
    print("Ma trận không phải là ma trận đối xứng")
