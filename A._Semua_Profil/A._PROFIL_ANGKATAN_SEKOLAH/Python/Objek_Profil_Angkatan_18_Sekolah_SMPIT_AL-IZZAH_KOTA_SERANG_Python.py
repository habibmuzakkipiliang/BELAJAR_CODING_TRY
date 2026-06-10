# Objek Profil Angkatan ke 18 SMPIT AL-IZZAH KOTA SERANG yaitu HISTARA dalam Coding Python


print ("\n Objek Profil Angkatan ke 18 SMPIT AL-IZZAH KOTA SERANG yaitu HISTARA dalam Coding Python \n")


data = {
    "asal" : "SMPIT AL-IZZAH KOTA SERANG",
    "tahun" : "2020 - 2023",
    "angkatan" : "ke - 18",
    "nama" : "HISTARA",
    "ketua" : "Aisyah Nalira Hadi (dari Kelas 9 Akhwat 2)",
    "wakil" : "Fakhri El Wafi (dari Kelas 9 Ikhwan 2)",
    "jumlah" : "100 orang",
    "kelas" : [
        
        "1. 9 Ikhwan 1", 
        "2. 9 Ikhwan 2", 
        "3. 9 Akhwat 1", 
        "4. 9 Akhwat 2"
        
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
