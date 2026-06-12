// Latihan Coding JavaScript

console.log ("\n Latihan Coding JavaScript \n")


console.log ("Hello World")


console.log ("\n --- Batas --- \n")




console.log ("\n Sintaks dasar \n")


var nama = "Jansen Rust"
var umur = "25 tahun"
var tinggi = "170 cm"
var coding = "HTML, CSS, JavaScript dan Python"
var warga = "Amerika Serikat"
var asal = "Silicon Valley"


console.log ("Nama :", nama)
console.log ("Umur :", umur)
console.log ("Tinggi badan :", tinggi)
console.log ("Coding :", coding)
console.log ("Warga :", warga)
console.log ("Asal :", asal)


console.log ("\n --- Batas --- \n")




console.log ("\n Sintaks dasar 2\n")


var nama = "Habib Muzakki"
var marga = "Piliang"
var kelas = "12 Agama"
var absen = 15
var coding = "HTML, CSS, JavaScript dan Python"
var sekolah = "MAN 2 KOTA SERANG"
var tinggi = "170 cm"


console.log ("Nama :", nama)
console.log ("Marga :", marga)
console.log ("Kelas :", kelas)
console.log ("Absen :", absen)
console.log ("Coding :", coding)
console.log ("Sekolah :", sekolah)
console.log ("Tinggi badan :", tinggi)


console.log ("\n --- Batas --- \n")




console.log ("\n Membedakan Deklarasi Var, Let, dan Const \n")


console.log ("\n Pakai Var \n")


var teks = "Member JKT48"
var angka = 12
var desimal = 3.14
var cek_1 = true
var cek_2 = false
var kosong = null


console.log ("Teks =", teks)
console.log ("Angka =", angka)
console.log ("Desimal =", desimal)
console.log ("Cek 1 =", cek_1)
console.log ("Cek 2 =", cek_2)
console.log ("Kosong =", kosong)


console.log ("\n --- Batas --- \n")




console.log ("\n Pakai Let \n")


let teks_1 = "Member JKT48"
let angka_1 = 12
let desimal_1 = 3.14
let cek_x = true
let cek_y = false
let kosong_1 = null


console.log ("Teks 1 =", teks_1)
console.log ("Angka 1 =", angka_1)
console.log ("Desimal 1 =", desimal_1)
console.log ("Cek X =", cek_x)
console.log ("Cek Y =", cek_y)
console.log ("Kosong 1 =", kosong_1)


console.log ("\n --- Batas --- \n")




console.log ("\n Pakai Const \n")


const teks_2 = "Member JKT48"
const angka_2 = 12
const desimal_2 = 3.14
const cek_a = true
const cek_b = false
const kosong_2 = null


console.log ("Teks 2 =", teks_2)
console.log ("Angka 2 =", angka_2)
console.log ("Desimal 2 =", desimal_2)
console.log ("Cek A =", cek_a)
console.log ("Cek B =", cek_b)
console.log ("Kosong 2 =", kosong_2)


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe data dasar \n")


var teks = "Tes aja"
var angka = 34
var desimal = 34.2
var cek_1 = true
var cek_2 = false
var kosong = null


console.log ("Teks =", teks)
console.log ("Angka =", angka)
console.log ("Desimal =", desimal)
console.log ("Cek 1 =", cek_1)
console.log ("Cek 2 =", cek_2)
console.log ("Kosong =", kosong)


console.log ("\n --- Batas --- \n")




console.log ("\n Operasi Dasar \n")


var x = 25
var y = 5


console.log ("Tambah =", x + y)
console.log ("Kurang =", x - y)
console.log ("Kali =", x * y)
console.log ("Bagi =", x / y)
console.log ("Pangkat =", x ** y)
console.log ("Modulus =", x % y)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Perbandingan \n")


console.log ("Hasil =", x > y)
console.log ("Hasil =", x > y)
console.log ("Hasil =", x >= y)
console.log ("Hasil =", x <= y)
console.log ("Hasil =", x == y)
console.log ("Hasil =", x != y)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Logika \n")


