# ==============================================================================
# PROGRAM KASIR TOKO BUKU DIGITAL - FINAL PROJECT

# Profil Habib Muzakki

nama = "Habib Muzakki"
asal = "Kota Serang"
gen = "Z Core (Inti)"
alumni_sekolah = "MAN 2 KOTA SERANG (Kelas atau Jurusan Agama) lulusan tahun 2026"
alumni_angkatan = "34 ASCENDRIA (lulusan 2026) MAN 2 KOTA SERANG"
coding = "HTML, CSS, JavaScript dan Python"
status = "Aspiring (Beginner) Full Stack Dev dan Bug Hunter"
jurusan = "D4 Vokasi Teknik Informatika (lebih suka Tech (Praktisi), bukan Math (Akademisi Teoritis))"
kampus = "Universitas Harkat Negeri Tegal"
lomba = "Finalis OSN-K Informatika tahun 2025"
fans = "JKT48 (Wota)"
game = "Minecraft Offline Android dan Warplane WW2  (World War 2) Dogfight Offline Android"
ig = "@habib_muzakki_piliang"
github = "https://github.com/habibmuzakkipiliang"
linkedin = "https://www.linkedin.com/in/habib-muzakki-piliang-15978b315/"


profil = f"""
- Nama lengkap    : {nama}
- Asal daerah     : {asal}
- Gen             : {gen}
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
tanggal = "26 Juli - 1 Agustus 2026"
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




# ==============================================================================

# --- MINI TASK 3: Struktur Data (List) ---

# Menyimpan daftar buku dan daftar harga

daftar_buku = [ 

    "1. Pemrograman Python Dasar",
    "2. Logika & Algoritma Kasir",
    "3. Panduan Clean Code Pemula"

]

daftar_harga = [50000, 35000, 45000]



# --- MINI TASK 5: Function (Modular Code) ---
def tampilkan_menu ():

    """Fungsi untuk menampilkan daftar menu buku"""
    
    print ("========================================")
    print ("      TOKO BUKU DIGITAL HABIB          ")
    print ("========================================")


    
    # --- MINI TASK 4: Perulangan (Looping) ---
    for buku in daftar_buku:
        print (buku)
    print ("========================================")



def hitung_diskon (total_belanja):

    """Fungsi logika diskon (Mini Task 1 & 2)"""

    # Jika total belanja di atas 50.000, dapat diskon 10%

    if total_belanja > 50000:
        diskon = total_belanja * 0.10

    else:
        diskon = 0

    return diskon


# --- MAIN PROGRAM (Integrasi Mini Task 1 - 5) ---
def jalankan_kasir ():
    
    # 1. Tampilkan menu
    tampilkan_menu ()


    
    # 2. Input dari pembeli (Mini Task 2)
    pilihan = int (input("Pilih nomor buku (1-3): "))
    jumlah = int (input("Masukkan jumlah buku: "))


    
    # 3. Logika Penentuan Harga (Mini Task 3)
    if pilihan == 1:
        nama_buku = "Pemrograman Python Dasar"
        harga_satuan = daftar_harga [0]

    elif pilihan == 2:
        nama_buku = "Logika & Algoritma Kasir"
        harga_satuan = daftar_harga [1]

    elif pilihan == 3:
        nama_buku = "Panduan Clean Code Pemula"
        harga_satuan = daftar_harga [2]
        
    else:
        print ("\nPilihan tidak valid! Program selesai.")
        return



    # 4. Hitung Subtotal & Diskon
    subtotal = harga_satuan * jumlah
    potongan = hitung_diskon (subtotal)
    total_bayar = subtotal - potongan



    # 5. Output Struk Pembayaran (Mini Task 1 & 2)
    print ("\n========================================")
    print ("          STRUK PEMBAYARAN              ")
    print ("========================================")
    print (f"Buku Dipilih  : {nama_buku}")
    print (f"Harga Satuan  : Rp {harga_satuan:,}")
    print (f"Jumlah Beli   : {jumlah}")
    print (f"Subtotal      : Rp {subtotal:,}")
    print (f"Diskon        : Rp {int (potongan):,}")
    print ("----------------------------------------")
    print (f"TOTAL BAYAR   : Rp {int (total_bayar):,}")
    print ("========================================")
    print (" Terima Kasih Telah Berbelanja di Toko Habib!")



# Jalankan Program Utama
jalankan_kasir ()