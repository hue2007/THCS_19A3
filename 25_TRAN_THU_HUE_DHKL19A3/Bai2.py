# Bài 2: Đếm tần suất xuất hiện của mỗi từ
# Bước 1: Đọc nội dung từ file
with open("vanban.txt", "r", encoding="utf-8") as tap_tin:
    noi_dung = tap_tin.read()

# Bước 2: Tách các từ
danh_sach_tu = noi_dung.split()

# Bước 3: Tạo từ điển lưu tần suất
tan_suat_tu = {}

for tu in danh_sach_tu:
    tu = tu.lower().strip(".,")
    if tu in tan_suat_tu:
        tan_suat_tu[tu] += 1
    else:
        tan_suat_tu[tu] = 1

# Bước 4: In kết quả
print("Tần suất xuất hiện của các từ:")
for tu, so_lan in tan_suat_tu.items():
    print(f"{tu}: {so_lan}")
