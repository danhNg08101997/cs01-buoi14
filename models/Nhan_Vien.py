class Nhan_Vien:
    def __init__(self) -> None:
        self.ma_nhan_vien = ''
        self.ten_nhan_vien = ''
        self.email = ''
        self.so_dien_thoai = ''
        self.so_gio_lam = 0
        self.luong_co_ban = 0
    def nhap_thong_tin(self):
        self.ma_nhan_vien = input('Nhập vào mã nhân viên: ')
        self.ten_nhan_vien = input('Nhập vào tên nhân viên: ')
        self.email = input('Nhập vào email: ')
        self.so_dien_thoai = input('Nhập vào số điện thoại: ')
        self.so_gio_lam = float(input('Nhập vào số giờ làm: '))
        self.luong_co_ban = float(input('Nhập vào lương cơ bản: '))
    def tinh_luong(self):
        tong_luong = self.so_gio_lam * self.luong_co_ban
        return tong_luong
    def xuat_thong_tin(self):
        print(f''' 
              Mã nhân viên: {self.ma_nhan_vien}
              Tên nhân viên: {self.ten_nhan_vien}
              Tổng lương: {self.tinh_luong()}
              ''')