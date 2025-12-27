from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri

ds = [5, 2, 9, 1, 7]
print("Danh sách sau khi sắp xếp:", sap_xep_tang_dan(ds))

info = {"ten": "Hue", "lop": "DHKL19A3"}
print("Giá trị của khóa 'ten':", lay_gia_tri(info, "ten"))