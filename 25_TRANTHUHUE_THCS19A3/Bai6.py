n = int(input("Nhập số phần tử của danh sách: "))

tong_chan = 0
tong_le = 0

for i in range(n):
    so = int(input("Nhập số: "))
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so

print("Tổng các số chẵn là:", tong_chan)
print("Tổng các số lẻ là:", tong_le)

