// Belajar JavaScript Dasar

console.log ("Hello World")

console.log ("\n --- Batas --- \n")




console.log ("\n Variabel Dan Template Literals \n")

var nama = "Habib Muzakki"
var sekolah = "MAN 2 KOTA SERANG"
var kelas = "Kelas 12 Agama"
var asal = "Bukittinggi"
var suku = "Minangkabau"
var marga = "Piliang"
var tinggal = "Kota Serang, Banten"

var detail = `Saya ${nama}, dan saya alumni kelas ${kelas} dan dari alumni sekolah ${sekolah} dan asal saya dari ${asal} dan suku saya dari ${suku} dan marga saya adalah ${marga} dan tempat tinggal di ${tinggal}`

console.log (detail)


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe data pemrograman \n")

var teks = "Halo Dunia"
var angka = 12
var desimal = 12.34
var char = 'A'
var cek = true

var dani = `
- Nama    : ${teks}
- Angka   : ${angka}
- Desimal : ${desimal}
- Char    : ${char}
- Cek     : ${cek}

`

console.log (dani)


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 1 \n")

var warna = "Merah"

switch (warna) {
    
    case "Merah":
        console.log ("Merah")
        break
        
    default:
    console.log ("Warna lain")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 2 \n")

var kondisi = 2

switch (kondisi) {
    
    case 1:
        console.log ("Oke")
        break
        
    case 2:
        console.log ("Mantap")
        break
        
    case 3:
        console.log ("Udah oke banget")
        break
        
    case 4:
        console.log ("Sedang kok")
        break
        
    default:
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 3 \n")

var cek = "Senang"

switch (cek) {
    
    case "Senang":
        console.log ("Senang")
        break
        
    case "Bahagia":
        console.log ("Bahagia")
        break
        
    case "Sedih":
        console.log ("Sedih")
        break
        
    case "Kesal":
        console.log ("Kesal")
        break
        
    default:
    console.log ("Masih ada waktu dan tetap berusaha lagi")
}


console.log ("\n --- batas --- \n")




console.log ("\n Percabangan dasar \n")

var a = 9

if (a > 5) {
    console.log (`Besar, a = ${a}`)
}

else {
    console.log (`Kecil, a = ${a}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Percabangan Lanjutan \n")

var b = 4

if (b > 5) {
    console.log (`Besar, b = ${b}`)
}

else if (b < 5) {
    console.log (`Kecil, b = ${b}`)
}

else {
    console.log (`Sama saj, b = ${b}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Percabangan Lanjutan 2 \n")

var c = 9

if (c > 5) {
    console.log (`Besar, c = ${c}`)
}

else if (c < 5) {
     console.log (`Kecil, c = ${c}`)
}

else {
    console.log (`Sama saja, c = ${c}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Percabangan Nested Majemuk Kompleks 1 \n")

var usia = 1
var uang = 3000

if ((usia >= 17) && (usia >= 5000)) {
    if (cek == true) {
        console.log (`Udah oke, usia = ${usia} dan uang = ${uang}`)
    }
    
    else if ((usia <= 17) && (uang <= 5000)) {
        console.log (`Belum, usia = ${usia} dan uang = ${uang}`)
    }
}

else {
    console.log (`Masih belum dong sama sekali, usia = ${usia} dan uang = ${uang}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Percabangan Nested Majemuk Kompleks \n")

var usia = 19
var cek = true

if ((usia >= 15) && (usia <= 64)) {
    if (cek == true) {
        console.log (`Sudah masuk usia produktif, usia = ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah tua dong, usia = ${usia}`)
    }
    
    else {
        console.log (`Remaja dong usia = ${usia}`)
    }
}

else {
    console.log (`Masih balita dong, usia = ${usia}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Nested 1 \n")

var a = 10
var cek = true

if (cek) {
    if (a > 5) {
        console.log (`Besar, a = ${a}`)
    }
    
    else if (a < 5) {
        console.log (`Kecil, a = ${a}`)
    }
}

else {
    console.log (`Sama saja, a = ${a}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Nested 2 \n")

var b = 3
var cek = true

if (cek) {
    if (b > 5) {
        console.log (`Besar, b = ${b}`)
    }
    
    else {
        console.log (`Kecil, b = ${b}`)
    }
}

else {
    console.log (`Sama saja, b = ${Besar}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Percabangan Ladder \n")

var nilai = 90

if (nilai >= 90) {
    console.log (`A++, nilai = ${nilai}`)
}

else if (nilai >= 80) {
    console.log (`B, nilai = ${nilai}`)
}

else if (nilai >= 70) {
    console.log (`C, nilai = ${nilai}`)
}

else if (nilai >= 60) {
    console.log (`D, nilai = ${nilai}`)
}

else if (nilai >= 50) {
    console.log (`E, nilai = ${nilai}`)
}

else {
    console.log (`Sama saja, nilai = ${nilai}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n For Perulangan \n")

for (a = 1; a < 10; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n For Perulangan 1 \n")

for (b = 5; b < 20; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n For Perulangan 2 \n")

for (c = 0; c < 25; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n For Perulangan 3 \n")

for (d = 0; d < 11; d++) {
    console.log (`Urutan ke - ${d}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n While Perulangan \n")

var a = 5

while (a < 15) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- batas --- \n")




console.log ("\n While Perulangan 1 \n")

var b = 15

while (b < 30) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- batas --- \n")




console.log ("\n While Perulangan 2 \n")


var c = 15

while (c < 30) {
    console.log (`Urutan ke - ${c}`)
    c++
}


console.log ("\n --- batas --- \n")




console.log ("\n Do While Perulangan 1 \n")


var a = 10

do {
    console.log (`Urutan ke - ${a}`)
    a++
}

while (a < 30)


console.log ("\n --- batas --- \n")




console.log ("\n Do While Perulangan 2 \n")


var b = 10

do {
    console.log (`Urutan ke - ${b}`)
    b++
}

while (b < 35)


console.log ("\n --- batas --- \n")




console.log ("\n Do While Perulangan 3 \n")

var c = 15

do {
    console.log (`Urutan ke - ${c}`)
    c++
}

while (c < 35)


console.log ("\n --- batas --- \n")




console.log ("\n For Nested 1 \n")

for (a = 0; a < 7; a++) {
    for (b = 0; b < 7; b++) {
        console.log (`Luar : ${a} dan Dalam : ${b}`)
    }
}


console.log ("\n --- batas --- \n")




console.log ("\n For Nested 2 \n")

for (x = 0; x < 7; x++) {
    for (y = 0; y < 7; y++) {
        console.log (`Luar : ${x} dan Dalam : ${y}`)
    }
}


console.log ("\n --- batas --- \n")




console.log ("\n For Nested 3 \n")

for (k = 0; k < 4; k++) {
    for (j = 0; j < 4; j++) {
        for (b = 0; b < 4; b++) {
            for (n = 0; n < 4; n++) {
                console.log (`K : ${k}, J : ${j}, B : ${b}, N : ${n}`)
            }
        }
    }
}


console.log ("\n --- batas --- \n")




console.log ("\n Array Oshi JKT48 \n")

var oshi = [
     "1. Michie JKT48",
     "2. Gracie JKT48",
     "3. Lily JKT48",
     "4. Fritzy JKT48",
     "5. Anindya JKT48",
     "6. Christy JKT48",
     "7. Freya JKT48",
]


oshi.push ("8. Olla JKT48")
oshi.push ("9. Jessi JKT48")
oshi.push ("10. Muthe JKT48")
oshi.push ("11. Fiony JKT48")
oshi.push ("12. Marsha JKT48")
oshi.push ("13. Eli JKT48")
oshi.push ("14. Mikaela JKT48")
oshi.push ("15. Ekin JKT48")
console.log (oshi)


console.log (oshi.length)


console.log ("\n Oshi JKT48 \n")

for (a = 0; a < oshi.length; a++) {
    console.log (oshi [a])
}

     
console.log ("\n --- batas --- \n")




console.log ("\n Dictionary \n")

var data = {
     "nama" : "Habib muzakki piliang",
     "asal" : "Bukitinggi",
     "tinggal" : "Kota Serang",
     "nomor" : 12,
     "tinggi" : 172,
     "berat" :  50,
}

console.log ("Nama :", data ["nama"])

console.log ("Asal :", data ["asal"])

console.log ("Tempat tinggal :", data ["tinggal"])

console.log ("Nomor :", data ["nomor"])

console.log ("Tinggi badan :", data ["tinggi"])

console.log ("Berat badan :", data ["berat"])


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dasar \n")

function dasar () {
    console.log ("Halo Dunia")
}

dasar ()


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dasar 2 \n")

function der () {
    console.log ("Hello Jakarta")
    console.log ("Hello Bogor")
    console.log ("Hello Bandung")
}

der ()


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Parameter 1 \n")

function den (nama, kelas, asal) {
    console.log (`Halo, saya ${nama}, dari kelas ${kelas}, dan asal dari ${asal}`)
}

den ("Habib", "12 Agama", "Bukitinggi")
den ("Gema", "12 Agama", "Petir Serang")
den ("Rayyan", "11 IPA 4", "Tangerang")
den ("Fayyan", "12 IPA 5", "Jakarta Barat")


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Parameter 2 \n")

function untuk (nama, tempat, suku) {
    console.log (`Halo saya ${nama} dari ${tempat} dan dari suku ${suku}`)
}

untuk ("Habib", "Jakarta", "Piliang")
untuk ("Hayyan", "Serang", "Jawa")
untuk ("Daffa", "Banten", "Sunda")
untuk ("Rayyan", "Semarang", "Jawa")


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Return \n")

function tambah (a, b) {
     return a + b
}

hasil = tambah (10, 10)
console.log (hasil)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Return 1 \n")


function ral (nama) {
    return `Halo saya ${nama} dari Jakarta Utara`
} 

hasil = ral ("Rutter")
console.log (hasil)


console.log ("\n --- batas --- \n")




console.log ("\n Error Handling \n")

try {
    hasil = 10 / an
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- batas --- \n")




console.log ("\n Error Handling 2 \n")

try {
    var hasil = 10 / nm 
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- batas --- \n")




console.log ("\n Error Handling 3 \n")

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


console.log ("\n --- batas --- \n")




console.log ("\n Percabangan Error Handling \n")

var a = -5

try {
    if (a < 0) {
        throw ("Gagal")
    }
    
    if (a > 5) {
        console.log ("Hasil lebih besar")
    }
    
    else {
        console.log ("Hasil lebih kecil")
    }
}

catch (Error) {
    console.log (`Gak boleh minus, angka = ${a}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi Percabangan Error Handling \n")

function error (b) {
    try {
        if (b < 0) {
            throw ("Gagal")
        }
        
        if (b > 5) {
            console.log (`Hasil lebih besar, angka = ${b}`)
        }
        
        else {
            console.log (`Hasil lebih kecil, angka = ${b}`)
        }
    }
    
    catch (Error) {
        console.log (`Gak boleh minus, angka = ${b}`)
    }
}

error (10)
error (-5)
error (4)
error (-10)
error (8)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi Percabangan Error Handling 2 \n")

function tes (c) {
    try {
        if (c < 0) {
            throw ("Gagal")
        }
        
        if (c > 5) {
            console.log (`Hasil lebih besar, angka = ${c}`)
        }
        
        else {
            console.log (`Hasil lebih kecil, angka = ${c}`)
        }
    }
    
    catch (Error) {
        console.log (`Gak boleh minus, angka = ${c}`)
    }
}

tes (-10)
tes (3)
tes (8)
tes (2)
tes (-8)


console.log ("\n --- batas --- \n")
