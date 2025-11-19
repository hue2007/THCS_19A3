n = int(input("Nhập vào số n: "))
i = 1
while i*i < n:
    i = i + 1
if i*i == n:
    print("Là số chính phương")
else:
    print("Không phải số chính phương")