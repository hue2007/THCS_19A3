s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))

tu = ""
for c in s + " ":
    if c != " ":
        tu += c
    else:
        if len(tu) > n:
            print(tu)
        tu = ""
