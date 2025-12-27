n = int(input("Nhập số sinh viên: "))

sinh_vien = {}

# Nhập dictionary ban đầu
for i in range(n):
    ten = input("Nhập tên sinh viên: ")
    diem = int(input("Nhập điểm: "))
    sinh_vien[ten] = diem

# Nhóm theo điểm
nhom_theo_diem = {}

for ten in sinh_vien:
    diem = sinh_vien[ten]

    if diem not in nhom_theo_diem:
        nhom_theo_diem[diem] = [ten]
    else:
        nhom_theo_diem[diem] = nhom_theo_diem[diem] + [ten]

# In kết quả
print("Dictionary ban đầu:", sinh_vien)
print("Dictionary sau khi nhóm theo điểm:", nhom_theo_diem)
