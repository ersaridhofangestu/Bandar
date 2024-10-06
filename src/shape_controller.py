import time

from src.shape_view import ShapeView
from src.shape_model import ShapeModel 

class ShapeController :
    def __init__(self):
        self.time = time
        self.view = ShapeView()
        self.model = ShapeModel()
        pass
        
    def Lanjut_Formula(self) -> bool:
        try:  
            self.time.sleep(1)
            loop = input('\nApakah anda ingin melihat formula [y/n] : ')
            if loop == 'y' or loop == 'n' :
                if loop == 'n' :
                    exit() 
                else: 
                    return False
            else :             
                self.time.sleep(1)
                self.view.Input_Invalid() 
                self.time.sleep(1)
                exit()
        except ValueError :
            self.time.sleep(1)
            self.view.Input_Invalid()
    
    def Formula_Persegi(self):
        try:
            while True :
                self.time.sleep(1)
                self.view.Menu_Formula()
                self.time.sleep(1)
                formula = int(input('Silakan pilih formula : '))
                match formula :
                    case 1 :
                        self.time.sleep(1)
                        sisi = int(input('\nSilakan masukan nilai sisi : '))
                        hasil = self.model.Luas_Persegi(sisi=sisi)
                        self.time.sleep(1)
                        self.view.Hasil_Persegi(sisi=sisi,hasil=hasil,keterangan='luas')
                        formula = self.Lanjut_Formula()
                    case 2 :
                        self.time.sleep(1)
                        sisi = int(input('\nSilakan masukan nilai sisi : '))
                        hasil = self.model.Keliling_Persegi(sisi=sisi)
                        self.time.sleep(1)
                        self.view.Hasil_Persegi(sisi=sisi, hasil=hasil,keterangan='keliling')
                        formula = self.Lanjut_Formula()
                             
                    case 3 :
                        break  
                    case _ :
                        self.time.sleep(1)
                        self.view.Input_Invalid() 
                        self.time.sleep(1)
        except ValueError :
            self.view.Input_Invalid() 
            
    def Formula_Persegi_Panjang(self) :
        try:
            while True :
                self.time.sleep(1)
                self.view.Menu_Formula()
                self.time.sleep(1)
                formula = int(input('Silakan pilih formula : '))
                match formula :

                    case 1 :
                        self.time.sleep(1)
                        panjang = int(input('\nSilakan masukan nilai panjang :'))
                        lebar = int(input('Silakan masukan nilai lebar :'))
                        hasil = self.model.Luas_Persegi_Panjang(panjang=panjang, lebar=lebar)
                        self.time.sleep(1)
                        self.view.Hasil_Persegi_Panjang(panjang=panjang, lebar=lebar, hasil=hasil,keteranan='luas')
                        formula = self.Lanjut_Formula()
                        
                    case 2 :
                        self.time.sleep(1)
                        panjang = int(input('\nSilakan masukan nilai panjang :'))
                        lebar = int(input('Silakan masukan nilai lebar :'))
                        hasil = self.model.Keliling_Persegi_Panjang(lebar=lebar,panjang=panjang)
                        self.time.sleep(1)
                        self.view.Hasil_Persegi_Panjang(panjang=panjang,lebar=lebar, hasil=hasil,keteranan='keliling')
                        formula = self.Lanjut_Formula()
                             
                    case 3 :
                        break
                             
                    case _ :
                        self.time.sleep(1)
                        self.view.Input_Invalid() 
                        self.time.sleep(1)
        except ValueError :
            self.view.Input_Invalid() 
            
    def Formula_Jajar_Genjang(self) :
        try:
            while True :
                self.time.sleep(1)
                self.view.Menu_Formula()
                self.time.sleep(1)
                formula = int(input('Silakan pilih formula : '))
                match formula :

                    case 1 :
                        self.time.sleep(1)
                        alas = int(input('\nSilakan masukan nilai alas : '))
                        tinggi = int(input('Silakan masukan nilai tinggi : '))
                        hasil = self.model.Luas_Jajar_Genjang(alas=alas, tinggi=tinggi)
                        self.time.sleep(1)
                        self.view.Hasil_Jajar_Genjang(alas=alas, tinggi=tinggi, hasil=hasil,keteranan='luas')
                        formula = self.Lanjut_Formula()
                        
                    case 2 :
                        self.time.sleep(1)
                        sisi_bawah = int(input('\nSilakan masukan nilai sisi bawah :'))
                        sisi_kanan = int(input('Silakan masukan nilai sisi kanan :'))
                        sisi_atas = int(input('Silakan masukan nilai sisi atas :'))
                        sisi_kiri = int(input('Silakan masukan nilai sisi kiri :'))
                        hasil = self.model.Keliling_Jajar_Genjang(sisi_bawah, sisi_kanan,sisi_atas,sisi_kiri)
                        self.time.sleep(1)
                        self.view.Hasil_Jajar_Genjang(sisi_bawah=sisi_bawah, sisi_kanan=sisi_kiri, sisi_atas=sisi_atas, sisi_kiri=sisi_atas, hasil=hasil ,keteranan='keliling')
                        formula = self.Lanjut_Formula()

                    case 3 :
                        break
                             
                    case _ :
                        self.time.sleep(1)
                        self.view.Input_Invalid() 
                        self.time.sleep(1)
        except ValueError :
            self.view.Input_Invalid() 
            
    def Formula_Segitiga(self) :
        try:
            while True :
                self.time.sleep(1)
                self.view.Menu_Formula()
                self.time.sleep(1)
                formula = int(input('Silakan pilih formula : '))
                match formula :

                    case 1 :
                        self.time.sleep(1)
                        alas = int(input('\nSilakan masukan nilai alas : '))
                        tinggi = int(input('Silakan masukan nilai tinggi : '))
                        hasil = self.model.Luas_Segitiga(alas=alas, tinggi=tinggi)
                        self.time.sleep(1)
                        self.view.Hasil_Segitiga(alas=alas, tinggi=tinggi, hasil=hasil,keteranan='luas')
                        formula = self.Lanjut_Formula()
                        
                    case 2 :
                        self.time.sleep(1)
                        sisi_bawah = int(input('\nSilakan masukan nilai sisi bawah :'))
                        sisi_kanan = int(input('Silakan masukan nilai sisi kanan :'))
                        sisi_kiri = int(input('Silakan masukan nilai sisi kiri :'))
                        hasil = self.model.Keliling_Segitiga(sisi_bawah=sisi_bawah, sisi_kanan=sisi_kanan ,sisi_kiri=sisi_kiri)
                        self.time.sleep(1)
                        self.view.Hasil_Jajar_Genjang(sisi_bawah=sisi_bawah, sisi_kanan=sisi_kanan ,sisi_kiri=sisi_kiri, hasil=hasil ,keteranan='keliling')
                        formula = self.Lanjut_Formula()
                           
                    case 3 :
                        break
                             
                    case _ :
                        self.time.sleep(1)
                        self.view.Input_Invalid() 
                        self.time.sleep(1)
        except ValueError :
            self.view.Input_Invalid()
            
    def Formula_Belah_Ketupat(self) :
        try:
            while True :
                self.time.sleep(1)
                self.view.Menu_Formula()
                self.time.sleep(1)
                formula = int(input('Silakan pilih formula : '))
                match formula :

                    case 1 :
                        self.time.sleep(1)
                        diagonal1 = int(input('\nSilakan masukan nilai diagonal 1 : '))
                        diagonal2 = int(input('Silakan masukan nilai diagonal 2 : '))
                        hasil = self.model.Luas_Belah_Ketupat(diagonal1=diagonal1,diagonal2=diagonal2)
                        self.time.sleep(1)
                        self.view.Hasil_Belah_Ketupat(diagonal1=diagonal1,diagonal2=diagonal2,hasil=hasil,keteranan='luas')
                        formula = self.Lanjut_Formula()
                        
                    case 2 :
                        self.time.sleep(1)
                        sisi_bawah_kanan = int(input('\nSilakan masukan nilai sisi bawah :'))
                        sisi_atas_kanan = int(input('Silakan masukan nilai sisi kanan :'))
                        sisi_atas_kiri = int(input('Silakan masukan nilai sisi atas :'))
                        sisi_bawah_kiri = int(input('Silakan masukan nilai sisi kiri :'))
                        hasil = self.model.Keliling_Belah_Ketupat(sisi_bawah_kanan=sisi_bawah_kanan, sisi_atas_kanan=sisi_atas_kanan,sisi_atas_kiri=sisi_atas_kiri,sisi_bawah_kiri=sisi_bawah_kiri)
                        self.time.sleep(1)
                        self.view.Hasil_Belah_Ketupat(sisi_bawah_kanan=sisi_bawah_kanan, sisi_atas_kanan=sisi_atas_kanan,sisi_atas_kiri=sisi_atas_kiri,sisi_bawah_kiri=sisi_bawah_kiri, hasil=hasil ,keteranan='keliling')
                        formula = self.Lanjut_Formula()
                             
                    case 3 :
                        break
                             
                    case _ :
                        self.time.sleep(1)
                        self.view.Input_Invalid() 
                        self.time.sleep(1)
                        exit()
        except ValueError :
            self.view.Input_Invalid()
            
    def Formula_Layang_Layang(self) :
        try:
            while True :
                self.time.sleep(1)
                self.view.Menu_Formula()
                self.time.sleep(1)
                formula = int(input('Silakan pilih formula : '))
                match formula :

                    case 1 :
                        self.time.sleep(1)
                        diagonal1 = int(input('\nSilakan masukan nilai diagonal 1 : '))
                        diagonal2 = int(input('Silakan masukan nilai diagonal 2 : '))
                        hasil = self.model.Luas_Layang_layang(diagonal1 = diagonal1, diagonal2 = diagonal2)
                        self.time.sleep(1)
                        self.view.Hasil_Belah_Ketupat(diagonal1=diagonal1,diagonal2=diagonal2,hasil=hasil,keteranan='luas')
                        formula = self.Lanjut_Formula()
                        
                    case 2 :
                        self.time.sleep(1)
                        sisi_bawah_kanan = int(input('\nSilakan masukan nilai sisi bawah kanan :'))
                        sisi_atas_kanan = int(input('Silakan masukan nilai sisi atas kanan :'))
                        sisi_atas_kiri = int(input('Silakan masukan nilai sisi atas kiri :'))
                        sisi_bawah_kiri = int(input('Silakan masukan nilai sisi bawah kiri :'))
                        hasil = self.model.Keliling_Layang_layang(sisi_bawah_kanan=sisi_bawah_kanan, sisi_atas_kanan=sisi_atas_kanan,sisi_atas_kiri=sisi_atas_kiri,sisi_bawah_kiri=sisi_bawah_kiri)
                        self.time.sleep(1)
                        self.view.Hasil_Layang_Layang(sisi_bawah_kanan=sisi_bawah_kanan, sisi_atas_kanan=sisi_atas_kanan, sisi_atas_kiri=sisi_atas_kiri, sisi_bawah_kiri=sisi_atas_kanan, hasil=hasil, keteranan='keliling')
                        formula = self.Lanjut_Formula()

                    case 3 :
                        break
                             
                    case _ :
                        self.time.sleep(1)
                        self.view.Input_Invalid() 
                        self.time.sleep(1)
        except ValueError :
            self.view.Input_Invalid()
            
    def Formula_Trapesium(self) :
        try:
            while True :
                self.time.sleep(1)
                self.view.Menu_Formula()
                self.time.sleep(1)
                formula = int(input('Silakan pilih formula : '))
                match formula :

                    case 1 :
                        self.time.sleep(1)
                        sisi_bawah = int(input('\nSilakan masukan nilai sisi bawah : '))
                        sisi_atas = int(input('Silakan masukan nilai sisi bawah atas :'))
                        tinggi = int(input('Silakan masukan nilai sisi tinggi :'))
                        hasil = self.model.Luas_Trapesium(sisi_bawah=sisi_bawah, sisi_atas=sisi_atas , tinggi=tinggi)
                        self.time.sleep(1)
                        self.view.Hasil_Trapesium(sisi_bawah=sisi_bawah, sisi_atas=sisi_atas, tinggi=tinggi,hasil=hasil,keteranan='luas')
                        formula = self.Lanjut_Formula()
                        
                    case 2 :
                        self.time.sleep(1)
                        sisi_bawah_kanan = int(input('\nSilakan masukan nilai sisi bawah kanan :'))
                        sisi_atas_kanan = int(input('Silakan masukan nilai sisi atas kanan :'))
                        sisi_atas_kiri = int(input('Silakan masukan nilai sisi atas kiri :'))
                        sisi_bawah_kiri = int(input('Silakan masukan nilai sisi bawah kiri :'))
                        hasil = self.model.Keliling_Trapesium(sisi_bawah_kanan=sisi_bawah_kanan, sisi_atas_kanan=sisi_atas_kanan,sisi_atas_kiri=sisi_atas_kiri,sisi_bawah_kiri=sisi_bawah_kiri)
                        self.time.sleep(1)
                        self.view.Hasil_Trapesium(sisi_bawah_kanan=sisi_bawah_kanan,sisi_atas_kanan=sisi_atas_kanan, sisi_atas_kiri=sisi_atas_kiri,sisi_bawah_kiri=sisi_bawah_kiri,hasil=hasil,keteranan='keliling')
                        formula = self.Lanjut_Formula()
                           
                    case 3 :
                        break
                             
                    case _ :
                        self.time.sleep(1)
                        self.view.Input_Invalid() 
                        self.time.sleep(1)
        except ValueError :
            self.view.Input_Invalid()   
            
    def Formula_Lingkaran(self) :
        try:
            while True :
                self.time.sleep(1)
                self.view.Menu_Formula()
                self.time.sleep(1)
                formula = int(input('Silakan pilih formula : '))
                match formula :

                    case 1 :
                        self.time.sleep(1)
                        jari_jari = int(input('\nSilakan masukan nilai jari-jari : '))
                        hasil = self.model.Luas_Lingkaran(jari_jari=jari_jari)
                        self.time.sleep(1)
                        self.view.Hasil_Lingkaran(jari_jari=jari_jari,hasil=hasil,keteranan='luas')
                        formula = self.Lanjut_Formula()
                        
                    case 2 :
                        self.time.sleep(1)
                        jari_jari = int(input('\nSilakan masukan nilai jari-jari : '))
                        hasil = self.model.Keliling_Lingkaran(jari_jari=jari_jari)
                        self.time.sleep(1)
                        self.view.Hasil_Lingkaran(jari_jari=jari_jari,hasil=hasil,keteranan='keliling')
                        formula = self.Lanjut_Formula()
                        
                    case 3 :
                        break
                    
                    case _ :
                        self.time.sleep(1)
                        self.view.Input_Invalid() 
                        self.time.sleep(1)
        except ValueError :
            self.view.Input_Invalid()   
            
            
            
            
            
            
            
            
            
            
            
            