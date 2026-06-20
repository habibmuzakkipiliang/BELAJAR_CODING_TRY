# Teknik Perulangan Fungsi Modular

print ("\n Teknik Perulangan Fungsi Modular \n")


print ("\n Perulangan dasar 1 \n")

for a in range (1, 11):
     print (f"Urutan ke - {a}")
     
print ("\n --- Batas --- \n")




print ("\n Perulangan dasar 2 \n")

for b in range (10, 21):
     print (f"Urutan ke - {b}")
   
     
print ("\n --- Batas --- \n")




print ("\n For Perulangan \n")

for c in range (15):
     print (f"Urutan ke - {c}")
     

print ("\n --- Batas --- \n")




print ("\n While Perulangan \n")

a = 10

while a < 25:
     print (f"Urutan ke - {a}")
     a = a + 1
     
     
print ("\n --- Batas --- \n")




print ("\n While Perulangan \n")

b = 15

while b < 25:
     print (f"Urutan ke - {b}")
     b = b + 1
     
     
print ("\n --- Batas --- \n")



print ("\n While Perulangan 3 \n")

c = 15

while c < 26:
     print (f"urutan ke - {c}")
     c = c + 1
     
     
print ("\n --- Batas --- \n")    



print ("\n While Perulangan 4 \n")

d = 10

while d > 0:
     print (f"Hitung mundur, angka = {d}")
     d = d - 1

print ("\n --- Batas --- \n")  




print ("\n For Nested \n")

for a in range (6):
     for b in range (6):
          print (f"Luar : {a}, Dalam : {b}")
          
          
print ("\n --- Batas --- \n")




print ("\n Teknik Iterasi For (Oshi saya) \n")

oshi = [
    "1. Michie JKT48 (UTAMA)",
    "2. Gracie JKT48 (UTAMA)",
    "3. Fritzy JKT48 (UTAMA)",
    "4. Lily JKT48 (UTAMA)",
    "5. Anindya JKT48 (UTAMA)",
    "6. Christy JKT48 (UTAMA)",
    "7. Freya JKT48 (UTAMA)",
    "8. Olla JKT48",
    "9. Jessi JKT48",
    "10. Fiony JKT48",
    "11. Muthe JKT48",
    "12. Marsha JKT48",
    "13. Eli JKT48",
    "14. Mikaela JKT48",
    "15. Ekin JKT48",
]

for a in oshi:
     print (a)


print ("\n --- Batas --- \n")




print ("\n Teknik Iterasi Kontrol Continue \n")

for f in range (1, 15):
     if f == 5:
          continue
     print (f"Urutan ke - {f}")
     
     
print ("\n --- Batas --- \n")




print ("\n Teknik Iterasi Kontrol Break\n")

for o in range (1, 25):
     if o == 15:
          break
     print (f"Urutan ke - {o}")
     
     
print ("\n --- Batas --- \n")




print ("\n List Iterasi Kontrol Continue \n")

buah = [
     "Apel", 
     "Naga", 
     "Melon", 
     "Semangka", 
     "Nangka",
     "Jeruk",
     "Strawberi",
     "Salak",
     
     ]

for a in buah:
     if a == "Melon":
          continue
     print (a)
     
     
print ("\n --- Batas --- \n")




print ("\n List Iterasi Kontrol Break \n")

buah = [
     "Apel", 
     "Naga", 
     "Melon", 
     "Semangka", 
     "Nangka",
     "Jeruk",
     "Strawberi",
     "Salak",
     
     ]

for k in buah:
     if k == "Melon":
          break
     print (k)
     
     
print ("\n --- Batas --- \n")




print ("\n Fungsi Dasar \n")

def tan ():
     print ("Hello World")
     
tan ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan parameter \n")

def yun (nama):
     print (f"Halo nama saya {nama}, dari Jakarta Utara")
     
yun ("Fakhri")
yun ("Hayyan")
yun ("Rayyan")
yun ("Dimas")
yun ("Mido")


print ("\n --- Batas --- \n")



print ("\n Fungsi dengan parameter 1 \n")

def tur (nama, asal, suku, budaya):
     print (f"Halo nama saya {nama}, asal dari {asal}, suku saya adalah {suku}, dan budaya saya adalah {budaya}")
     
tur ("Frederick", "Jerman", "Jermanik Barat", "Jerman")
tur ("Louis", "Prancis", "Prancis", "Prancis")
tur ("Graciantsya", "Palembang", "Tionghoa", "Tionghoa")
tur ("Eri Erria", "Singkawang", "Tionghoa", "Tionghoa")


print ("\n --- Batas --- \n")



print ("\n Fungsi dengan Parameter \n")

def run (nama):
     print (f"Halo saya {nama} dari Jakarta")
     
run ("Rummer")
run ("Santer")
run ("Rus")
run ("Far")


print ("\n --- Batas --- \n")



print ("\n Fungsi dengan Return \n")

def tambah (a, b):
     return a + b

hasil = tambah (10, 10)
print (hasil)


print ("\n --- Batas --- \n")