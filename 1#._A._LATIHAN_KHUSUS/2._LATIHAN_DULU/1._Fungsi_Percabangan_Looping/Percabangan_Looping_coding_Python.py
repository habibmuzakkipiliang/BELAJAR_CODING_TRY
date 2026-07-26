print ("\n Fungsi dengan Percabangan Dasar \n")

def dar (a):

     if a >= 5:
          print (f"Besar, angka a = {a}")

     else:
          print (f"Kecil, angka a = {a}")

dar (10)
dar (9)
dar (8)
dar (7)
dar (6)
dar (5)
dar (6)
dar (5)
dar (4)
dar (3)
dar (2)
dar (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan \n")

def run (n):

     if n >= 8:
          print (f"Besar, angka n = {n}")

     elif n >= 5:
          print (f"Tengah, angka n = {n}")

     else:
          print (f"Kecil, angka n = {n}")

run (10)
run (9)
run (8)
run (7)
run (6)
run (5)
run (4)
run (3)
run (2)
run (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Nilai Rapor \n")

def nilai (k): 

     if k >= 90:
          print (f"A, nilai = {k}")

     elif k >= 80:
          print (f"B, nilai = {k}")

     elif k >= 70:
          print (f"C, nilai = {k}")

     elif k >= 60:
          print (f"D, nilai = {k}")

     elif k >= 50:
          print (f"E, nilai = {k}")

     else:
          print (f"Nilai nya jelek, nilai = {k}")

nilai (100)
nilai (90)
nilai (80)
nilai (70)
nilai (60)
nilai (50)
nilai (40)
nilai (30)
nilai (20)
nilai (10)


print ("\n --- batas --- \n")




print ("\n usia produktif manusia \n")

def nus (x):

     if x >= 15 and x <= 50:
          print (f"Usia produktif, usia = {x}")

     elif x > 50:
          print (f"Usia sudah tua, usia = {x}")

     else:
          print (f"Belum masuk, usia = {x}")

nus (70)
nus (60)
nus (50)
nus (40)
nus (30)
nus (20)
nus (10)


print ("\n --- batas --- \n")




print ("\n Usia masuk JKT48 \n")

def jkt48 (j):

     if j >= 15 and j <= 18:
          print (f"Sudah boleh masuk jkt48, usia = {j}")

     elif j > 18:
          print (f"Sudah lebih dari cukup, usia = {j}")

     else:
          print (f"Masih kecil usianya, usia = {j}")

jkt48 (20)
jkt48 (19)
jkt48 (18)
jkt48 (17)
jkt48 (16)
jkt48 (15)
jkt48 (14)
jkt48 (13)
jkt48 (11)
jkt48 (12)


print ("\n --- batas --- \n")





print ("\n Fungsi dengan Usia Masuk JKT48 \n")

def run (s):

     if s >= 13 and s <= 19:
          print (f"Usia boleh masuk jkt48, usia = {s}")

     elif s > 19:
          print (f"Sudah boleh dari cukup, usia = {s}")

     else:
          print (f"Belum boleh ikut JKT48, usia = {s}")


run (60)
run (50)
run (40)
run (30)
run (20)
run (10)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Nested 1 \n")

def run (k):

     cek = True

     if k >= 5:
          if cek:
               print (f"Besar, angka k = {k}")

     else:
          print (f"Kecil, angka k = {k}")

run (7)
run (6)
run (5)
run (4)
run (3)
run (2)
run (1)


print ("\n --- batas --- \n")




print ("\n Usia masuk kerja \n")

def kerja (l):

     if l >= 23 and l <= 40:
          print (f"Boleh masuk kerja, usia = {l}")

     elif l > 40:
          print (f"Sudah pensiun, usia = {l}")

     else:
          print (f"Masih belum boleh kerja, usia = {l}")

kerja (50)
kerja (40)
kerja (30)
kerja (20)
kerja (10)


print ("\n --- batas --- \n")




print ("\n For Dasar \n")

for a in range (10):
     print (f"U ke - {a}")


print ("\n --- batas --- \n")




for b in range (1, 10):
     print (f"Urutan ke - {b}")



print ("\n --- batas --- \n")




print ("\n While dasar \n")

a = 1

while a < 11:
     print (f"Urutan ke - {a}")
     a = a + 1


print ("\n --- batas --- \n")



b = 10

while b > 0:
     print (f"Urutan ke - {b}")
     b = b - 1



print ("\n --- batas --- \n")




print ("\n For Nested \n")

for x in range (1, 4):
     for y in range (1, 4):
          print (f"Luar : {x}, Dalam : {y}")


print ("\n --- batas --- \n")




print ("\n Array \n")

daf = ["Jakarta", "Palembang", "Bandung", "Semarang", "Surabaya"]

for i in daf:
     print (i)



print ("\n Array 2 \n")

fr = ["Dam", "Ron", "var", "ror", "ner"]

fr.append ("Ranner")
fr.append ("Ron")
fr.append ("Ros")

for a in fr:
     print (a)


print ("\n --- batas --- \n")




print ("\n Dictionary \n")

data = {
     "nama" : "Hayyan Farras",
     "asal" : "Kota Serang",
     "usia" : 19,
     "kerja" : "Web Dev"
}

print ("Nama :", data ["nama"])
print ("Asal :", data ["asal"])
print ("Usia :", data ["usia"])
print ("Kerja :", data ["kerja"])


print ("\n --- batas --- \n")




print ("\n Dictionary 2 \n")

dat = {
     "nama" : "Rayyan Farras",
     "asal" : "Jakarta",
     "usia" : 19,
     "kerja" : "Web Dev",
}

print ("Nama :", dat ["nama"])
print ("Asal :", data ["asal"])
print ("Usia :", data ["usia"])
print ("Kerja :", data ["kerja"])


print ("\n --- batas --- \n")




print ("\n Dictionary 3 \n")

get = {
     "nama" : "John Doe",
     "asal" : "Amerika Serikat",
     "usia" : 19,
     "tinggi" : 190,
     "kerja" : "Web Dev",
}

print ("Nama :", get ["nama"])
print ("Asal :", get ["asal"])
print ("Tinggi :", get ["tinggi"])
print ("Kerja :", get ["kerja"])


print ("\n --- batas --- \n")




print ("\n Error Handling \n")

try:
     a = 10 / 0
     print (a)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Berhasil")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")




print ("\n Error Handling 2 \n")

try: 
     b = 10 + 10
     print (b)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Berhasil")

finally:
     print ("Selesai")