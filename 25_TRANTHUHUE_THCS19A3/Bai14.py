# Nhập set A
n = int(input("Nhập số phần tử của set A: "))
A = set()
for i in range(n):
    A.add(int(input("Nhập phần tử A: ")))

# Nhập set B
m = int(input("Nhập số phần tử của set B: "))
B = set()
for i in range(m):
    B.add(int(input("Nhập phần tử B: ")))

# A - B
print("Các phần tử thuộc A nhưng không thuộc B:")
for x in A:
    co_trong_B = False
    for y in B:
        if x == y:
            co_trong_B = True
            break
    if not co_trong_B:
        print(x, end=" ")
print()

# B - A
print("Các phần tử thuộc B nhưng không thuộc A:")
for x in B:
    co_trong_A = False
    for y in A:
        if x == y:
            co_trong_A = True
            break
    if not co_trong_A:
        print(x, end=" ")
print()

# A giao B
print("Các phần tử thuộc cả A và B:")
for x in A:
    for y in B:
        if x == y:
            print(x, end=" ")
print()

# A hợp B
print("Các phần tử thuộc A hoặc B:")
for x in A:
    print(x, end=" ")

for x in B:
    da_co = False
    for y in A:
        if x == y:
            da_co = True
            break
    if not da_co:
        print(x, end=" ")
