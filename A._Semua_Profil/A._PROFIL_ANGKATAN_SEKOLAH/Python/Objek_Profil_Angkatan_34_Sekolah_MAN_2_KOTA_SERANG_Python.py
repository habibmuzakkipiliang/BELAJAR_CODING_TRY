# Objek Profil Angkatan ke 34 MAN 2 KOTA SERANG yaitu ASCENDRIA dalam Coding Python


print ("\n Objek Profil Angkatan ke 34 MAN 2 KOTA SERANG yaitu ASCENDRIA dalam Coding Python \n")


data = {
    "asal" : "MAN 2 KOTA SERANG",
    "tahun" : "2023 - 2026",
    "angkatan" : "ke - 34",
    "nama" : "ASCENDRIA",
    "ketua" : "Fitra Hidayat Arasy (dari kelas 12 IPA 1)",
    "wakil" : "Mokhamad Asyraf Ramadhan (Acop) (dari kelas 12 IPA 1)",
    "jumlah" : "300 orang",
    "kelas" : [
        
        "1. 12 IPA 1", 
        "2. 12 IPA 2", 
        "3. 12 IPA 3", 
        "4. 12 IPA 4", 
        "5. 12 IPA 5",
        "6. 12 IPS 1", 
        "7. 12 IPS 2", 
        "8. 12 IPS 3", 
        "9. 12 BAHASA",
        "10. 12 AGAMA,
        
    ],
}



print ("Asal sekolah :", data ["asal"], "\n"
)


print ("Tahun :", data ["tahun"], "\n")


print ("Angkatan :", data ["angkatan"], "\n")


print ("Nama angkatan :", data ["nama"], "\n")


print ("Ketua angkatan :", data ["ketua"], "\n")


print ("Wakil ketua angkatan :", data ["wakil"], "\n")


print ("Jumlah siswa :", data ["jumlah"], "\n"
)


print ("Kelas :")


for i in data ["kelas"]:
    print (i)
 
    
print ("\n")
