n = int(input("Nhập số phần tử của tuple: "))

# Nhập tuple ban đầu
tuple_ban_dau = ()
for i in range(n):
    so = int(input("Nhập số: "))
    tuple_ban_dau = tuple_ban_dau + (so,)

# Tạo tuple chẵn và lẻ
tuple_chan = ()
tuple_le = ()

tong_chan = 0
tong_le = 0

for x in tuple_ban_dau:
    if x % 2 == 0:
        tuple_chan = tuple_chan + (x,)
        tong_chan = tong_chan + x
    else:
        tuple_le = tuple_le + (x,)
        tong_le = tong_le + x

# In kết quả
print("Tuple ban đầu:", tuple_ban_dau)
print("Tuple các số chẵn:", tuple_chan)
print("Tổng các số chẵn:", tong_chan)
print("Tuple các số lẻ:", tuple_le)
print("Tổng các số lẻ:", tong_le)
