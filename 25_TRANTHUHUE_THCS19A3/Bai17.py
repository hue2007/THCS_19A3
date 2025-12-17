n = int(input("Nhập số cặp key-value: "))

tu_dien = {}

# Nhập dictionary
for i in range(n):
    key = int(input("Nhập key: "))
    value = int(input("Nhập value: "))
    tu_dien[key] = value

# Tìm key có value lớn nhất
key_max = None
value_max = None

for key in tu_dien:
    if value_max is None or tu_dien[key] > value_max:
        value_max = tu_dien[key]
        key_max = key

print("Key có giá trị lớn nhất là:", key_max)
print("Giá trị lớn nhất là:", value_max)
