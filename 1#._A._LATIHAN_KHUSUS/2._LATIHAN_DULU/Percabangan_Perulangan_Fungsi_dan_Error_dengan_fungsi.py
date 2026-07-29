# Switch Case 1

def eru (l):

     match (l):

          case 1:
               print ("Angka 1")

          case 2:
               print ("Angka 2")

          case 3:
               print ("Angka 3")

          case 4:
               print ("Angka 4")

          case _:
               print ("Angka lain")

eru (1)
eru (2)
eru (3)
eru (4)
eru (5)


print ("\n --- batas --- \n")



# Switch Case 2

def hun (e):

     match (e):

          case "Merah":
               print ("Warna Merah")

          case "Kuning":
               print ("Warna Kuning")

          case "Hijau":
               print ("Warna Hijau")

          case _:
               print ("Warna lain")

hun ("Merah")
hun ("Kuning")
hun ("Hijau")


print ("\n --- batas --- \n")





# Fungsi dengan Percabangan Dasar 

def run (a):

     if a >= 5:
          print (f"Besar, angka a = {a}")

     else:
          print (f"Kecil, angka a = {a}")

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




# Fungsi dengan percabangan lanjutan 2 

def tur (b):

     if b >= 8:
          print (f"Besar, angka b = {b}")

     elif b >= 5:
          print (f"Tengah, angka b = {b}")

     else:
          print (f"Kecil, angka b = {b}")

tur (10)
tur (9)
tur (8)
tur (7)
tur (6)
tur (5)
tur (4)
tur (3)
tur (2)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan nilai rapor

def rapor (f):

     if f >= 95:
          print (f"A, nilai = {f}")

     elif f >= 90:
          print (f"B, nilai = {f}")

     elif f >= 80:
          print (f"C, nilai = {f}")

     elif f >= 70:
          print (f"D, nilai = {f}")

     elif f >= 60:
          print (f"E, nilai = {f}")

     elif f >= 50:
          print (f"Jelek amat, nilai = {f}")

rapor (100)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (40)
rapor (30)
rapor (20)
rapor (10)
rapor (5)


print ("\n --- batas --- \n")



# Fungsi dengan Percabangan nested 1 

def wer (c):

     cek = True

     if c >= 5:
          if cek:
               print (f"Besar, angka c = {c}")

          else:
               print (f"Tengah, angka c = {c}")

     else:
          print (f"Kecil, angka c = {c}")

wer (10)
wer (9)
wer (8)
wer (7)
wer (6)
wer (5)
wer (4)
wer (3)
wer (2)
wer (1)


print ("\n --- batas --- \n")




# Fungsi dengan Percabangan Nested 2 

def kop (f):

     cek = True

     if f >= 8:
          if cek:
               print (f"Besar, angka f = {f}")

          elif f >= 5:
               print (f"Tengah, angka f = {f}")

     else:
          print (f"Kecil, angka f = {f}")

kop (10)
kop (9)
kop (8)
kop (7)
kop (6)
kop (5)
kop (4)
kop (3)
kop (2)
kop (1)


print ("\n --- batas --- \n")




# Usia produktif manusia 

def usia (m):

     if m >= 15 and m <= 40:
          print (f"Usia yang produktif, usia = {m}")

     elif m > 40:
          print (f"Usia sudah cukup, usia = {m}")

     else:
          print (f"Masih kecil usiannya, usia = {m}")

usia (10)
usia (40)
usia (30)
usia (20)
usia (70)
usia (75)
usia (4)


print ("\n --- batas --- \n")



# Usia masuk JKT48 

def oshi (j):

     if j >= 13 and j <= 19:
          print (f"Usia yang sudah boleh masuk jkt48, usia = {j}")

     elif j >= 19:
          print (f"Sudah lebih dari cukup, usia = {j}")

     else:
          print (f"Masih kecil usiannya, usia = {j}")

oshi (20)
oshi (19)
oshi (18)
oshi (17)
oshi (16)
oshi (15)
oshi (14)
oshi (13)
oshi (12)


print ("\n --- batas --- \n")




# Usia masuk kerja

def ban (k):

     if k >= 15 and k <= 40:
          print (f"usia yang boleh kerja, usia = {k}")

     elif k > 40:
          print (f"Sudah pensiun, usia = {k}")

     else:
          print (f"Masih kecil usiannya, usia = {k}")

ban (70)
ban (60)
ban (50)
ban (40)
ban (30)
ban (20)
ban (10)
ban (5)


print ("\n --- batas --- \n")



# For dasar 

for a in range (1, 11):
     print (f"Urutan ke - {a}")


print ("\n --- batas --- \n")



# For dasar 

for i in range (11):
     print (f"Urutan ke - {i}")


print ("\n --- batas --- \n")




# Struktur data

dat = ["Halo Dunia", "Halo Fire", "Halo World", "Fireball"]

for i in dat:
     print (i)


print ("\n --- batas --- \n")