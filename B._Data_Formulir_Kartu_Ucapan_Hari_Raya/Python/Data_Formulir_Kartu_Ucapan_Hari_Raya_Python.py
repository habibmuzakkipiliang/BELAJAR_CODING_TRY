# Program Kartu Ucapan

print ("Program Kartu Ucapan \n")

raya = input ("Hari raya apa : ")
kata_tambahan = input ("Kata Tambahan :")
tahun = int (input ("Tahun berapa : "))
nama = input ("Nama kamu siapa : ")
panggil = input ("Nama panggilan apa : ")
kelas = input ("Dari kelas apa : ")
asal = input ("Asal daerah apa : ")
marga = input ("Marga nya apa : ")
suku = input ("Suku apa : ")
fans = input ("Kamu ngefans siapa : ")
oshi = input ("Kamu oshi nya siapa : ")


ucapan = f""" \n Selamat {raya} {tahun}, {kata_tambahan}

Salam dari :

- Nama    : {nama}
- Panggil : {panggil}
- Kelas   : {kelas}
- Asal    : {asal}
- Marga   : {marga}
- Suku    : {suku}
- Fans    : {fans}
- Oshi    : {oshi}

"""

print (ucapan)