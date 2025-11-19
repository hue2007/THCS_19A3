n = int(input("Nhập n: "))
print("Các số nguyên tố nhỏ hơn", n, ": ", end="")
for x in range(2, n):
    dem_uoc = 0
    for i in range(1, x + 1):
        if x % i == 0:
            dem_uoc += 1
    if dem_uoc == 2:   
        print(x, end=" ")