// Project Lengkap JavaScript di Intensive Camp Pemrograman JavaScript

console.log ("\n Project Lengkap JavaScript di Intensive Camp Pemrograman JavaScript \n")

console.log ("Hello World")



var nama = "Habib Muzakki"
var akrab = "Habib"
var asal = "Kota Serang, Banten"
var alumni = "Alumni MAN 2 KOTA SERANG (Kemenag) tahun 2023 - 2026"
var kelas = "Alumni Kelas Jurusan Agama tahun 2023 - 2026"
var angkatan = 34
var linkedin = "Habib Muzakki Piliang"
var instagram = "@habib_muzakki_piliang"
var github = "https://github.com/habibmuzakkipiliang"



var profil = `
- Dibuat oleh :

- Nama lengkap   : ${nama}
- Nama panggilan : ${akrab}
- Asal           : ${asal}
- Alumni         : ${alumni}
- Kelas          : ${kelas}
- Angkatan       : ${angkatan}
- LinkedIn       : ${linkedin}
- Instagram      : ${instagram}
- Github         : ${github}
`

console.log (profil)


console.log ("\n --- Batas --- \n")




console.log ("\n Input dan Output Formulir data \n")

var nama_lengkap = prompt ("Siapa Nama lengkap Kamu ? ")
var nama_panggilan = prompt ("Apa nama panggilan kamu ? ")
var asal = prompt ("Darimana asal kamu ? ")
var tempat = prompt ("Dimana tempat tinggal kamu ? ")
var kerja = prompt ("Kerja apa kamu sekarang ? ")
var tinggi = Number (prompt("Berapa tinggi badan kamu ? "))
var berat = Number (prompt ("Berapa berat badan kamu ? "))
var usia = Number (prompt ("Berapa usia kamu sekarang ? "))
var hobi = prompt ("Hobi kamu apa sekarang ? ")
var passion = prompt ("Passion kamu apa sekarang ? ")
var desimal = Number (prompt ("Ketik angka desimal terserah ? "))


var form = `
- Nama lengkap   : ${nama_lengkap}
- Nama panggilan : ${nama_panggilan}
- Asal           : ${asal}
- Tempat tinggal : ${tempat}
- Pekerjaan      : ${kerja}
- Tinggi badan   : ${tinggi}
- Berat badan    : ${berat}
- Usia           : ${usia}
- Hobi           : ${hobi}
- Passion        : ${passion}
- Desimal        : ${desimal}
`

console.log (form)


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe Data Pemrograman dasar \n")

var teks = "Halo Teks"
var angka = 12
var desimal = 3.14
var cek_1 = true
var cek_2 = false
var char = 'A'
var kosong = null


var tipe = `
- Teks    : ${teks}
- Angka   : ${angka}
- Desimal : ${desimal}
- Cek 1   : ${cek_1}
- Cek 2   : ${cek_2}
- Char    : ${char}
- Kosong  : ${kosong}
`

console.log (tipe)


console.log ("\n --- Batas --- \n")




console.log ("\n Free Class Pemrograman Python \n")

var kursus = "Special Skill Indonesia (2026) Online"
var tipe = "Bootcamp atau Kursus IT Coding"
var platform = "Zoom Meeting dan Google Colab"
var tutor = "Febriyanti Paramudita S.T (Data Science di Bank Rakyat Indonesia)"
var tanggal = "24 Mei 2026"
var waktu = "19.00 - 21.00 WIB"

var data = `
- Kursus   : ${kursus}
- Tipe     : ${tipe}
- Platform : ${platform}
- Tutor    : ${tutor}
- Tanggal  : ${tanggal}
- Waktu    : ${waktu}
`

console.log (data)


console.log ("\n --- Batas --- \n")




console.log ("\n Intensive Camp Pemrograman Python \n")