console.log ("Hasil =", (x > y) && (x < y))
console.log ("Hasil =", (x < y) || (x > y))
console.log ("Hasil =", (!x))
console.log ("Hasil =", (!y))


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case \n")


var nilai = 95

switch (nilai) {
    
    case 95:
        console.log ("A")
        break
      
    case 90:
        console.log ("B")
        break
         
    case 80:
        console.log ("C")
        break
        
    case 75:
        console.log ("D")
        break
        
    case 70:
        console.log ("E")
        break
    
    case 60:
        console.log ("F")
        break
        
    default:
    console.log ("Sama saja")
    
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 2 \n")


var kondisi = 2

switch (kondisi) {
    
    case 1:
        console.log ("Iya")
        break
        
    case 2:
        console.log ("Tidak")
        break
        
    case 3:
        console.log ("Kadang-kadang")
        break
        
    default:
    console.log ("Bukan dong")
    
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan dasar \n")


var c = 3

if (c >= 5) {
    console.log (`Besar, nilai = ${c}`)
}

else {
    console.log (`Kecil, nilai = ${c}`)
}


console.log ("\n --- Batas --- \n")



console.log ("\n Percabangan Lanjutan \n")


var a = 7

if (a >= 5) {
    console.log (`Besar, nilai = ${a}`)
}

else if (a <= 5) {
    console.log (`Kecil, nilai = ${a}`)
}

else {
    console.log (`Sama saja, nilai = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Skor Sederhana \n")


var b = 5

if (b >= 9) {
    console.log (`A, nilai = ${b}`)
}

else if (b >= 8) {
    console.log (`B, nilai = ${b}`)
}

else if (b >= 7) {
    console.log (`C, nilai = ${b}`)
}

else if (b >= 6) {
    console.log (`D, nilai = ${b}`)
}

else if (b >= 5) {
    console.log (`E, nilai = ${b}`)
}

else if (b >= 4) {
    console.log (`F, nilai = ${b}`)
}

else {
    console.log (`Sama saja, nilai = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nilai Rapor Sederhana \n")


var nilai = 95

if (nilai >= 95) {
    console.log (`A, nilai = ${nilai}`)
}

else if (nilai >= 90) {
    console.log (`B, nilai = ${nilai}`)
}

else if (nilai >= 80) {
    console.log (`C, nilai = ${nilai}`)
}

else if (nilai >= 70) {
    console.log (`D, nilai = ${nilai}`)
}

else if (nilai >= 60) {
    console.log (`E, nilai = ${nilai}`)
}

else if (nilai >= 50) {
    console.log (`F, nilai = ${nilai}`)
}

else {
    console.log (`Sama saja, nilai = ${nilai}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar \n")


for (a = 0; a < 11; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




for (b = 0; b < 11; b++) {
    console.log (`Urutan ke- ${b}`)
}


console.log ("\n --- Batas --- \n")




for (c = 0; c < 11; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar \n")


var a = 2

while (a < 11) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




var b = 5

while (b < 16) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")




var e = 3

while (e < 11) {
    console.log (`Urutan ke - ${e}`)
    e++
}


console.log ("\n --- Batas --- \n")





console.log ("\n Do While dasar \n")


var e = 8

do {
    console.log (`Urutan ke - ${e}`)
    e++
} while (e < 17)


console.log ("\n --- Batas --- \n")




var h = 3

do {
    console.log (`Urutan ke - ${h}`)
    h++
} while (h < 7)


console.log ("\n --- Batas --- \n")




var d = 5

do {
    console.log (`Urutan ke - ${d}`)
    d++
} while (d < 17)


console.log ("\n --- Batas --- \n")




console.log ("\n Array \n")


var data = [
    
    "1. Nangka",
    "2. Melon",
    "3. Semangka",
    "4. Buah Naga",
    "5. Pepaya",
    "6. Buah Anggur",
    
    ]
    
    
for (a = 0; a < data.length; a++) {
    console.log (data [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Array 2 \n")


var daftar = [
    
    "1. Rendang",
    "2. Nasi Padang",
    "3. Nasi Kapau",
    "4. Ayam Gulai",
    "5. Rendang Daging",
    "6. Sala lauak",
    
    ]
    
    
for (b = 0; b < daftar.length; b++) {
    console.log (daftar [b])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")


var profil = {
    
    "nama" : "Jansen Rust",
    "umur" : "25 tahun",
    "tinggi" : "170 cm",
    "coding" : "HTML, CSS, JavaScript, dan Python",
    "warga" : "Amerika Serikat",
    "asal" : "Silicon Valley",
    
}


console.log ("Nama :", profil ["nama"])

console.log ("Umur :", profil ["umur"])

console.log ("Tinggi :", profil ["tinggi"])

console.log ("Coding :", profil ["coding"])

console.log ("Asal :", profil ["asal"])


console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary 2 \n")


var profil = {
    
    "nama" : "Habib Muzakki",
    "marga" : "Piliang",
    "kelas" : "12 Agama",
    "absen" : 15,
    "coding" : "HTML, CSS, JavaScript, Python",
    "sekolah" : "MAN 2 KOTA SERANG",
    "tinggi" : "170 cm",
    
}


console.log ("Nama :", profil ["nama"])

console.log ("Marga :", profil ["marga"])

console.log ("Kelas :", profil ["kelas"])

console.log ("Absen :", profil ["absen"])

console.log ("Coding :", profil ["coding"])

console.log ("Sekolah :", profil ["sekolah"])

console.log ("Tinggi badan :", profil ["tinggi"])


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar \n")


function dasar () {
    console.log ("Hello World")
}

dasar ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar 1 \n")


function suf () {
    console.log ("Hello Dun")
    console.log ("Hello Ser")
    console.log ("Hello Der")
    
}

suf ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar 2 \n")


function det () {
    console.log ("Helo Jan")
}

det ()
det ()
det ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan parameter 1 \n")


function ren (nama) {
    console.log ("Hello " + nama + " dari Glodok, Jakbar")
}

ren ("Anton Djin Yan")
ren ("Reyvon Djan")
ren ("Ren Hard")
ren ("Ben Anderson")
ren ("Dart Bento Djin Zhan")

console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan parameter 2 \n")


function rf (nama) {
    console.log (`Halo nama ${nama}, dari Jakarta Timur dan Jatinegara`)
}

rf ("E")
rf ("A")
rf ("R")
rf ("S")
rf ("V")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Parameter 3 spesial oshi member JKT48 \n")


function oshi (nama) {
    console.log (`Halo ${nama} cantik`)
}

oshi ("Michie JKT48")
oshi ("Frizy JKT48")
oshi ("Anindya JKT48")
oshi ("Christy JKT48")
oshi ("Freya JKT48")
oshi ("Olla JKT48")
oshi ("Jessi JKT48")
oshi ("Fiony JKT48")
oshi ("Muthe JKT48")
oshi ("Marsha JKT48")
oshi ("Eli JKT48")
oshi ("Mikaela JKT48")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan return \n")


function tambah (a, b) {
    return a + b
}

var hasil = tambah (10, 10)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan return 1 \n")


function der (nama) {
    return "Halo " + nama + " Asal dari Jakarta"
}

var hasil = der ("Johan")
console.log ("Hasil =", hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan return 2 \n")


function dar (nama) {
    return `Halo semuanya, saya ${nama}, dari Indonesia`
}

var hasil = dar ("Hayyan")
console.log ("Hasil =", hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dasar \n")


var hasil = () => {
    console.log ("Hello World")
}

hasil ()


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi 1 \n")


var hasil = () => {
    console.log ("Hello Dart")
    console.log ("Hello Rur")
    console.log ("Hello Sun")
    console.log ("Hello Ikal")
    console.log ("Hello Dun")
    console.log ("Hello Fans JKT48")
}

hasil ()


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan parameter \n")


var hasil = (nama) => {
    console.log ("Hello " + nama + " Dari Informatika")
}

hasil ("Hans")
hasil ("Fans")
hasil ("Rar")
hasil ("Dart")
hasil ("Fonter")


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan return \n")


var tambah = (a, b) => {
    return a + b
}

var hasil = tambah (10, 10)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")



console.log ("\n Arrow Fungsi dengan parameter 3 \n")


var oshi = (nama) => {
    console.log (`Halo ${nama} Cantik`)
}

oshi ("Michie JKT48")
oshi ("Frizy JKT48")
oshi ("Anindya JKT48")
oshi ("Christy JKT48")
oshi ("Freya JKT48")
oshi ("Olla JKT48")
oshi ("Jessi JKT48")
oshi ("Fiony JKT48")
oshi ("Muthe JKT48")
oshi ("Marsha JKT48")
oshi ("Eli JKT48")
oshi ("Mikaela JKT48")


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan return 2 \n")


var hasil = (nama) => {
    return "Halo " + nama + " Dari Jakarta"
}

var ras = hasil ("Guran")
console.log (ras)


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan return 3 \n")


var tar = (nama) => {
    return `Halo ${nama}, dari Indonesia`
}

var hasil = tar ("Rans")
console.log (hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling \n")


try {
    var hasil = 10 / 0
    console.log ("Hasil =", hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")



console.log ("\n Error Handling 2 \n")


try {
    var hasil = 20 / 0
    console.log ("Hasil =", hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 3 \n")


try {
    var hasil = 10 + 10
    console.log ("Hasil =", hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 4 \n")


try {
    var hasil = 20 + 20
    console.log ("Hasil =", hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 \n")


var a = 9
var cek = true

if (cek) {
    if (a >= 5) {
        console.log (`Besar, nilai = ${a}`)
    }
    
    else if (a <= 5) {
        console.log (`Kecil, nilai = ${a}`)
    }
}

else {
    console.log (`Sama saja, nilai = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 2 \n")


var b = 3
var cek = true

if (cek) {
    if (b >= 5) {
        console.log (`Besar, nilai = ${b}`)
    }
    
    else {
        console.log (`Kecil, nilai = ${b}`)
    }
}

else {
    console.log (`Sama saja, nilai = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, Daftar masuk JKT48 \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 13) && (usia <= 17)) {
        console.log (`Sudah boleh daftar JKT48, usia = ${usia}`)
    }
    
    else if (usia > 17) {
        console.log (`Sudah matang masuk JKT48, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum boleh ya, ${usia}`)
    }
}

else {
    console.log (`Jangan dulu ya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia produktif manusia \n")


var umur = 25
var cek = true

if (cek) {
    if ((umur >= 15) && (umur <= 64)) {
        console.log (`Masuk usia produktif, umur = ${umur}`)
    }
    
    else if (umur > 64) {
        console.log (`Masuk lanjut usia, umur = ${umur}`)
    }
    
    else {
        console.log (`Bukan usia produktif, umur = ${umur}`)
    }
}

else {
    console.log (`Masih kecil usianya, umur = ${umur}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested \n")


for (a = 0; a < 4; a++) {
    for (b = 0; b < 4; b++) {
        console.log (`Urutan ke - ${a}, dan Urutan ke - ${b}`)
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 1 \n")


for (k = 0; k < 4; k++) {
    for (j = 0; j < 4; j++) {
        console.log (`Urutan ke - ${k} dan Urutan ke - ${j}`)
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 2 \n")


for (w = 0; w < 5; w++) {
    for (s = 0; s < 5; s++) {
        console.log (`Urutan ke - ${w} dan Urutan ke - ${s}`)
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 3 \n")


for (x = 0; x < 4; x++) {
    for (y = 0; y < 4; y++) {
        for (z = 0; z < 4; z++) {
            console.log (`Urutan ke - ${x}, Urutan ke - ${y}, dan Urutan ke - ${z}`)
        }
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 4 \n")


for (j = 0; j < 5; j++) {
    for (d = 0; d < 5; d++) {
        for (f = 0; f < 5; f++) {
            console.log (`Urutan ke - ${j}, Urutan ke - ${d} dan Urutan ke - ${f}`)
        }
    }
}


console.log ("\n --- Batas --- \n")
