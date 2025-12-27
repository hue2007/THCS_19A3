import sys
import os

# Thêm thư mục thu_vien_chung vào đường dẫn
duong_dan = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "thu_vien_chung")
)
sys.path.append(duong_dan)

from xu_ly_so import kiem_tra_so_nguyen_to

so = 17

if kiem_tra_so_nguyen_to(so):
    print(so, "là số nguyên tố")
else:
    print(so, "không phải là số nguyên tố")
