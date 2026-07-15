class Profil:
     
     def __init__(self, nama, asal):
          self.nama = nama
          self.asal = asal
          
     def aksi (self):
          print (f"- {self.nama} dan asal dari {self.asal}")
          
profil_1 = Profil ("Habib", "Kota Serang")

profil_1.aksi ()