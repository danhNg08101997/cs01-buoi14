# Yêu cầu: Viết chương trình tính lương và quản lý thông tin nhân viên bao gồm: ma_nhan_vien, ten_nhan_vien, so_dien_thoai, email, so_gio_lam_viec, luong_cb cho 1 công ty A.

from models.Cong_Ty import Cong_Ty
from models.Nhan_Vien import Nhan_Vien

cong_ty = Cong_Ty()
# Thiết kế menu
running = True
while running:
    print(f'''
          1/ Thêm nhân viên
          2/ Xóa nhân viên
          3/ Xuất thông tin nhân viên
          Bấm e/E để thoát chương trình
          ''')
    select = input('Chọn chức năng: ')
    if select == '1':
        nv = Nhan_Vien()
        nv.nhap_thong_tin()
        nv.xuat_thong_tin()
        # Thêm nhân viên vào công ty
        cong_ty.them_nhan_vien(nv)
    elif select == '2':
        ma_nhan_vien = input('Nhập vào mã nhân viên cần xóa: ')
        cong_ty.xoa_nhan_vien(ma_nhan_vien)
    elif select == '3':
        cong_ty.xuat_thong_tin_nhan_vien()
    elif select == 'e' or 'E':
        running = False