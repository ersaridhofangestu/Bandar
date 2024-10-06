import time

from src.shape_view import ShapeView
from src.shape_controller import ShapeController

def main():
      view = ShapeView()
      controller = ShapeController()
      while True :
            try:
                  time.sleep(1)
                  view.Menu_Bangun_Datar()
                  time.sleep(1)
                  bangun_datar = int(input('Silakan pilih bangun datar : '))
                  match bangun_datar :
                        case 1 :
                              controller.Formula_Persegi()  
                        case 2 :
                              controller.Formula_Persegi_Panjang()
                        case 3 :
                              controller.Formula_Jajar_Genjang()
                        case 4 :
                              controller.Formula_Segitiga()
                        case 5 :
                              controller.Formula_Belah_Ketupat()
                        case 6 :
                              controller.Formula_Layang_Layang()
                        case 7 :
                              controller.Formula_Trapesium()
                        case 8 :
                              controller.Formula_Lingkaran()
                        case 9 :
                              time.sleep(1)
                              exit()
            except ValueError:
                  view.Input_Invalid() 
                  

if __name__ == "__main__":
      main()