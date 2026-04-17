# Latihan Fungsi dengan contoh kasus beragam seperti JKT48, agar gak mudah bosan sama sekali  


def main ():
    
    print ("\n Latihan Fungsi dengan contoh kasus beragam seperti JKT48, agar mudah bosan sama sekali \n")
    
    
    print ("\n 20 Top Member JKT48 paling populer di Indonesia tahun 2026 \n")
    
    
    jkt48 = [
        
       "1. Feni Fitriyanti",
       "2. Fiony Alveria",
       "3. Freya Jayawardhana", 
       "4. Angelina Christy (Christy)", 
       "5. Jessica Chandra (Jessi)",
       "6. Marsha Lenathea",
       "7. Gita Sekar Andarini",
       "8. Mutiara Azzahra (Muthe)",
       "9. Kathrina Irene (Atin)",
       "10. Lulu Salsabila",
       "11. Greesella Adhalia (Greesel)",
       "12. Indah Cahya",
       "13. Cornelia Vanisa (Oniel)",
       "14. Aurellia (Lia)",
       "15. Fritzy Rosmerian",
       "16. Michelle Alexandra (Michie)",
       "17. Helisma Putri (Eli)",
       "18. Cathleen Hana Nixie (Cathy)",
       "19. Febriolla Sinambela (Olla)",
       "20. Gracie Octaviani (Gracie)",
        
    ]
    
    
    for a in jkt48:
        print (a)
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Tipe data dasar 
    
    print ("\n Tipe data dasar \n")
    
    
    teks = "Halo Teks"
    angka = 23
    desimal = 34.24
    cek_1 = True
    cek_2 = False
    fer = [1, 2, 3, 4, 5, 6, 7, 8]
    cer = (1, 2, 3, 4, 5, 6, 7, 8)
    der = {1, 2, 3, 4, 5, 6, 7, 8}
    
    
    print ("Teks =", teks)
    print ("Angka =", angka)
    print ("Desimal =", desimal)
    print ("Cek 1 =", cek_1)
    print ("Cek 2 =", cek_2)
    print ("List =", fer)
    print ("Tuple =", cer)
    print ("Set =", der)
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Manipulasi String
    
    print ("\n Manipulasi String \n")
    
    
    tulis = "JKT48"
    
    print (f"Halo anak {tulis}")
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    tes = "Freya JKT48"
    
    print (f"Halo kapten {tes}")
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    center = "Fiony JKT48"
    
    print (f"Halo center {center}")
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    manajer = "Melody Laksani"
    
    print (f"Halo manajer umum {manajer}")
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    wakil = "Shani Indira Natio"
    
    print (f"Halo wakil umum manajer {wakil}")
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # For dasar
    
    print ("\n For dasar \n")
    
    
    for a in range (10):
        print ("a", a)
        
        
    print ("\n --- Batas --- \n")
    
    
    
    
    # While dasar
    
    print ("\n While dasar \n")
    
    
    a = 5
    
    while a < 10:
        print ("a", a)
        a = a + 1
        
        
    print ("\n --- Batas --- \n")
    
    
    
    
    # For Nested 
    
    print ("\n For Nested \n")
    
    
    for a in range (3):
        for b in range (4):
            print ("a", a, "b", b)
           
    
    print ("\n --- Batas --- \n")
    
    
    
    
    # Percabangan dasar
    
    print ("\n Percabangan dasar \n")
    
    a = 3
    
    if a > 5:
        print ("Bagus")
        
    else:
        print ("Kecil")
        
        
    print ("\n --- Batas --- \n")
    
    
    
    
    # Percabangan Nested 1
    
    print ("\n Percabangan Nested 1 \n")
    
    
    member = 9
    cek = True
    
    if member > 7:
        if (cek):
            print ("Iya, lulus dan jadi anggota tetap JKT48")
            
    elif member < 5:
            print ("Iya, turun jadi Trainee JKT48")
            
    else:
        print ("Gak lulus sama sekali")
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Switch Case 
    
    
    print ("\n Switch Case \n")
    
    
    kondisi = 2
    
    match (kondisi):
        
        case 1:
            print ("Laper banget")
            
        case 2:
            print ("Laper dikit")
            
        case 3:
            print ("Laper biasa")
            
        case 4:
            print ("Kenyang biasa")
            
        case 5:
            print ("Kenyang dikit")
            
        case 6:
            print ("Kenyang banget")
            
        case _:
            print ("Biasa aja deh")
            
            
    print  ("\n --- Batas --- \n")
    
    
