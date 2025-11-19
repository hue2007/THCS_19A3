tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
a = abs(tu)
b = abs(mau)
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
ucln = a
tu //= ucln
mau //= ucln
print("Phân số tối giản:", tu, "/", mau)
