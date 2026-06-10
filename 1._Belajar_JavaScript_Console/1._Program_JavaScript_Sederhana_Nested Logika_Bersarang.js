// Program JavaScript Sederhana Nested Logika Bersarang 

console.log ("\n Program JavaScript Sederhana Nested Logika Bersarang \n")


console.log ("\n Tipe data dasar \n")


var string = "Halo Michie JKT48"
var angka = 22
var desimal = 33.64
var cek = true
var cek_1 = false
var kosong = null


console.log ("String =", string)
console.log ("Angka =", angka)
console.log ("Desimal =", desimal)
console.log ("Cek =", cek)
console.log ("Cek 1 =", cek_1)
console.log ("Kosong =", kosong)


console.log ("\n --- Batas --- \n")




console.log ("\n Oshi (Member Favorit) saya \n")


var array = [
    
    "1. Michie JKT48 (Utama)",
    "2. Fritzy JKT48 (Utama)",
    "3. Anindya JKT48 (Utama)",
    "4. Christy JKT48 (Utama)",
    "5. Freya JKT48",
    "6. Olla JKT48",
    "7. Jessi JKT48",
    "8. Fiony JKT48",
    "9. Muthe JKT48",
    "10. Marsha JKT48",
    "11. Eli JKT48",
    "12. Mikaela JKT48",
    "13. Yui Oguri (AKB48)",
    "14. Endo Rino (Rain Tree)",
    
    ]


