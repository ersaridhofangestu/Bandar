import math

class ShapeModel:
    #ANCHOR -   -  1. Persegi
    def Keliling_Persegi(self,sisi = 0) -> int:
        return sisi * 4
    
    def Luas_Persegi(self,sisi = 0) -> int:
        return sisi * sisi
    
    #ANCHOR -  2. Persegi Panjang
    def Keliling_Persegi_Panjang(self,panjang = 0, lebar = 0) -> int:
        return 2 * (panjang + lebar)
    
    def Luas_Persegi_Panjang(self,panjang = 0, lebar = 0) -> int:
        return panjang * lebar
    
    #ANCHOR -  3. Jajar Genjang
    def Keliling_Jajar_Genjang(self,sisi_bawah = 0, sisi_kanan = 0,sisi_atas = 0,sisi_kiri = 0) -> int:
        return sisi_bawah + sisi_kanan + sisi_atas + sisi_kiri
    
    def Luas_Jajar_Genjang(self,alas = 0,  tinggi = 0) -> int:
        return tinggi * alas
    
    #ANCHOR -  4. Segitiga
    def Keliling_Segitiga(self, sisi_bawah = 0, sisi_kanan = 0,sisi_kiri = 0) -> int:
        return sisi_bawah + sisi_kanan + sisi_kiri
    
    def Luas_Segitiga(self, alas = 0, tinggi = 0) -> int:
        return 0.5 * tinggi * alas

    #ANCHOR -  5. Belah Ketupat
    def Keliling_Belah_Ketupat(self,sisi_bawah_kanan = 0, sisi_atas_kanan = 0,sisi_atas_kiri = 0,sisi_bawah_kiri = 0) -> int:
        return sisi_bawah_kanan +  sisi_atas_kanan + sisi_atas_kiri + sisi_bawah_kiri

    def Luas_Belah_Ketupat(self,diagonal1 = 0, diagonal2 = 0) -> int:
        return 0.5 * diagonal1 * diagonal2

    #ANCHOR -  6. Layang Layang
    def Keliling_Layang_layang(self, sisi_bawah_kanan = 0, sisi_atas_kanan = 0, sisi_atas_kiri = 0,sisi_bawah_kiri = 0) -> int:
        return sisi_bawah_kanan + sisi_atas_kanan + sisi_atas_kiri + sisi_bawah_kiri

    def Luas_Layang_layang(self,diagonal1 = 0, diagonal2 = 0) -> int:
        return 0.5 * diagonal1 * diagonal2
    
    #ANCHOR -  7. Trapesium
    def Keliling_Trapesium(self, sisi_bawah_kanan = 0, sisi_atas_kanan = 0, sisi_atas_kiri = 0,sisi_bawah_kiri = 0):
        return sisi_bawah_kanan + sisi_atas_kanan + sisi_atas_kiri + sisi_bawah_kiri

    def Luas_Trapesium(self,sisi_bawah = 0, sisi_atas = 0, tinggi = 0):
        return ((sisi_bawah + sisi_atas) /2) * tinggi 

    #SECTION -  8. Lingkaran
    def Keliling_Lingkaran(self, jari_jari):
        return 2 * math.pi * jari_jari 
    
    def Luas_Lingkaran(self, jari_jari):
        return math.pi * (jari_jari **2)