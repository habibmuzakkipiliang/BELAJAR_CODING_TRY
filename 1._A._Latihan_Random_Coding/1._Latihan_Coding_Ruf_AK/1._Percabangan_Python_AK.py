print ("\n Bikin Hello World dan Variabel \n")

print ("Hello World")


gan = "Contoh Aja"
print (gan)


fan = "Ayo ke Fx Sudirman"
print (fan)


print ("\n --- Batas --- \n")




print ("\n Tipe Data Pemrograman \n")

teks = "Contoh teks"
angka = 13
desimal = 23.12
cek = True
char = 'A'
kosong = None

detail = f"""
- Teks    : {teks}
- Angka   : {angka}
- Desimal : {desimal}
- Cek     : {cek}
- Char    : {char}
- Kosong  : {kosong}
"""

print (detail)


print ("\n --- Batas --- \n")




print ("\n Array \n")

bensin = [
    
    "1. Pertamax",
    "2. Pertamax Turbo",
    "3. Pertamax Dex",
    "4. Dexlite",
    "5. Pertalite",
    "6. Bio Solar",
    
    ]
    
    
for a in bensin:
    print (a)
    
    
print ("\n --- Batas --- \n")




print ("\n Dictionary \n")

gok = {
    "nama" : "James",
    "usia" : 18, 
    "asal" : "Amrik",
    "cek" : True,
}

print ("Nama :", gok ["nama"])
print ("Usia :", gok ["usia"])
print ("Asal :", gok ["asal"])
print ("Cek :", gok ["cek"])


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Operator dasar \n")

def tambah (x, y):
    return x + y
    
    
def kurang (a, b):
    return a - b
    
    
def kali (e, r):
    return e * r
    

def bagi (l, p):
    return l / p
    
    
def modulus (w, k):
    return w % k
    
    
def pangkat (v, h):
    return v ** h
    
    
hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 10)
hasil_4 = bagi (20, 5)
hasil_5 = modulus (20, 5)
hasil_6 = pangkat (10, 4)


print ("Tambah =", hasil_1)
print ("Kurang =", hasil_2)
print ("Kali =", hasil_3)
print ("Bagi =", hasil_4)
print ("Modulus =", hasil_5)
print ("Pangkat =", hasil_6)


print ("\n --- Batas --- \n")




print ("\n Operator Perbandingan \n")

x = 10
y = 5

banding = f"""
- Hasil = {x > y}
- Hasil = {x < y}
- Hasil = {x >= y}
- Hasil = {x <= y}
- Hasil = {x != y}
- Hasil = {x == y}
"""

print (banding)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Switch Case 1 \n")

def rar (a):
    
    match (a):
        
        case 1:
            print ("Oke")
            
        case 2:
            print ("Belum")
            
        case 3:
            print ("Baru Mulai")
            
        case _:
            print ("Biasa aja")
            
rar (2)
rar (1)
rar (3)
rar (4)


print ("\n --- Batas --- \n")



print ("\n Fungsi dengan Switch Case 2, Lampu Rambu Lalu Lintas \n")

def lampu (b):
    
    match (b):
        
        case "Merah":
            print ("Lampu Merah")
            
        case "Kuning":
            print ("Lampu Kuning")
            
        case "Hijau":
            print ("Lampu Hijau")
            
        case _:
            print ("Lampu warna lain")
            
lampu ("Merah")
lampu ("Kuning")
lampu ("Hijau")
lampu ("Biru")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Dasar \n")

def dasar (a):
    
    if a >= 5:
        print (f"Besar, angka a = {a}")
        
    else:
        print (f"Kecil, angka a = {a}")
        
dasar (10)
dasar (4)
dasar (8)
dasar (3)
dasar (7)
dasar (2)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan dasar 1 \n")

def rer (b):
    
    if b >= 5:
        print (f"Besar, angka b = {b}")
        
    else:
        print (f"Kecil, angka b = {b}")
        

rer (10)
rer (4)
rer (8)
rer (3)
rer (7)
rer (2)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan \n")

def fer (c):
    
    if c >= 8:
        print (f"Besar, angka c = {c}")
        
    elif c >= 5:
        print (f"Sedang, angka c = {c}")
        
    else:
        print (f"Kecil, angka c = {c}")
        
fer (10)
fer (8)
fer (7)
fer (5)
fer (4)
fer (3)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan 1 \n")

def des (d):
    
    if d >= 8:
        print (f"Besar, angka d = {d}")
        
    elif d >= 5:
        print (f"Sedang, angka d = {d}")
        
        
    else:
        print (f"Kecil, angka d = {d}")
        
des (10)
des (8)
des (7)
des (5)
des (4)
des (3)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Tangga, Nilai Rapor \n")

def rapor (h):
    
    if h >= 95:
        print (f"A, nilai = {h}")
        
    elif h >= 90:
        print (f"B, nilai = {h}")
        
    elif h >= 80:
        print (f"C, nilai = {h}")
        
    elif h >= 70:
        print (f"D, nilai = {h}")
        
    elif h >= 60:
        print (f"E, nilai = {h}")
        
    elif h >= 50:
        print (f"F, nilai = {h}")
        
    else:
        print (f"Kecil banget, nilai = {h}")
        
rapor (100)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (30)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Nested \n")

def det (x):
    
    if x >= 8:
        if cek == True:
            print (f"Besar, angka x = {x}")
            
        elif x >= 5:
            print (f"Sedang, angka x = {x}")
            
    else:
        print (f"Kecil, angka x = {x}")
        
det (10)
det (9)
det (8)
det (7)
det (5)
det (3)
det (2)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Nested 1 \n")

def fer (y):
    
    if y >= 8:
        if cek == True:
            print (f"Besar, angka y = {y}")
            
        else:
            print (f"Sedang, angka y = {y}")
            
    else:
        print (f"Kecil, angka y = {y}")
        
fer (10)
fer (9)
fer (8)
fer (7)
fer (5)
fer (3)
fer (4)

print ("\n --- Batas --- \n")