for (a = 0; a < array.length; a++) {
    console.log (array [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Objek (Dictionary) \n")


var objek = {
    
    "nama" : "Johan Dick",
    "asal" : "Amerika Serikat",
    "job" : "Programmer dan Software Engineer",
    "coding" : "Python, JavaScript dan Dart (Flutter)",
    "tinggi_badan" : "175 cm",
}


console.log ("Nama :", objek ["nama"])

console.log ("Asal :", objek ["asal"])

console.log ("Kerja :", objek ["job"])

console.log ("Coding :", objek ["coding"])

console.log ("Tinggi badan :", objek ["tinggi_badan"])


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case \n")


var kondisi = 8

switch (kondisi) {
    
    case 1:
        console.log ("Ada Energi")
        break
        
    case 2:
        console.log ("Kenyang banget")
        break
        
    case 3:
        console.log ("Kenyang parah")
        break
        
    case 4:
        console.log ("Kenyang dikit")
        break
        
    case 5:
        console.log ("Agak kenyang")
        break
        
    case 6:
        console.log ("Agak laper")
        break
        
    case 7:
        console.log ("Laper dikit")
        break
        
    case 8:
        console.log ("Laper parah")
        break
        
    case 9:
        console.log ("Laper banget")
        break
        
    case 10:
        console.log ("Gak ada Energi")
        break
        
    default:
    console.log ("Udah kembali aja deh ke rumah")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Dasar \n")

var a = 10

if (a > 5) {
    console.log (`Besar, angka = ${a}`)
}

else {
    console.log (`Kecil, angka = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan \n")


var b = 3

if (b > 5) {
    console.log (`Besar, angka = ${b}`)
}

else if (b < 5) {
    console.log (`Kecil, angka = ${b}`)
}

else {
    console.log (`Semula, angka = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Nested Percabangan If level 1 (Else If) \n")


var a = 10
var cek = true

if (cek) {
    if (a > 5) {
        console.log (`Besar, nilai = ${a}`)
    }
    
    else if (a < 5) {
         console.log (`Kecil, nilai = ${a}`)
    }
}

else {
    console.log (`Semula, nilai = ${a}`)
}


console.log ("\n --- Batas --- \n")




var b = 2
var cek = true

if (cek) {
    if (b > 5) {
        console.log (`Besar, nilai = ${b}`)
    }
    
    else if (b < 5) {
        console.log (`Kecil, nilai = ${b}`)
    }
}

else {
    console.log (`Semula, nilai = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Nested Percabangan If level 1 (Else) \n")


var c = 9
var cek = true

if (cek) {
    if (c > 5) {
        console.log (`Besar, nilai = ${c}`)
    }
    
    else {
        console.log (`Kecil, nilai = ${c}`)
    }
}

else {
    console.log (`Semula, nilai = ${c}`)
}


console.log ("\n --- Batas --- \n")




var d = 3
var cek = true

if (cek) {
    if (d > 5) {
        console.log (`Besar, nilai = ${d}`)
    }
    
    else {
        console.log (`Kecil, nilai = ${d}`)
    }
}

else {
    console.log (`Semula, nilai = ${d}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Nilai Rapor Sederhana \n")


var nilai = 100

if (nilai >= 90) {
    console.log (`A, nilai = ${nilai}`)
}

else if (nilai >= 80) {
    console.log (`B, nilai = ${nilai}`)
}

else if (nilai >= 75) {
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
    console.log (`Jelek semua nilainya, nilai = ${nilai}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Skor UTBK dan SNBT \n")


var skor = 1000

if (skor >= 900) {
    console.log (`A, nilai = ${skor}`)
}

else if (skor >= 800) {
    console.log (`B, nilai = ${skor}`)
}

else if (skor >= 750) {
    console.log (`C, nilai = ${skor}`)
}

else if (skor >= 700) {
    console.log (`D, nilai = ${skor}`)
}


else if (skor >= 600) {
    console.log (`E, nilai = ${skor}`)
}

else if (skor >= 500) {
    console.log (`F, nilai = ${skor}`)
}

else {
    console.log (`Jelek amat nilanya, nilai = ${skor}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested level 3 (Usia Produktif Manusia) \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Masuk usia produktif, dan usia = ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah masuk usia lanjut dan usia = ${usia}`)
    }
    
    else {
        console.log (`Bukan usia produktif, dan usia = ${usia}`)
    }
}

else {
    console.log (`Masih dibawah usia produktif, dan usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested level 3 (Join ke member JKT48) \n")


var umur = 18
var cek = true

if (cek) {
    if ((umur >= 13) && (umur <= 19)) {
        console.log (`Kamu boleh ikut audisi JKT48, dan usia = ${umur}`)
    }
    
    else if (umur > 19) {
        console.log (`Kamu sudah matang, gabung ke JKT48, dan usia = ${umur}`)
    }
    
    else {
        console.log (`Gak lolos audisi JKT48, usia = ${umur}`)
    }
}

else {
    console.log (`Belum bisa ikut audisi JKT48, usia = ${umur}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar \n")


for (a = 0; a < 8; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




for (b = 0; b < 9; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")




for (c = 0; c < 6; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar \n")


var a = 3

while (a < 9) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




var b = 6

while (b < 11) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")




var c = 6 

while (c < 14) {
    console.log (`Urutan ke - ${c}`)
    c++
}


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar \n")


var a = 3

do {
    console.log (`Urutan ke - ${a}`)
    a++
} while (a < 11)


console.log ("\n --- Batas --- \n")




var b = 4

do {
    console.log (`Urutan ke - ${b}`)
    b++
} while (b < 13)


console.log ("\n --- Batas --- \n")




var c = 5

do {
    console.log (`Urutan ke - ${c}`)
    c++
} while (c < 18)


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested \n")


for (a = 0; a < 5; a++) {
    for (b = 0; b < 5; b++) {
        console.log (`Urutan ke - ${a} dan Urutan ke - ${b}`)
    }
}


console.log ("\n --- Batas --- \n")




for (c = 0; c < 4; c++) {
    for (d = 0; d < 4; d++) {
        console.log (`Urutan ke - ${c} dan Urutan ke - ${d}`)
    }
}


console.log ("\n --- Batas --- \n")




for (e = 0; e < 3; e++) {
    for (f = 0; f < 3; f++) {
        console.log (`Urutan ke - ${e} dan Urutan ke - ${f}`)
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Dasar \n")


function dasar () {
    console.log ("Hello World")
}

dasar ()


console.log ("\n --- Batas --- \n")




function ser () {
    console.log ("Hello World Indonesia")
}

ser ()


console.log ("\n --- Batas --- \n")




function der () {
    console.log ("Dart")
    console.log ("Sert")
    console.log ("Rart")
    console.log ("Dran")
}

der ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Parameter \n")


function daf (nama) {
    console.log ("Hello " + nama + " dari Jakarta")
}

daf ("Run")
daf ("Rurt")
daf ("Fart")
daf ("Sert")
daf ("Dan")
daf ("Rust")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Parameter 2 \n")


function der (nama) {
    console.log (`Halo ${nama} dari Tangerang`)
}

der ("Fun")
der ("Has")
der ("Hef")
der ("Runner")
der ("Hujan")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Return \n")


function tambah (a, b) {
    return a + b
}

var hasil = tambah (10, 9)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




function dun (nama) {
    return `Halo ${nama} dari Fx Sudirman`
}

var hasil = dun ("Michie JKT48")
console.log (hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dasar \n")


var hasil = () => {
    console.log ("Hello Run")
    console.log ("Hello Far")
    console.log ("Hello Rur")
    console.log ("Hello Ser")
}

hasil ()


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan Parameter \n")

var hasil = (nama) => {
    console.log ("Hello " + nama + " JKT48")
}

hasil ("Michie")
hasil ("Fritzy")
hasil ("Anindya")
hasil ("Christy")
hasil ("Freya")
hasil ("Olla")


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling \n")

try {
    var hasil = 10 / 0
    console.log (hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 1 \n")

try {
    var hasil = 20 / 0
    console.log (hasil)
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
    var hasil = 30 / 0
    console.log (hasil)
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
    var hasil = 10 + 9
    console.log (hasil)
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
    var hasil = 45 + 3
    console.log (hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")
