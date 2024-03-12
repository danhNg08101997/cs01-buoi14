# from Nhan_Vien import Nhan_Vien
from models.Nhan_Vien import Nhan_Vien

class Cong_Ty:
    def __init__(self) -> None:
        self.ds_nhan_vien: list[Nhan_Vien] = []
        self.ten_cong_ty = ''
    def them_nhan_vien(self, nhan_vien_moi:Nhan_Vien):
        self.ds_nhan_vien.append(nhan_vien_moi)
    def xuat_thong_tin_nhan_vien(self):
        for nv in self.ds_nhan_vien:
            nv.xuat_thong_tin()
    def xoa_nhan_vien(self, ma_nhan_vien:str):
        for nv in self.ds_nhan_vien:
            if nv.ma_nhan_vien == ma_nhan_vien:
                self.ds_nhan_vien.remove(nv)
        # Gọi lại phương thức hiển thị sau khi xóa
        self.xuat_thong_tin_nhan_vien()