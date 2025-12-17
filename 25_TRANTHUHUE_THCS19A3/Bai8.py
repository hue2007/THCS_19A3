n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    a.append(int(input("Nhập số: ")))
k = int(input("Nhập k: "))
k = k % n
for lan in range(k):
    cuoi = a[n - 1]
    i = n - 1
    while i > 0:
        a[i] = a[i - 1]
        i -= 1
    a[0] = cuoi
print("Danh sách sau khi dịch sang phải:")
for x in a:
    print(x, end=" ")
