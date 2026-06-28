# Latihan Project Sederhana Python

print ("\n Latihan Project Sederhana Python \n")


tes = "Ayo Latihan Python untuk memulai Project nya  \n"
print (tes)




nama = input ("Nama kamu siapa ? ")
asal = input ("Dari mana asal kamu ? ")
tinggal = input ("Tempat tinggal kamu dimana ? ")
usia = int (input ("Usia kamu berapa ? "))
hobi = input ("Hobi kamu apa ? ")
darah = input ("Golongan darah ? ")
suku = input ("Suku kamu ? ")
agama = input ("Agama kamu ? ")
fans = input ("Fans kamu ? ")


print ("\n --- Batas --- \n")




if usia >= 25 :
    print ("Usia lebih dari kamu 25 tahun")
    
elif usia >= 24:
    print ("Usia kamu 24 tahun")
    
elif usia >= 23:
    print ("Usia kamu 23 tahun")
    
elif usia >= 22:
    print ("Usia kamu 22 tahun")
    
elif usia >= 21:
    print ("Usia kamu 21 tahun")
    
elif usia >= 20:
    print ("Usia kamu 20 tahun")

elif usia >= 19: 
    print ("Usia kamu 19 tahun")
    
elif usia >= 18:
    print ("Usia kamu 18 tahun")
    
elif usia >= 17:
    print ("Usia kamu 17 tahun")
    
elif usia >= 16:
    print ("Usia kamu 16 tahun")
    
else:
    print ("Usia kamu dibawah 16 tahun")
    
    
print ("\n --- Batas --- \n")




profil = f"""

--- Profil ---

- Nama    : {nama}
- Asal    : {asal}
- Alamat  : {tinggal}
- Usia    : {usia}
- Hobi    : {hobi}
- Darah   : {darah}
- Suku    : {suku}
- Agama   : {agama}
- Fans    : {fans}


"""


print (profil)


print ("\n --- Batas --- \n")




print ("\n Oshi Saya \n")

oshi = [
    
    "1. Michie JKT48",
    "2. Gracie JKT48",
    "3. Lily JKT48",
    "4. Fritzy JKT48",
    "5. Anindya JKT48",
    "6. Christy JKT48",
    "7. Freya JKT48",
    
    ]
    
    
for a in oshi:
    print (a)
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Dasar Login \n")

login = "mark"
password = "kino"


if "mark" and "kino":
    print ("Benar")
    
else:
    print ("Salah")
    

print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan Dasar \n")


def wen (an):
    
    if an >= 5:
        print (f"Besar, angka = {an}")
        
    else:
        print (f"Kecil, angka = {an}")
        
wen (10)
wen (3)
wen (9)
wen (3)


print ("\n --- Batas --- \n")





print ("\n Fungsi Percabangan Dasar 1 \n")


def ran (b):
    
    if b >= 5:
        print (f"Besar, angka = {b}")
        
    else:
        print (f"Kecil, angka = {b}")
        
ran (10)
ran (3)
ran (8)
ran (4)


print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan Lanjutan 1 \n")

def er (c):
    
    if c >= 10:
        print (f"Besar, angka = {c}")
        
    elif c == 5:
        print (f"Setengah, angka = {c}")
        
    else:
        print (f"Kurang, angka = {c}")
        
er (10)
er (3)
er (1)
er (10)
er (6)


print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan Nested 1 \n")

def fur (d):

    cek = True
    
    if d >= 10:
        if cek == True:
            print (f"Besar, angka = {d}")
            
        elif d <= 5:
            print (f"Kecil, angka = {d}")
            
    else:
        print (f"Sama saja, angka = {d}")
        
fur (10)
fur (3)
fur (2)
fur (8)
fur (9)


print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan Nested 2 \n")

def hun (e):
    
    cek = True
    
    if e >= 10:
        if cek == True:
            print (f"Besar, angka = {e}")
            
        else:
            print (f"Kecil, angka = {e}")
            
    else:
        print (f"Sama saja, angka = {e}")
        
hun (10)
hun (3)
hun (9)
hun (3)
hun (7)


print ("\n --- Batas --- \n")





print ("\n Fungsi Percabangan Nested Majemuk Kompleks \n")

def op (usia, uang):
    
    cek = True
    
    if usia >= 15 and uang >= 5000:
        if cek == True:
            print (f"Berarti kamu udah cukup, usia = {usia}, uang = {uang}")
            
        elif usia <= 16 and uang <= 5000:
            print (f"Kamu belum cukup, usia = {usia}, uang = {uang}")
            
        else:
            print (f"Kamu masih ada waktu, usia = {usia}, uang = {uang}")
            
    else:
        print (f"Kamu belum ada sama sekali, usia = {usia}, uang = {uang}")
    
op (10, 3000)
op (19, 6000)
op (12, 10000)