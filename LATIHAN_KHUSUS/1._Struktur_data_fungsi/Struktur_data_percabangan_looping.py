# for dasar

for j in range (15):
     print (f"urutan ke - {j}")


print ("\n --- batas --- \n")     



# for dasar 1

for a in range (1, 10):
     print (f"urutan ke - {a}")


print ("\n --- batas --- \n")



# While dasar

a = 1

while a < 16:
     print (f"urutan ke - {a}")
     a = a + 1


print ("\n --- batas --- \n")




# while dasar 2

b = 15

while b > 0:
     print (f"urutan ke - {b}")
     b = b - 1


print ("\n --- batas --- \n")



# For + Percabangan 

for i in range (1, 20):
     if i == 15:
          continue
     print (i)


print ("\n --- batas --- \n")




# for + percabangan

for h in range (1, 11):
     if h == 10:
          break
     print (h)


print ("\n --- batas --- \n")




# For + Percabangan Nested 

daftar = ["Sharingan", "Rinnegan", "Byakugan", "Tomoe Rinnegan"]

for mata in daftar:
     if mata == "Rinnegan":
          continue
     print (mata)


print ("\n --- batas --- \n")




# Array + For

er = ["Lone", "Itel", "Black Villager", "Minecraft", "Hun", "Hjun", "Loger", "Fun", "GUn"]

for j in er:
     if j == "Hun":
          break
     print (j)


print ("\n --- batas --- \n")



# Array Iterasi

negara = ["Amerika Serikat", "China", "Jepang", "Korea Selatan", "Inggris", "Prancis", "Spanyol"]

negara.append ("Italia")
negara.append ("Genoa")
negara.append ("Portugal")
negara.append ("Irlandia")
negara.append ("Belanda")
negara.append ("Indonesia")
negara.append ("Vietnam")

negara.sort ()

for j in negara:
     if j == "Korea Selatan":
          continue
     print (j)


print ("\n --- batas --- \n")





# Fungsi dengan return

def tambah (x, y):
     return x + y

def kurang (x, y):
     return x - y

def kali (x, y):
     return x * y

def bagi (x, y):
     return x + y

def pangkat (x, y):
     return x ** y


def modulus (x, y):
     return x % y

print ("Hasil tambah =", tambah (10, 5))
print ("Hasil kurang =", kurang (10, 5))
print ("Hasil kali =", kali (10, 4))
print ("Hasil pangkat =", pangkat (10, 6))
print ("Hasil bagi =", bagi (10, 2))
print ("Hasil modulus =", modulus (10, 5))


print ("\n --- batas --- \n")



# Fungsi dengan percabangan dasar

def dasar (x):

     if x >= 5:
          print (f"angka besar, angka a = {a}")

     else:
          print (f"angka kecil, angka a = {a}")

dasar (10)
dasar (9)
dasar (8)
dasar (7)
dasar (6)
dasar (5)
dasar (4)
dasar (3)
dasar (2)
dasar (1)



print ("\n --- batas --- \n")



# fungsi dengan percabangan dasar

x = "Iya"

def der (d):

     if x == "Iya":
          print ("Iya")

     else:
          print ("Tidak")

der ("Iya")
der ("Iya")
der ("Tidak")
der ("Tidak")
der ("Tidak")
der ("Iya")
der ("Iya")
der ("Tidak")
der ("Iya")
der ("Tidak")


print ("\n --- batas --- \n")





# For dasar

for i in range (11):
     print (f"urutan ke - {i}")


print ("\n --- batas --- \n")




for a in range (1, 20):
     print (f"urutan ke - {a}")

print ("\n --- batas --- \n")