# Mở file vanban.txt để ghi nội dung
with open("vanban.txt", "w", encoding="utf-8") as f:
    f.write(
        "Python là một ngôn ngữ lập trình mạnh mẽ, dễ học và có nhiều ứng dụng. "
        "Nó được sử dụng rộng rãi trong phát triển web, khoa học dữ liệu, "
        "trí tuệ nhân tạo và tự động hóa."
    )

# Đọc toàn bộ nội dung trong file
with open("vanban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

# Tách các từ trong chuỗi
cac_tu = noi_dung.split()

# In tổng số từ
print("Tổng số từ trong tập tin là:", len(cac_tu))