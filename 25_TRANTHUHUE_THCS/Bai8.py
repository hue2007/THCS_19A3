def tim_so_le_lon_nhat(a, b, c):
    le = [x for x in (a, b, c) if x % 2 == 1]
    if len(le) == 0:
        return -1
    return max(le)
print(tim_so_le_lon_nhat(2, 7, 10))
