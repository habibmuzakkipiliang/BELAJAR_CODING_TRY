class Motor:
     
     def __init__(self, nama, kecepatan):
          self.nama = nama
          self.kecepatan = kecepatan
          
     def unik (self):
          print (f"- Motor {self.nama} dan kecepatan {self.kecepatan} km / jam")
          
motor_1 = Motor ("Nmax", 20)
motor_2 = Motor ("Kawasaki", 30)

motor_1.unik ()
motor_2.unik ()