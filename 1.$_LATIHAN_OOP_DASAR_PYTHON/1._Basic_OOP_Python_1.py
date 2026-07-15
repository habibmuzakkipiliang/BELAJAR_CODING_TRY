class Mobil:
     
     def __init__(self, nama, asal):
          self.nama = nama
          self.asal = asal
              
     def aksi (self):
          print (f"- Mobil {self.nama}, berasal dari {self.asal}")
              
mobil_baru = Mobil ("Toyota", "Tangerang")
mobil_lama = Mobil ("Esemka", "Kota Solo")

mobil_baru.aksi ()
mobil_lama.aksi ()