GIA_BAC_1 = 1678
GIA_BAC_2 = 1734
GIA_BAC_3 = 2014
so_kwh = float(input("Nhập số kWh điện đã tiêu thụ: "))
so_kwh_bac_1 = so_kwh * (so_kwh <= 100) + 100 * (so_kwh > 100)
so_kwh_bac_2 = (so_kwh - 100) * (so_kwh > 100) * (so_kwh <= 200) + 100 * (so_kwh > 200)
so_kwh_bac_3 = (so_kwh - 200) * (so_kwh > 200)
tien_bac_1 = so_kwh_bac_1 * GIA_BAC_1
tien_bac_2 = so_kwh_bac_2 * GIA_BAC_2
tien_bac_3 = so_kwh_bac_3 * GIA_BAC_3
tong_tien = tien_bac_1 + tien_bac_2 + tien_bac_3
print(f"Tổng tiền điện phải trả: {tong_tien:.0f} VNĐ")

