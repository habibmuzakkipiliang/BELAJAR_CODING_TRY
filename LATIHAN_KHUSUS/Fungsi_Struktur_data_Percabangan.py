# Struktur data

daf = [
     "Halo Dunia",
     "Halo World",
     "Halo Fets",
     "Halo Jundy",
     "Halo Gundy",
     "Halo Rundy",
]

for j in daf:
     print (j)


print ("\n --- batas --- \n")



# Array 1

fer = [
     "Halo Dunk",
     "Halo Dri",
     "Halo dun",
     "Halo Der",
     "Halo Wer",
     "Halo Qwe",
     "Halo Ban",
     "Halo Dun"
]

for u in fer:
     print (u)


print ("\n --- batas --- \n")




# Array 3

ger = [
     "Halo Der",
     "Halo Dun",
     "Halo Zhong",
     "Halo Wei",
     "Halo Er Wei",
     "Halo Der",
     "Halo Fer", 
]

ger.append ("Halo hun")
ger.append ("Halo der")
ger.append ("Halo run")
ger.append ("Halo fer")
ger.append ("Halo Fen")
ger.append ("Halo Der")
ger.append ("Halo Dun")

for j in ger:
     if j == "Halo Fer":
          continue
     print (j)


print ("\n --- batas --- \n")




# Array + For

gun = [
     "Halo Dun",
     "Halo Lip",
     "Halo Der",
     "Halo dun",
     "halo dun",
     "afer",
     "fert",
     "gert"
]

gun.append ("Halo Dunf")
gun.append ("Halo Der")
gun.append ("Halo Dek")
gun.append ("Halo Det")
gun.append ("Halo Qwe")

for i in gun:
     if i == "Gert":
          continue
     print (i)


print ("\n --- batas --- \n")




# For end 

fet = [
     "Halo Dun",
     "Sky",
     "Hun",
     "Hunk",
     "Junk",
     "Funn",
     "Gunn",
]

for h in fet:
     if h == "Junk":
          break
     print (h)


print ("\n --- batas --- \n")





# Fungsi dasar

def dasar ():
     print ("Hello World")

dasar ()


print ("\n --- batas --- \n")




# Fungsi dengan parameter

def nama (sapa):
     print (f"Halo nama saya {sapa} dari Jakarta Timur")

nama ("Roni")
nama ("Romi")
nama ("Yanzheng")
nama ("Ron")
nama ("Fan")
nama ("Yan")
nama ("Fest")


print ("\n --- batas --- \n")



# Fungsi return

def run (sapa):
     return f"Halo saya {sapa} dari Kota Tegal"

print (run ("Hayyan"))
print (run ("Hafan"))
print (run ("Hun"))
print (run ("Fun"))
print (run ("Der"))


print ("\n --- batas --- \n")


# Fungsi return dengan operator dasar

def tambah (x, y):
     return x + y


def kurang (x, y):
     return x - y


def kali (x, y):
     return x * y


def bagi (x, y):
     return x / y


print ("Hasil tambah =", tambah (10, 9))
print ("Hasil kurang =", kurang (10, 5))
print ("Hasil kali =", kali (10, 10))
print ("Hasil bagi =", bagi (10, 4))


print ("\n --- bataas --- \n")




# Error Handling

try:
     a = 10 + 10
     print (a)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Oke")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")




# Error Handling

try:
     b = 10 / 0
     print (b)


except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Oke")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")



# Fungsi dengan percabangan dasar

def der (f):

     if f >= 5:
          print (f"angka f besar, angka f = {f}")

     else:
          print (f"angka f kecil, angka f = {f}")

der (10)
der (9)
der (8)
der (4)
der (3)
der (2)
der (1)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan nested

def erun (e):

     cek = True

     if e >= 5:
          if cek:
               print (f"angka e besar, angka e = {e}")

          else:
               print (f"angka e tengah, angka e = {e}")

     else:
          print (f"angka e kecil, angka e = {e}")

erun (10)
erun (9)
erun (8)
erun (7)
erun (6)
erun (5)
erun (4)
erun (3)
erun (2)
erun (1)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan error handling

def eror (f):

     try:

          if f < 0:
               raise Exception ("Angka minus")

          if f >= 8:
               print (f"angka f besar, angka f = {f}")

          elif f >= 5:
               print (f"angka f tengah, angka f = {f}")

          else:
               print (f"angka f kecil, angka f = {f}")

     except:
          print (f"angka minus, angka f = {f}")

eror (-10)
eror (-44)
eror (-2)
eror (-45)
eror (-5)
eror (10)
eror (9)
eror (5)


print ("\n --- batas --- \n")



# OOP dasar

class Mobil:

     def __init__(self, nama, asal):
          self.nama = nama
          self.asal = asal

     def aksi (self):
          print (f"Mobil {self.nama} dengan asal daerah dari {self.asal}")

hasil_1 = Mobil ("Roy", "Tegal")

hasil_1.aksi ()


print ("\n --- batas --- \n")