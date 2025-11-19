n = int(input("Nhập n: "))
S1 = 0
for i in range(1, n+1):
    S1 += i
S2 = 1
for i in range(1, n):
    S2 *= i
S3 = 0
for i in range(1, n+1):
    if i % 2 == 1:
        S3 += 1/i
    else:
        S3 -= 1/i
S4 = 0
for k in range(0, n+1):
    S4 += k / (k + 2)
print("Kết quả:")
print("S1 =", S1, ", S2 =", S2, ", S3 =", S3, ", S4 =", S4)