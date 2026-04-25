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






