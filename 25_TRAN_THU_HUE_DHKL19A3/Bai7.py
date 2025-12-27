import os

# Tên thư mục gốc
thu_muc_goc = "my_project"

# 1. Tạo các thư mục
os.makedirs(os.path.join(thu_muc_goc, "src"), exist_ok=True)
os.makedirs(os.path.join(thu_muc_goc, "docs"), exist_ok=True)
os.makedirs(os.path.join(thu_muc_goc, "data"), exist_ok=True)

# 2. Tạo các tập tin rỗng
open(os.path.join(thu_muc_goc, "src", "main.py"), "w").close()
open(os.path.join(thu_muc_goc, "docs", "README.md"), "w").close()
open(os.path.join(thu_muc_goc, "data", "input.txt"), "w").close()

# 3. In ra cấu trúc thư mục ĐÚNG
print("my_project/")
for thu_muc in os.listdir(thu_muc_goc):
    print("├──", thu_muc + "/")
    duong_dan = os.path.join(thu_muc_goc, thu_muc)
    for tep in os.listdir(duong_dan):
        print("│   └──", tep)