main ()




def profil ():
    
    # Profil JKT48 
    
    
    print ("\n Profil JKT48 \n")
    
    
    data = {
        
        "nama_grup" : "JKT48",
        "asal_negara" : "Indonesia",
        "pendiri" : "Yasushi Akimoto",
        "berdiri_tahun" : "2011",
        "berdiri_bulan" : "17 Desember",
        "era_sekarang" : "JKT48 FIGHT",
        "kapten_jkt48" : "Freya JKT48 (gen 7)",
        "manajer_jkt48" : "Melody Laksani (Eks Kapten JKT48 gen 1)",
        "wakil_manajer_jkt48" : "Shani Indira Natio (Eks Kapten JKT48 gen 3)",
    }
    
    
    print ("Nama grup :", data ["nama_grup"])
    
    print ("Asal negara :", data ["asal_negara"])
    
    print ("Pendiri :", data ["pendiri"])
    
    print ("Berdiri tahun :", data ["berdiri_tahun"])
    
    print ("Berdiri bulan :", data ["berdiri_bulan"])
    
    print ("Era sekarang :", data ["era_sekarang"])
    
    print ("Kapten JKT48 :", data ["kapten_jkt48"])
    
    print ("Manajer JKT48 :", data ["manajer_jkt48"])
    
    print ("Wakil manager JKT48 :", data ["wakil_manajer_jkt48"])
    
    
    print  ("\n --- Batas --- \n")
    
    
    
profil ()




# Fungsi dasar

def dasar ():
    print ("Hello Dapeng")
    
dasar ()


print  ("\n --- Batas --- \n")




# Fungsi dasar 2

print ("\n Fungsi dasar 2 \n")


def zet ():
    print ("Hello Dun")
    
zet ()
zet ()
zet ()
zet ()


print  ("\n --- Batas --- \n")




# Fungsi dasar 3

print ("\n Fungsi dasar \n")


def arif ():
    print ("Hello Arif")
    print ("Hello Hayyan")
    print ("Hello Jansen")
    print ("Hello Yusuf")
    
arif ()


print  ("\n --- Batas --- \n")




# Fungsi dengan parameter 


print ("\n Fungsi dengan parameter \n")


def unter (nama):
    print ("Hello " + nama)
    
 
unter ("JKT48 Mantap Jiwa Guys")    
unter ("JKT48 Early")
unter ("JKT48 Golden Era")
unter ("JKT48 New Era")
unter ("JKT48 Fight")


print  ("\n --- Batas --- \n")




print ("\n Fungsi dengan parameter 1 \n")


def fos (nama):
    print ("Hello " + nama)
    
fos ("AKB48")
fos ("JKT48")
fos ("KLP48")
fos ("MNL48")
fos ("Quadlips")
fos ("BNK48")
fos ("TSH48")
fos ("TPE48")
fos ("CGM48")
fos ("Raintree Non Grup 48")


print ("\n --- Batas --- \n")



print ("\n Fungsi dengan parameter 2 \n")


def det (nama):
    print ("Hello " + nama)
    print ("Hello " + nama)
    print ("Hello " + nama)
    print ("Hello " + nama)
    print ("Hello " + nama)
    
det ("Python")
det ("JavaScript")
det ("Java")
det ("C#")
det ("C++ / C")
det ("Dart (Flutter)")
det ("PHP")


print  ("\n --- Batas --- \n")



# Fungsi dengan return

print ("\n Fungsi dengan return \n")


def tambah (a, b):
    return a + b
    
hasil = tambah (10, 10)
print ("Tambah =", hasil)


print  ("\n --- Batas --- \n")




def kurang (e, r):
    return e - r
    
hasil = kurang (20, 10)
print ("Kurang =", hasil)


print  ("\n --- Batas --- \n")




def kali (e, d):
    return e * d
    
hasil = kali (10, 10)
print ("Kali =", hasil)


print  ("\n --- Batas --- \n")




def pangkat (f, k):
    return f ** k
    
hasil = pangkat (10, 3)
print ("Pangkat =", hasil)


print  ("\n --- Batas --- \n")




def bagi (g, h):
    return g / h
    
hasil = bagi (10, 5)
print ("Bagi =", hasil)


print  ("\n --- Batas --- \n")




def modulus (x, y):
    return x % y
    
hasil = modulus (10, 3)
print ("Modulus =", hasil)