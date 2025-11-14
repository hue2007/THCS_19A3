tong_keo = int(input("Nhập tổng số kẹo: "))
so_hoc_sinh = int(input("Nhập số học sinh: "))
keo_moi_hoc_sinh = tong_keo // so_hoc_sinh
keo_con_thua = tong_keo % so_hoc_sinh
print(f"Số kẹo mỗi học sinh nhận được: {keo_moi_hoc_sinh}")
print(f"Số kẹo còn thừa: {keo_con_thua}")