m = int(input("Nhập số hàng của ma trận A: "))
n = int(input("Nhập số cột của ma trận A: "))
A = []
for i in range(m):
    dong = []
    for j in range(n):
        dong.append(int(input("Nhập phần tử A: ")))
    A.append(dong)
p = int(input("Nhập số hàng của ma trận B: "))
q = int(input("Nhập số cột của ma trận B: "))

B = []
for i in range(p):
    dong = []
    for j in range(q):
        dong.append(int(input("Nhập phần tử B: ")))
    B.append(dong)
if n != p:
    print("Hai ma trận không nhân được")
else:
    C = []
    for i in range(m):
        dong = []
        for j in range(q):
            dong.append(0)
        C.append(dong)
    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    print("Ma trận kết quả là:")
    for i in range(m):
        for j in range(q):
            print(C[i][j], end=" ")
        print()
