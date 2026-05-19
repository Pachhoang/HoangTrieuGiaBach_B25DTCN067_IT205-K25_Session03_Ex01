print(" --- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG -- ")

# Vòng Lặp chạy 3 Lần dể nhập Lương cho 3 nhân viên
total_budget = 0
for employee_number in range(1, 4):

    print ("Đang xử lý nhân viên số", employee_number)
# Nhập mức lương
    salary = int(input (" Nhập mức lương (VNĐ): "))

# Thuc hien thao tac cong don tiền vao chiec hộp
    total_budget = total_budget + salary

# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình
print (" KET QUA: TONG NGAN SACH CAN CHUAN BI LA:", total_budget, "VND")