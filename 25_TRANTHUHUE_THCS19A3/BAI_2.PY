a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
a = abs(a)
b = abs(b)
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print("Ước chung lớn nhất là:", a)
