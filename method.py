# Chức năng phát sinh thì hàm xử lý sẽ phát sinh (hàm thì sẽ trùng tên nhau, biến cũng vậy vì vậy khó bảo trì code về sau)

# Lưu thông tin sinh viên, tính điểm trung bình

ho_ten = 'Nguyễn Văn A'
diem_toan = 8
diem_ly = 9
diem_hoa = 10

def tinh_diem_trung_binh (diem_toan, diem_ly, diem_hoa):
    dtb = (diem_toan + diem_ly+ diem_hoa)/3
    return dtb

print(tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa))
