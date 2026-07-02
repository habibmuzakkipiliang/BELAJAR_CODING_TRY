# Latihan Struktur Data dan Modular (Fungsi) dan Percabangan dan Iterasi

print ("\n Latihan Struktur Data dan Modular (Fungsi) dan Percabangan dan Iterasi \n")


print ("\n List atau Array \n")

daftar = [
     "Front Barat WW1",
     "Front Timur WW1", 
     "Front Barat WW2",
     "Front Timur WW2",
     
]

daftar.append ("Perang Dunia 2")
daftar.append ("Perang Dunia 1")
daftar.append ("Perang Dingin") 
daftar.append ("Perang Modern")
daftar.append ("Perang Napoleon")
daftar.append ("Perang 30 Tahun")
daftar.append ("Amerika Serikat WW2")
daftar.append ("Tiongkok WW2")
daftar.append ("Inggris WW2")
daftar.append ("Uni Soviet WW2")
daftar.append ("Jepang WW2")
daftar.append ("Jerman WW2")
daftar.append ("Italia WW2")  
daftar 
print (daftar)


print ("\n --- Batas --- \n")


daftar.remove ("Perang Napoleon")
daftar.remove ("Perang 30 Tahun")
print (daftar) 


print ("\n --- Batas --- \n")


daftar.sort ()
print (daftar)


print ("\n --- Batas --- \n")

for a in daftar:
     print (a)
     
 
print ("\n --- Batas --- \n")



print ("\n Dictionary \n")

profil = {
     "nama" : "Gracie JK48, Ecarg, Geci",
     "nama_lengkap" : "Grace Octaviani Tanujaya",
     "tinggi_badan" : 166,
     "asal" : "Tangerang",
     "lahir" : "18 Oktober 2007",
     "team" : "Love",
     "jikoshoukai" : "Manis seperti gulali, imut seperti kelinci! Xi xi xi, Gracie!",
     
}

print ("Nama :", profil ["nama"])
print ("Nama lengkap :", profil ["nama_lengkap"])
print ("Tinggi badan :", profil ["tinggi_badan"])
print ("Asal :", profil ["asal"])
print ("Lahir :", profil ["lahir"])
print ("Team :", profil ["team"])
print ("Jikoshoukai :", profil ["jikoshoukai"])


print ("\n --- Batas --- \n")




print ("\n Dictionary \n")

data = {
     "nama" : "Jason",
     "asal" : "Amrik",
     "kerja" : "Programming",
     "usia" : 20,
}

print ("Nama :", data ["nama"])
print ("Asal :", data ["asal"])
print ("Kerja :", data ["kerja"])
print ("Usia :", data ["usia"])


print ("\n --- Batas --- \n")
    
    


print ("\n Fungsi Percabangan Dasar \n")

def dash (a):
     
     if a > 5:
          print (f"Besar, angka a = {a}")
          
     else:
          print (f"Kecil, angka a = {a}")
          
dash (10)
dash (3)
dash (8)
dash (2)


print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan Dasar 2 \n")

def fun (b):
     
     if b > 5:
          print (f"Besar, angka b = {b}")
          
     else:
          print (f"Kecil, angka b = {b}")
          
fun (10)
fun (3)
fun (7)
fun (4)


print ("\n --- Batas --- \n")
