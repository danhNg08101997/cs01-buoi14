# Tạo class(lớp) đối tượng (tạo ra 1 format object cho 1 biến Sinh_Vien)
class Sinh_Vien:
    # Hàm init là hàm khởi tạo
    def __init__(self) -> None:
        self.ho_ten = ''
        self.diem_toan = 0
        self.diem_ly = 0
        self.diem_hoa = 0
    def tinh_diem_trung_binh(self):
        dtb = (self.diem_toan + self.diem_ly + self.diem_hoa)/3
        return dtb

# Tạo đối tượng (1 biến lưu được nhiều giá trị)
sv = Sinh_Vien()
sv.ho_ten = "Nguyễn Văn A"
sv.diem_toan = 8
sv.diem_ly = 7
sv.diem_hoa = 6
print(sv.tinh_diem_trung_binh())

sv2 = Sinh_Vien()

# Dict: khi cập nhật thuộc tính thì phải cập nhật thủ công và dict không quản lý hàm tốt
sv_dict = {
    'ho_ten':'Nguyen Van B',
    'diem_toan': 9,
    'diem_ly': 4,
    'diem_hoa': 4
}