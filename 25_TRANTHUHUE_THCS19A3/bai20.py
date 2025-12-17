n = int(input("Nhập số cặp key-value: "))

tu_dien = {}
# Nhập dictionary ban đầu
for i in range(n):
    key = input("Nhập key: ")
    value = int(input("Nhập value: "))
    tu_dien[key] = value

# Lọc theo điều kiện value > 50
tu_dien_loc = {}

for key in tu_dien:
    if tu_dien[key] > 50:
        tu_dien_loc[key] = tu_dien[key]

# In kết quả
print("Dictionary ban đầu:", tu_dien)
print("Dictionary sau khi lọc (value > 50):", tu_dien_loc)
