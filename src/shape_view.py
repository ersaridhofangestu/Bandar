import math
from colorama import Fore, Style

class ShapeView:
    def Menu_Bangun_Datar(self) -> str:
        print(f'''
{Fore.YELLOW}{'-'*10+'+ Menu Bangun Datar +'+'-'*10}{Fore.RESET}
        
            1. Persegi
            2. Persegi Panjang
            3. Jajar Genjang
            4. Segitiga
            5. Belah Ketupat
            6. Layang Layang
            7. Trapesium
            8. Lingkaran
            9. Exit
            {Style.RESET_ALL}
              ''')
        
    def Menu_Formula(self) -> str:
        print(f'''
{Fore.YELLOW}{'-'*10+'+ Menu Bangun Datar +'+'-'*10}{Fore.RESET}
              
            1. Menghitung luas 
            2. Menghitung keliling 
            3. Exit
            {Style.RESET_ALL}
              ''')
        
    def Hasil_Persegi(self, sisi = 0, hasil = 0, keterangan = 0) -> str:
        if keterangan == 'luas':
            print(f'''

{'-'*10+'+ Persegi +'+'-'*10}
            
            {Fore.YELLOW}Diketahui:{Style.RESET_ALL}
            
                sisi = s = {sisi}cm
            
            {Fore.YELLOW}Ditanya:{Style.RESET_ALL} Luas Persegi ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL}
            
                l = s x s   =   {sisi} x {sisi}
                            =   {hasil}
            
{Fore.BLUE}Luas segitiga dengan sisi {sisi}cm adalah {hasil}cm
                {Style.RESET_ALL}''')
        else :
            print(f'''
            
{'-'*10+'+ Persegi +'+'-'*10}
            
            {Fore.YELLOW}Diketahui:{Style.RESET_ALL}
                sisi = s = {sisi}cm
            
            {Fore.YELLOW}Ditanya:{Style.RESET_ALL} keliling Persegi ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
                k = 4 x s   =    4 x {sisi}
                            =   {hasil}
            
{Fore.BLUE}Keliling segitiga dengan sisi {sisi}cm adalah {hasil}cm
                {Style.RESET_ALL}''')
    
    def Hasil_Persegi_Panjang(self, panjang = 0, lebar = 0, hasil = 0, keteranan = 0) -> str:
        if keteranan == 'luas' :
             print(f'''
{'-'*10+'+ Persegi Panjang +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL} 
            
                panjang = p = {panjang}cm
                lebar   = l = {lebar}cm
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL}  Luas Persegi Panjang ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL}  
            
                l = p x l   =   {panjang} x {lebar}
                            =   {hasil}
            
{Fore.BLUE}Luas segitiga dengan panjang {panjang}cm dan lebar {lebar}cm adalah {hasil}cm
                {Style.RESET_ALL}''')
        else:
            print(f'''
{'-'*10+'+ Persegi Panjang +'+'-'*10}
            
            {Fore.YELLOW}Ditahui:{Style.RESET_ALL} 
            
                panjang = p = {panjang}cm
                lebar   = l = {lebar}cm
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL}  Keliling Persegi Panjang ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL}  
            
                k = (2 x p) + (2 x l)   =   (2 x p) + (2 x l) 
                                        =   (2 x {panjang}) + (2 x {lebar})
                                        =   {panjang **2} + {lebar **2}
                                        =   {hasil}
                                                    
{Fore.BLUE}Keliling segitiga dengan panjang {panjang}cm dan lebar {lebar}cm adalah {hasil}cm
                {Style.RESET_ALL}''')
            
    def Hasil_Jajar_Genjang(self, alas = 0, tinggi = 0, sisi_bawah = 0, sisi_kanan = 0,sisi_atas = 0,sisi_kiri = 0, hasil = 0, keteranan ='') -> str:
        if keteranan == 'luas' :
            print(f'''
{'-'*10+'+ Jajar Genjang +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}
            
                alas   = a = {tinggi}cm
                tinggi = t = {alas}cm
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Luas Persegi Panjang ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
            
                l = a x t   =   {alas} x {tinggi}
                            =   {hasil}cm
            
{Fore.BLUE}Luas dengan alas {alas}cm, dan tinggi {tinggi} adalah {hasil}cm
                {Style.RESET_ALL}''')
        else:
            print(f'''
{'-'*10+'+ Jajar Genjang +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}
            
                sisi bawah = a = {sisi_bawah}cm
                sisi kanan = b = {sisi_kanan}cm
                sisi atas  = c = {sisi_atas}cm
                sisi kiri  = d = {sisi_kiri}cm
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Keliling Persegi Panjang ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
            
                k = a + b + c + d   =  {sisi_bawah} + {sisi_kanan} + {sisi_atas} + {sisi_kiri}
                                    =  {hasil}
{Fore.BLUE}Keliling dengan  sisi bawah {sisi_bawah}cm, sisi kanan {sisi_kanan}cm, sisi atas {sisi_atas}cm, dan sisi kiri {sisi_kiri}cm adalah {hasil}cm
                {Style.RESET_ALL}''')
            
    def Hasil_Segitiga(self,sisi_bawah = 0, sisi_kanan = 0,sisi_kiri = 0, alas = 0, tinggi = 0, hasil = 0, keteranan ='') -> str:
        if keteranan == 'luas' :
            print(f'''
{'-'*10+'+ Segitiga +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}
            
                alas   = a = {tinggi}cm
                tinggi = t = {alas}cm
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Luas Persegi Panjang ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 

                l = a x t   = 1/2 {alas} x {tinggi}
                            = {hasil}cm
            
{Fore.BLUE}Luas dengan alas {alas}cm, dan tinggi {tinggi} adalah {hasil}cm
                {Style.RESET_ALL}''')
        else:
            print(f'''
{'-'*10+'+ Segitiga +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}

                sisi bawah = a = {sisi_bawah}cm
                sisi kanan = b = {sisi_kanan}cm
                sisi kiri  = c = {sisi_kiri}cm
                
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Luas Persegi Panjang ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
            
                k = a + b + c   =   {sisi_bawah} + {sisi_kanan} + {sisi_kiri}
                                =   {hasil}cm
            
{Fore.BLUE}Keliling dengan  sisi bawah {sisi_bawah}cm, sisi kanan {sisi_kanan}cm, dan sisi kiri {sisi_kiri}cm adalah {hasil}cm
                {Style.RESET_ALL}''')
    
    def Hasil_Belah_Ketupat(self, sisi_bawah_kanan = 0, sisi_atas_kanan = 0,sisi_atas_kiri = 0,sisi_bawah_kiri = 0, diagonal1 = 0, diagonal2 = 0,hasil = 0, keteranan ='') -> str:
        if keteranan == 'luas' :
            print(f'''
{'-'*10+'+ Belah Ketupat +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}

                diagonal 1 = d1 = {diagonal1}
                diagonal 2 = d2 = {diagonal2}
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Luas Persegi Panjang ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
            
                l = 1/2 x d1 x d2   =   1/2 {diagonal1} x {diagonal2}
                                    =   {hasil}
            
{Fore.BLUE}Luas dengan diagonal 1 {diagonal1}cm, dan diagonal 2 {diagonal2}cm adalah {hasil}cm
                {Style.RESET_ALL}''')
        else:
            print(f'''
{'-'*10+'+ Belah Ketupat +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}
              
                sisi bawah kanan = a = {sisi_bawah_kanan}cm
                sisi atas kanan  = b = {sisi_atas_kanan}cm
                sisi atas kiri   = c = {sisi_atas_kiri}cm
                sisi bawah kiri  = d = {sisi_bawah_kiri}cm
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Luas Persegi Panjang ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 

                k = a + b + c + d    =   {sisi_bawah_kiri} + {sisi_atas_kanan} + {sisi_atas_kiri} + {sisi_bawah_kiri}
                                     =   {hasil}
            
{Fore.BLUE}Keliling dengan  sisi bawah kanan {sisi_bawah_kanan}cm, sisi atas kanan {sisi_atas_kanan}cm, sisi atas kiri {sisi_atas_kiri}cm , dan sisi bawah kiri {sisi_bawah_kiri}cm adalah {hasil}cm
                {Style.RESET_ALL}''')
            
    def Hasil_Layang_Layang(self, sisi_bawah_kanan = 0, sisi_atas_kanan = 0,sisi_atas_kiri = 0,sisi_bawah_kiri = 0, diagonal1 = 0, diagonal2=0,hasil = 0, keteranan ='') -> str:
        if keteranan == 'luas' :
            print(f'''
{'-'*10+'+ Layang-Layang +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}

                diagonal 1 = d1 = {diagonal1}
                diagonal 2 = d2 = {diagonal2}
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Luas Persegi Panjang ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
            
                l = 1/2 x d1 x d2   =   1/2 {diagonal1} x {diagonal2}
                                    =   {hasil}
            
{Fore.BLUE}Luas dengan diagonal 1 {diagonal1} dan diagonal 2 {diagonal2} adalah {hasil}cm
                {Style.RESET_ALL}''')
        else:
            print(f'''
{'-'*10+'+ Layang-Layang +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}

                sisi bawah kanan = a = {sisi_bawah_kanan} 
                sisi atas kanan  = b = {sisi_atas_kanan} 
                sisi atas kiri   = c = {sisi_atas_kiri} 
                sisi bawah kiri  = d = {sisi_bawah_kiri} 
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Keliling Layang-Layag ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
            
                l = a + b + c + d   =   {sisi_bawah_kanan} + {sisi_atas_kanan} + {sisi_atas_kiri} + {sisi_bawah_kiri}
                                    =   {hasil}
            
{Fore.BLUE}Kelilig dengan  sisi bawah kanan {sisi_bawah_kanan}cm, sisi atas kanan {sisi_atas_kanan}cm, sisi atas kiri {sisi_atas_kiri}cm , dan sisi bawah kiri {sisi_bawah_kiri}cm adalah {hasil}cm
                {Style.RESET_ALL}''')
    
            
    def Hasil_Trapesium(self, sisi_bawah_kanan = 0, sisi_atas_kanan = 0,sisi_atas_kiri = 0,sisi_bawah_kiri = 0, sisi_bawah = 0, sisi_atas = 0, tinggi = 0,hasil = 0, keteranan ='') -> str:
        if keteranan == 'luas' :
            print(f'''
{'-'*10+'+ Trapesium +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}

                sisi atas   = a = {sisi_atas} 
                sisi bawah  = b = {sisi_bawah} 
                sisi tinggi = c = {tinggi} 
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Keliling Layang-Layag ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
            
                l = ( ( a + b ) /2 ) x t    =   ( ( {sisi_atas + sisi_bawah} ) /2 ) x 4
                                            =   {hasil}
{Fore.BLUE}Luas dengan sisi bawah {sisi_bawah}cm, sisi atas {sisi_atas}cm dan tinggi {tinggi} adalah {hasil}cm
                {Style.RESET_ALL}''')
        else:
            print(f'''
{'-'*10+'+ Trapesium +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}

                sisi bawah kanan = a = {sisi_bawah_kanan} 
                sisi atas kanan  = b = {sisi_atas_kanan} 
                sisi atas kiri   = c = {sisi_atas_kiri} 
                sisi bawah kiri  = d = {sisi_bawah_kiri} 
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Keliling Layang-Layag ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
            
                k = a + b + c + d   =   {sisi_bawah_kanan} + {sisi_atas_kanan} + {sisi_atas_kiri} + {sisi_bawah_kiri}
                                    =   {hasil}cm

{Fore.BLUE}Keliling dengan sisi bawah kanan {sisi_bawah_kanan}cm, sisi atas kanan {sisi_atas_kanan}cm, sisi atas kiri {sisi_atas_kiri} dan sisi bawah kiri {sisi_bawah_kiri} adalah {hasil}cm
                {Style.RESET_ALL}''')
    
    
    def Hasil_Lingkaran(self, jari_jari ,hasil = 0, keteranan ='') -> str:
        if keteranan == 'luas' :
            print(f'''
{'-'*10+'+ Lingkaran +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}

                sisi jari-jari = r = {jari_jari} 
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Luas Layang-Layag ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
            
                l = π x r x r   =  {float(math.pi)} x {jari_jari} x {jari_jari}  
                                =  {hasil}

{Fore.BLUE}Luas dengan jari-jari {jari_jari} adalah {hasil}
                {Style.RESET_ALL}''')
        else:
            print(f'''
{'-'*10+'+ Lingkaran +'+'-'*10}

            {Fore.YELLOW}Ditahui:{Style.RESET_ALL}

                sisi jari-jari = r = {jari_jari} 
            
            {Fore.YELLOW}Tanya:{Style.RESET_ALL} Luas Layang-Layag ?
            
            {Fore.YELLOW}Jawab:{Style.RESET_ALL} 
            
                k = 2 x π x r x r   =   2 x {float(math.pi)} x {jari_jari}  
                                    =   {hasil}

{Fore.BLUE}Luas dengan jari-jari {jari_jari} adalah {hasil}
                {Style.RESET_ALL}''')
    
    
    def Input_Invalid(self):
        print(f'''{Fore.RED}
            Maaf input tidak sesuai
               {Style.RESET_ALL} ''') 