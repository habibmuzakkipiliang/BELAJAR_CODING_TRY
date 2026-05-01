print ("Hello World")

print ("\n --- Batas --- \n")



print ("\n Variabel dasar \n")

nama = "Hai Indonesia"
print (nama)


print ("\n --- Batas --- \n")




print ("\n Tipe data pemrograman \n")

teks = "Tes tulisan"
angka = 12
desimal = 42.2
cek = True
huruf = 'A'
daftar = [
    "1. Toyota",
    "2. Daihatsu",
    "3. Mitsubishi",
    "4. Ford",
    "5. Mercedes Benz",
]   
    
detail = f"""

- Teks    :{teks}
- Angka   :{angka}
- Desimal :{desimal}
- Char    :{huruf}
- Cek     :{cek}
- Daftar  :

"""

print (detail)


for a in daftar:
    print (a)
    

print ("\n --- Batas --- \n")



print ("\n Tuple \n")


far = (
    
    "1. Toyota",
    "2. Daihatsu",
    "3. Mitsubishi",
    "4. Ford",
    "5. Mercedes Benz",
    
    )
    
    
for w in far:
    print (w)
    
    
print ("\n --- Batas --- \n") 
    
    
    
print ("\n Set \n")


der = {
    "1. Toyota",
    "2. Daihatsu",
    "3. Mitsubishi",
    "4. Ford",
    "5. Mercedes Benz",
}


for t in der:
    print (t)
    
    
print ("\n --- Batas --- \n")




print ("\n Dictionary \n")

data = {
    "nama" : "John Doe",
    "asal" : "Amerika",
    "umur" : 30,
    "pekerjaan" : "Programmer",
   }

print ("Nama :", data ["nama"])

print ("Asal :", data ["asal"])

print ("Umur :", data ["umur"])

print ("Pekerjaan :", data ["pekerjaan"])   


print ("\n --- Batas --- \n")




print ("\n Operator dasar \n")

x = 10
y = 5

print ("Tambah =", x + y)
print ("Kurang =", x - y)
print ("Kali =", x * y)
print ("Bagi =", x / y)
print ("Modulus =", x % y)
print ("Pangkat =", x ** y)

print ("\n --- Batas --- \n")




print ("\n Operator Perbandingan \n")

print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)
print ("Hasil =", x >= y)
print ("Hasil =", x <= y)


print ("\n --- Batas --- \n")




print ("\n Operator Logika \n")


print ("Hasil =", x > y and x < y)
print ("Hasil =", x > y or x < y)
print ("Hasil =", not x)
print ("Hasil =", not y)


print ("\n --- Batas --- \n")




print ("\n Switch Case \n")


a = 9

match (a):
    
    case 1:
        print ("1")
        
    case 2:
        print ("2")
        
    case 3:
        print ("3")
        
    case 4:
        print ("4")
        
    case 5:
        print ("5")
        
    case 6:
        print ("6")
        
    case 7:
        print ("7")
        
    case 8:
        print ("8")
        
    case 9:
        print ("9")
        
    case 10:
        print ("10")
        
    case _:
        print ("Semula")
        
        
print ("\n --- Batas --- \n")




print ("\n Percabangan dasar \n")


a = 10

if a > 5:
    print (f"Besar, a = {a}")
    
else:
    print (f"Kecil, a = {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan \n")


b = 3

if b > 5:
    print (f"Besar, b = {b}")
    
elif b < 5:
    print (f"Kecil, b = {b}")
    
else:
    print (f"Sama saja, b = {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan 1 \n")


d = 9

if d > 5:
    print (f"Besar, d = {d}")
    
elif d < 5:
    print (f"Kecil, d = {d}"
    
else:
    print (f"Sama saja, d = {d}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 1 \n")


g = 9
cek = True

if cek:
    if g > 5:
        print (f"Besar, g = {g}")
        
    elif g < 5:
        print (f"Kecil, g = {g}")
        
else:
    print (f"Sama saja, g = {g}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 \n")


j = 9
cek = True

if cek:
    if j > 5:
        print (f"Besar, j = {j}")
        
    else:
        print (f"Kecil, j = {j}")
        
else:
    print (f"Sama saja, j = {j}")
    
    
print ("\n --- Batas --- \n")
