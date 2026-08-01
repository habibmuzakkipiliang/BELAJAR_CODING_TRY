# Profil Habib Muzakki

nama = "Habib Muzakki"
asal = "Kota Serang"
gen = "Z Core (Inti)"
alumni_sekolah = "MAN 2 KOTA SERANG (Kelas atau Jurusan Agama) lulusan tahun 2026"
alumni_angkatan = "34 ASCENDRIA (Lulusan tahun 2026) MAN 2 KOTA SERANG"
coding = "HTML, CSS, JavaScript dan Python"
status = "Aspiring (Beginner) Full Stack Dev dan Bug Hunter"
jurusan = "D4 Vokasi Teknik Informatika (lebih suka Tech (Praktisi), bukan Math (Akademisi Teoritis))"
kampus = "Universitas Harkat Negeri Tegal"
lomba = "Finalis OSN-K Informatika tahun 2025"
fans = "JKT48 (WOTA)"
ig = "@habib_muzakki_piliang"
game = "Minecraft Offline Android dan Warplane WW2 (World War 2) Dogfight Offline Android"
github = "https://github.com/habibmuzakkipiliang"
linkedin = "https://www.linkedin.com/in/habib-muzakki-piliang-15978b315/"


profil = f"""
- Nama lengkap    : {nama}
- Asal daerah     : {asal}
- Generasi        : {gen}
- Alumni sekolah  : {alumni_sekolah}
- Alumni angkatan : {alumni_angkatan}
- Coding          : {coding}
- Status          : {status}
- Jurusan         : {jurusan}
- Kampus          : {kampus}
- Lomba           : {lomba}
- Fans            : {fans}
- Game            : {game}
- Instagram       : {ig}
- Github          : {github}
- LinkedIn        : {linkedin}
"""

print (profil)


print ("\n --- batas --- \n")



# Dokumentasi Jadwal Free Bootcamp Pemrograman Python

judul = "Free Class Pemrograman Python"
tipe = "Bootcamp atau Kursus IT Coding"
bootcamp = "Special Skill Indonesia"
tanggal = "26 Juli - 3 Agustus 2026"
waktu = " Fleksibel"
tempat = "E-Learning dan WhatsApp Grup"
tutor = "Febriyanti Paramudita S.T (Data Science di Bank Rakyat Indonesia)"
materi = [
     "Mindset Programmer dan Algoritma",
     "Fundamental Python",
     "Struktur data dan Percabangan",
     "Perulangan dan Pattern Thinking",
     "Function dan Clean Code",
     "Utilizing AI (AI Agent Tools : Claude dan Antigravity)",
     "Final Project",
]

bootcamp_kursus = f"""
- Judul bootcamp   : {judul}
- Tipe bootcamp    : {bootcamp}
- Tanggal bootcamp : {tanggal} 
- Waktu bootcamp   : {waktu}
- Tempat           : {tempat}
- Tutor            : {tutor}
- Materi           :
"""

print (bootcamp_kursus)

for a in materi:
     print (a)


print ("\n --- batas --- \n")




# ----------------------

# MINI TASK 2: Menerjemahkan Algoritma ke Python
# Program Pembayaran Kopi Sederhana

# ---------------------------------


# 1. Variabel dan input (dengan Integer)

harga_kopi = int (input ("Masukkan harga kopi :"))
jumlah_kopi = int (input ("Masukkan jumlah kopi :"))


# 2. Operasi dasar Awal

total_harga = harga_kopi * jumlah_kopi


# 3. Percabangan dasar

if total_harga > 50000:
     diskon = 5000
     print (f"Anda dapet diskon 5000")

else:
     diskon = 0
     print ("Anda tidak dapet diskon")


# 4. Total akhir

total_bayar = total_harga - diskon


# Output

print (f"Total harga yang harus dibayar, harga = {total_bayar}")


print ("\n --- batas --- \n")