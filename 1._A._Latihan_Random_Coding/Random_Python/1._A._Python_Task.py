# Python Task

print ("Hello World")


print ("\n --- Batas --- \n")



print ("\n Variabel dan Tipe data pemrograman \n")


nama = "Tes 1"
angka = 34
desimal = 44.23
huruf = 'A'
cek = True
daftar = [
    
    "1. Mobil",
    "2. Motor", 
    "3. Kereta Api",
    "4. Bajai",
    
    ]


detail = f"""

- Nama    : {nama}
- Angka   : {angka}
- Desimal : {desimal}
- Huruf   : {huruf}
- Cek     : {cek}
- Daftar  : 

"""

print (detail)


for a in daftar:
    print (a)


print ("\n --- Batas --- \n")




print ("\n Dictionary \n")


data = {
    "nama" : "Alan John",
    "asal" : "Amerika Serikat",
    "kerja" : "Software Engineer",
    "coding" : "HTML, CSS, JavaScript dan Python",
    
}


print ("Nama :", data ["nama"])

print ("Asal :", data ["asal"])

print ("Kerja :", data ["kerja"])

print ("Coding :", data ["coding"])


print ("\n --- Batas --- \n")




print ("\n Percabangan Dasar \n")


a = 9

if a > 5:
    print (f"Besar, a = {a}")
    
else:
    print (f"Kecil, a = {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan dasar 1 \n")


b = 3

if b > 5:
    print (f"Besar, b = {b}")
    
else:
    print (f"Kecil, b = {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan 1\n")


c = 9

if c > 5:
    print (f"Besar, c = {c}")
    
elif c < 5:
    print (f"Kecil, c = {c}")
    
else:
    print (f"Sama saja, c = {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan 2\n")


d = 3

if d > 5:
    print (f"Besar, d = {d}")
    
elif d < 5:
    print (f"Kecil, d = {d}")
    
else:
    print (f"Sama saja, d = {d}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 1 \n")

skor = 9
cek = True

if cek:
    if skor > 5:
        print (f"Besar, skor = {skor}")
        
    elif skor < 5:
        print (f"Kecil, skor = {skor}")
        
else:
    print (f"Sama saja, skor = {skor}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 \n")

skor = 3
cek = True

if cek:
    if skor > 5:
        print (f"Besar, skor = {skor}")
        
    else:
        print (f"Kecil, skor = {skor}")
        
else:
    print (f"Sama saja, skor = {skor}")


print ("\n --- Batas --- \n")




print ("\n Percabangan nested, usia produtif manusia \n")


usia = 19
cek = True

if cek:
    if usia >= 15 and usia <= 64:
        print (f"Sudah masuk usia produktif, usia = {usia}")
        
    elif usia > 64:
        print (f"Sudah lanjut usia, usia = {usia}")
        
    else:
        print (f"Masih dibawah usia produktif, usia = {usia}")
        
else:
    print (f"Usianya masih kecil, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar \n")


for a in range (11):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar 1 \n")

for b in range (21):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")
