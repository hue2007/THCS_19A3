import os

# 1. Tạo thư mục temp_files
os.makedirs("temp_files", exist_ok=True)

# 2. Trong thư mục temp_files, tạo tập tin file.txt
file_path = os.path.join("temp_files", "file.txt")
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Đây là tập tin tạm thời.")

# 3. Đổi tên file.txt thành new_file.txt trong thư mục temp_files
new_file_path = os.path.join("temp_files", "new_file.txt")
os.rename(file_path, new_file_path)

# 4. Di chuyển new_file.txt ra thư mục hiện tại
os.rename(new_file_path, "new_file.txt")

# 5. Xóa thư mục temp_files (sau khi đã di chuyển tập tin)
os.rmdir("temp_files")

print("Hoàn thành bài 8!")