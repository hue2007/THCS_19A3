chuoi = input("Nhập chuỗi: ")

tan_suat = {}

for ky_tu in chuoi:
    if ky_tu in tan_suat:
        tan_suat[ky_tu] = tan_suat[ky_tu] + 1
    else:
        tan_suat[ky_tu] = 1

print("Tần suất xuất hiện của các ký tự là:")
for ky_tu in tan_suat:
    print(ky_tu, ":", tan_suat[ky_tu])
