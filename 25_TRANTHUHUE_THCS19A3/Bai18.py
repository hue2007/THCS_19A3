n = int(input("Nhập số cặp key-value: "))

tu_dien = {}

# Nhập dictionary ban đầu
for i in range(n):
    key = int(input("Nhập key: "))
    value = int(input("Nhập value: "))
    tu_dien[key] = value

# Đảo ngược dictionary
tu_dien_dao = {}

for key in tu_dien:
    value = tu_dien[key]
    tu_dien_dao[value] = key

# In kết quả
print("Dictionary ban đầu:", tu_dien)
print("Dictionary sau khi đảo:", tu_dien_dao)







n = int(input("Số phần tử: "))
a = []

for i in range(n):
    a.append(int(input()))

t = tuple(a)

chan = []
le = []
tong_chan = 0
tong_le = 0

for x in t:
    if x % 2 == 0:
        chan.append(x)
        tong_chan += x
    else:
        le.append(x)
        tong_le += x

print("Tuple chẵn:", tuple(chan))
print("Tổng chẵn:", tong_chan)
print("Tuple lẻ:", tuple(le))
print("Tổng lẻ:", tong_le)

