class Kucing:
     
     def __init__(self, nama, warna):
          self.nama = nama
          self.warna = warna         
     
     def aksi (self):
          print (f"- Kucing kamu {self.nama}, dan berwarna {self.warna}, bunyi nya Miaw Miaw")
 
kucing_lucu = Kucing ("Fan", "Hitam")
kucing_imut = Kucing ("Rayyan", "Abu-abu")
kucing_kecil = Kucing ("Lian", "Putih")

kucing_imut.aksi ()
kucing_kecil.aksi ()
kucing_lucu.aksi ()


print ("\n --- batas --- \n")