var kursus = "Special Skill Indonesia (2026) Online"
var tipe = "Bootcamp atau Kursus IT Coding"
var platform = "Zoom Meeting dan Google Colab"
var tutor = "Febriyanti Paramudita S.T (Data Science di Bank Rakyat Indonesia)"
var tanggal = "29 - 31 Mei 2026"
var waktu = "19.00 - 21.00 WIB"
var materi = [
     "1. Hello World",
     "2. Variabel, Sintaks, Komen dasar",
     "3. Operasi dasar (Aritmatika, Perbandingan dan Logika)",
     "4. F String",
     "5. Input dan Output data",
     "6. Percabangan dan Nested If (Match Case, If, Elif, Else)",
     "7. Perulangan dan Nested Loop (For dan While)",
     "8. Struktur data (List, Tuple, Set dan Dictionary)",
     "9. Fungsi (Dasar, Parameter dan Return)",
]


var data = `
- Kursus   : ${kursus}
- Tipe     : ${tipe}
- Platform : ${platform}
- Tutor    : ${tutor}
- Tanggal  : ${tanggal}
- Waktu    : ${waktu}
- Materi   :
`

console.log (data)

for (a = 0; a < materi.length; a++) {
     console.log (materi [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Variabel dasar \n")

var nama = "Halo Dunia"
console.log (nama)

console.log ("\n --- Batas --- \n")



var angka = 19
console.log (angka)

console.log ("\n --- Batas --- \n")



var desimal = 20.12
console.log (desimal)

console.log ("\n --- Batas --- \n")




console.log ("\n Kalkulator Operasi Arimatika dalam Fungsi pakai Return \n")

function tambah (a, b) {
     return a + b
}

function kurang (x, y) {
     return x - y
}

function kali (e, r) {
     return e * r
}

function bagi (w, k) {
     return w / k
}

function pangkat (l, p) {
     return l ** p
}

function modulus (k, m) {
     return k % m
}


hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 9)
hasil_3 = kali (10, 10)
hasil_4 = bagi (10, 2)
hasil_5 = pangkat (10, 3)
hasil_6 = modulus (10, 5)


console.log (hasil_1)
console.log (hasil_2)
console.log (hasil_3)
console.log (hasil_4)
console.log (hasil_5)
console.log (hasil_6)


console.log ("\n --- Batas --- \n")




console.log ("\n Operasi Perbandingan dan Logika \n")

var o = 10
var u = 5

var hasil = `
Operasi Perbandingan

- Hasil = ${o > u}
- Hasil = ${o < u}
- Hasil = ${o >= u}
- Hasil = ${o <= u}
- Hasil = ${o == u}
- Hasil = ${o != u}

-------------------------------

Operasi Logika

- Hasil = ${o > u && o < u}
- Hasil = ${o < u || o > u}
- Hasil = ${! (o < u)}
- Hasil = ${! (o > u)}
- Hasil = ${! o}
- Hasil = ${! u}
`

console.log (hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Match Case dengan Fungsi \n")

function jun (a) {
     
     switch (a) {

          case 1:
               console.log ("Oke")
               break
          
          case 2:
               console.log ("Setengah oke")
               break

          default:
               console.log ("Biasa aja")
     }
}

jun (1)
jun (2)
jun (3)


console.log ("\n --- Batas --- \n")




console.log ("\n Match Case 1 dengan Fungsi \n")

function warna (k) {

     switch (k) {
          
          case "Merah":
               console.log ("Warna Merah")
               break

          case "Biru":
               console.log ("Warna Biru")
               break

          case "Kuning":
               console.log ("Warna Kuning")
               break

          case "Ungu":
               console.log ("Warna Ungu")
               break

          case "Hijau":
               console.log ("Warna Hijau")
               break
          
          case "Nila":
               console.log ("Warna Nila")
               break

          default:
               console.log ("Warna lain")
     }
}

warna ("Nila")
warna ("Merah")
warna ("Biru")
warna ("Kuning")
warna ("Hijau")
warna ("Aqua")
warna ("Aquamarine")


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan dasar dengan Fungsi \n")

function fk (a) {
    
    if (a > 5) {
        console.log (`Besar, angka a = ${a}`)
    }
    
    else {
        console.log (`Kecil, angka a = ${a}`)
    }
}

fk (10)
fk (3)
fk (1)
fk (2)
fk (4)
fk (7)
fk (4)


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan dengan Fungsi \n")

function hj (b) {
    
    if (b > 5) {
        console.log (`Besar, angka b = ${b}`)
    }
    
    else if (b < 5) {
        console.log (`Kecil, angka b = ${b}`)
    }
    
    else {
        console.log (`Sama saja, angka b = ${b}`)
    }
}

hj (10)
hj (3)
hj (5)
hj (8)
hj (4)
hj (2)
hj (1)
hj (3)
hj (6)


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Ladder dengan Fungsi, nilai rapor \n")

function nilai (y) {
    
    if (y >= 95) {
        console.log (`A, nilai = ${y}`)
    }
    
    else if (y >= 90) {
        console.log (`B, nilai = ${y}`)
    }
    
    else if (y >= 80) {
        console.log (`C, nilai = ${y}`)
    }
    
    else if (y >= 70) {
        console.log (`D, nilai = ${y}`)
    }
    
    else if (y >= 60) {
        console.log (`E, nilai = ${y}`)
    }
    
    else if (y >= 50) {
        console.log (`F, nilai = ${y}`)
    }
    
    else {
        console.log (`Jelek banget, nilai = ${y}`)
    }
}

nilai (100)
nilai (95)
nilai (90)
nilai (80)
nilai (70)
nilai (60)
nilai (50)


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 dengan Fungsi \n")

function run (usia) {
    
    cek = true
    
    if (usia >= 17) {
        if (cek) {
            console.log (`Usia kamu kamu oke kok, usia = ${usia}`)
        }
        
        else if (usia <= 17) {
            console.log (`Usia kamu belum oke kok, usia = ${usia}`)
        }
    }
    
    else {
        console.log (`Kembali ke bocil, usia = ${usia}`)
    }
}

run (20)
run (13)
run (16)
run (17)
run (18)
run (20)


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 2 dengan fungsi \n")

function yun (f) {
    
    cek = true
    
    if (f > 5) {
        if (cek) {
            console.log (`Usia kamu udah oke kok, usia = ${f}`)
        }
        
        else {
            console.log (`Usia kamu belum kok, usia = ${f}`)
        }
    }
    
    else {
        console.log (`Usia kamu masih bocil, usia = ${f}`)
    }
}

yun (20)
yun (15)
yun (18)
yun (13)
yun (10)


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Majemuk Kompleks dengan Fungsi, persyaratan nonton bioskop film Pengantin Setan Indonesia 2026 \n")

function fg (usia, uang) {
    
    cek = true
    
    if ((usia >= 18) && (uang >= 50000)) {
        if (cek) {
            console.log (`Boleh nonton film horor yaitu Pengantin Setan, uang = ${uang} dan usia ${usia}`)
        }
        
        else if ((usia <= 18) && (uang <= 50000)) {
            console.log (`Jangan nontoh dibawah umur dan uang kecil untuk nonton film horor Pengantin Setan, uang = ${uang} dan usia = ${usia}`)
        }
        
        else {
            console.log (`Uang dan umur anda kurang, uang = ${uang} dan usia = ${usia}`)
        }
    }
    
    else {
        console.log (`Gak ada uang dan umur masih kurang, uang = ${uang} dan usia = ${usia}`)
    }
}

fg (19, 90000)
fg (20, 100000)
fg (18, 450000)
fg (25, 60000)
fg (10, 6000)
fg (12, 10000)       

          
console.log ("\n --- Batas --- \n")




console.log ("\n For Perulangan dasar \n")

for (a = 1; a < 11; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Perulangan dasar 2 \n")


for (b = 0; b < 20; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Perulangan dasar 3 \n")

for (c = 0; c < 30; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n While Perulangan Hitung Maju \n")

var a = 1

while (a < 15) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While Perulangan Hitung Mundur \n")

var b = 15

while (b > 0) {
    console.log (`Urutan ke - ${b}`)
    b--
}


console.log ("\n --- Batas --- \n")




console.log ("\n Do While Hitung Maju \n")

var c = 1

do {
    console.log (`Urutan ke - ${c}`)
    c++
}

while (c < 15)


console.log ("\n --- Batas --- \n")




console.log ("\n Do While Hitung Mundur \n")

var d = 15

do {
    console.log (`Urutan ke - ${d}`)
    d--
}

while (d > 0)


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 1 \n")

for (a = 0; a < 6; a++) {
    for (b = 0; b < 6; b++) {
        console.log (`Luar : ${a}, Dalam : ${b}`)
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 2 \n")

for (x = 0; x < 6; x++) {
    for (y = 0; y < 6; y++) {
        console.log (`Luar : ${x}, Dalam : ${y}`)
    }
}



console.log ("\n --- Batas --- \n")





console.log ("\n Array dan Methods \n")

var buah = [
     "Melon",
     "Semangka",
     "Apel",
     "Salak",
]

buah.push ("Buah Naga")
buah.push ("Buah Merah Papua")
buah.push ("Nangka") 
buah.push ("Nanas")
buah.push ("Mangga")
console.log (buah)


for (a = 0; a < buah.length; a++) {
    console.log (buah [a])
}
      
     
console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")

var data = {
     "nama" : "Johan",
     "kerja" : "IT Senior",
     "status" : "hidup",
     "asal" : "Amrik",
     "usia" : 20,
}

console.log ("Nama :", data ["nama"])
console.log ("Kerja :", data ["kerja"])
console.log ("Status :", data ["status"])
console.log ("Asal :", data ["asal"])
console.log ("Usia :", data ["usia"])


console.log ("\n --- Batas --- \n")





console.log ("\n Fungsi dengan parameter \n")

function run (nama, asal) {
     console.log (`Halo nama saya ${nama}, dari ${asal}`)
   
} 

run ("Hans", "Jerman")
run ("Luther", "Jerman")
run ("James", "Inggris")
run ("Frank", "Amerika")
run ("Frederick", "Jerman")
run ("Otto", "Jerman")

console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Parameter 2 \n")

function wer (nama, asal, tinggi) {
     console.log (`Halo nama saya ${nama}, dari ${asal}, dan tinggi badan saya ${tinggi}`)
}
     
wer ("Chuck", "Amerika", 175)
wer ("Leonard", "Amerika", 180)
wer ("Jansen", "Belanda", 190)
wer ("Luger", "Jerman", 175)
wer ("Jon", "Italia", 170)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar \n")

function tun () {
     console.log ("Hello World")
}
 
     
tun ()


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi \n")


var data = () => {
    console.log ("Hello World")
}


data ()


console.log ("\n --- Batas --- \n")





console.log ("\n Arrow Fungsi dengan Parameter \n")

var data = (nama) => {
    console.log (`Halo nama saya ${nama} dari Jakarta`)
}

data ("Hayyan")
data ("Rayyan")
data ("Ron")
data ("Fast")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Return \n")

var data = (a, b) => {
    return a + b
}

hasil = data (10, 10)
console.log (hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 1\n")

try {
    var hasil = 10 / e 
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 2\n")

try {
    var hasil = 20 / k
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 3\n")

try {
    var hasil = 10 + 10
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 4\n")

try {
    var hasil = 20 + 20
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Throw Error Handling 1 \n")

function er (a) {
    
    try {
        if (a < 0) {
            throw ("Gagal")
        }
        
        if (a >= 5) {
            console.log (`Besar, angka a = ${a}`)
        }
        
        else if (a <= 5) {
            console.log (`Kecil, angka a = ${a}`)
        }
        
        else {
            console.log (`Sama saja, angka a = ${a}`)
        }
    
    }
    
    catch (Error) {
        console.log (`Gak boleh minus, angka a = ${a}`)
    }
}

er (-10)
er (-2)
er (-6)
er (10)
er (3)
er (7)
er (5)

       
console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Throw dengan Error Handling \n")

function rus (b) {
    
    try {
        if (b < 0) {
            throw ("Gagal")
        }
        
        if (b >= 5) {
            console.log (`Besar, angka b = ${b}`)
        }
        
        else if (b <= 5) {
            console.log (`Kecil, angka b = ${b}`)
        }
        
        else {
            console.log (`Sama saja, angka b = ${b}`)
        }
    }
    
    catch (Error) {
        console.log (`Gak boleh minus, angka b = ${b}`)
    }
}

rus (10)
rus (-2)
rus (-7)
rus (3)
rus (7)
rus (5)


console.log ("\n --- Batas --- \n")