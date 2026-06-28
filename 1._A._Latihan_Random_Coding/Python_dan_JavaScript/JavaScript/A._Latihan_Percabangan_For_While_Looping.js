console.log ("\n Profil Habib Muzakki Piliang \n")


var nama = "Habib Muzakki"
var panggil = "Habib"
var marga = "Piliang"
var suku = "Minangkabau"
var coding = "HTML, CSS, JavaScript dan Python"
var lomba = "Finalis OSN-K Informatika tahun 2025"
var alumni = "MAN 2 KOTA SERANG (tahun 2026)"
var kelas = "12 Agama (tahun 2026)"
var tinggi = "170 cm"
var berat = "60 kg"
var darah = "B"
var fans = "JKT48"
var oshi = "Michie, Gracie, Fritzy, Anindya, Christy, Freya, Fiony JKT48"


var profil = `

- Nama lengkap   : ${nama}
- Nama panggilan : ${panggil}
- Marga          : ${marga}
- Suku           : ${suku}
- Coding         : ${coding}
- Lomba          : ${lomba}
- Alumni         : ${alumni}
- Kelas          : ${kelas}
- Tinggi badan   : ${tinggi}
- Berat badan    : ${berat}
- Golongan darah : ${darah}
- Fans           : ${fans}
- Oshi JKT48     : ${oshi}

`


console.log (profil)


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe data pemrograman \n")


var teks = "Halo Guys"
var angka = 23
var desimal = 45.2
var cek = true
var kosong = null
var huruf = 'A'


var ner = `

- Teks    = ${teks}
- Angka   = ${angka}
- Desimal = ${desimal}
- Cek     = ${cek}
- Kosong  = ${kosong}
- Huruf   = ${huruf}

`

console.log (ner)


console.log ("\n --- Batas --- \n")




console.log ("\n Array \n")

var array = [
    
    "1. Michie",
    "2. Fritzy",
    "3. Anindya",
    "4. Christy",
    "5. Freya",
    
    ]
    
    
for (a = 0; a < array.length; a++) {
    console.log (array [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")


var data = {
    "nama" : "John Doe",
    "kelas" : "Menengah",
    "asal" : "Amerika Serikat",
    "coding" : "HTML, CSS, JavaScript dan Python"
}


console.log ("Nama :", data ["nama"])

console.log ("Kelas :", data ["nama"])

console.log ("Asal :", data ["asal"])

console.log ("Coding :", data ["coding"])


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case \n")


var hari = "Senin"

switch (hari) {
    
    case "Senin":
        console.log ("Senin")
        break
        
    case "Selasa":
        console.log ("Selasa")
        break
        
    case "Rabu":
        console.log ("Rabu")
        break
        
    case "Kamis":
        console.log ("Kamis")
        break
        
    case "Jumat":
        console.log ("Jumat")
        break
        
    default:
    console.log ("Libur")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 2 \n")


var kondisi = 2

switch (kondisi) {
    
    case 1:
        console.log ("Yes")
        break
        
    case 2:
        console.log ("Tidak")
        break
        
    case 3:
        console.log ("Kadang-kadang")
        
    default:
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Dasar \n")


a = 9

if (a > 5) {
    console.log (`Besar, a = ${a}`)
}

else {
    console.log (`Kecil, a = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan \n")


var b = 8

if (b > 5) {
    console.log (`Besar, b = ${b}`)
}

else if (b < 5) {
    console.log (`Kecil, b = ${b}`)
}

else {
    console.log (`Sama saja, b = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Ledder \n")


var nilai = 100

if (nilai >= 90) {
    console.log (`A, nilai = ${nilai}`)
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

else if (nilai >= 40) {
    console.log (`F, nilai = ${nilai}`)
}

else if (nilai >= 30) {
    console.log (`G, nilai = ${nilai}`)
}

else {
    console.log (`Semula, nilai = ${nilai}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 \n")


var a = 9
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


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 2 \n")


var b = 4
var cek = true

if (cek) {
    if (b > 5) {
        console.log (`Besar, b = ${b}`)
    }
    
    else if (b < 5) {
        console.log (`Kecil, b = ${b}`)
    }
}

else {
    console.log (`Sama saja, b = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 3 \n")


var c = 10
var cek = true

if (cek) {
    if (c > 5) {
        console.log (`Besar, c = ${c}`)
    }
    
    else if (c < 5) {
        console.log (`Kecil, c = ${c}`)
    }
}

else {
    console.log (`Sama saja, c = ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 4 \n")


var d = 3
var cek = true

if (cek) {
    if (d > 5) {
        console.log (`Besar d = ${d}`)
    }
    
    else if (d < 5) {
        console.log (`Kecil, d = ${d}`)
    }
}

else {
    console.log (`Sama saja, d = ${d}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 5 \n")


var e = 10
var cek = true

if (cek) {
    if (e > 5) {
        console.log (`Besar, e = ${e}`)
    }
    
    else {
        console.log (`Kecil, e = ${e}`)
    }
}

else {
    console.log (`Sama saja, e = ${e}`)
}



console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 6 \n")


var f = 3
var cek = true

if (cek) {
    if (f > 5) {
        console.log (`Besar, f = ${f}`)
    }
    
    else {
        console.log (`Kecil, f = ${f}`)
    }
}

else {
    console.log (`Sama saja, f = ${f}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 7 \n")


var g = 10
var cek = true

if (cek) {
    if (g > 5) {
        console.log (`Besarz g = ${g}`)
    }
    
    else {
        console.log (`Kecil, g = ${g}`)
    }
}

else {
    console.log (`Sama saja, g = ${g}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, Join ke JKT48 \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 13) && (usia <= 17)) {
        console.log (`Bisa join JKT48 dan ikut audisi JKT48, usia = ${usia}`)
    }
    
    else if (usia > 17) {
        console.log (`Sudah lebih dari cukup, usia = ${usia}`)
    }
    
    else {
        console.log (`Masih dibawah umur, usia = ${usia}`)
    }
}

else {
    console.log (`Daftar di lain waktu, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia produktif manusia \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Sudah masuk usia produktif manusia, usia = ${usia}`)
    }
    
    
    else if (usia > 64) {
        console.log (`Sudah lanjut usia, usia = ${usia}`)
    }
    
    
    else {
        console.log (`Masih belum usia produktif, usia = ${usia}`)
    }
}

else {
    console.log (`Usianya masih kecil, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 1 \n")


for (a = 0; a < 11; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 2 \n")


for (b = 0; b < 11; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 3 \n")


for (c = 0; c < 11; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")



console.log ("\n For dasar 4 \n")


for (d = 0; d < 11; d++) {
    console.log (`Urutan ke - ${d}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 5 \n")


for (e = 0; e < 11; e++) {
    console.log (`Urutan ke - ${e}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 1 \n")


var a = 5

while (a < 20) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 2 \n")


var b = 10

while (b < 20) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 3 \n")


var c = 20

while (c < 30) {
    console.log (`Urutan ke - ${c}`)
    c++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 4 \n")


var d = 25

while (d < 35) {
    console.log (`Urutan ke - ${d}`)
    d++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 5 \n")


var e = 15

while (e < 30) {
    console.log (`Urutan ke - ${e}`)
    e++
}


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 1 \n")


var a = 10

do {
    console.log (`Urutan ke - ${a}`)
    a++
} 

while (a < 20)



console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 2 \n")


var b = 20


do {
    console.log (`Urutan ke - ${b}`)
    b++
}

while (b < 30)


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 3 \n")


var c = 5

do {
    console.log (`Urutan ke - ${c}`)
    c++
}

while (c < 10)


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 4 \n")


var d = 10

do {
    console.log (`Urutan ke - ${d}`)
    d++
}

while (d < 20)


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 5 \n")


var e = 25

do {
    console.log (`Urutan ke - ${e}`)
    e++
}

while (e < 40)


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 1 \n")


for (a = 0; a < 4; a++) {
    for (b = 0; b < 4; b++) {
        for (c = 0; c < 4; c++) {
            for (d = 0; d < 4; d++) {
                for (e = 0; e < 4; e++) {
                   console.log (`Urutan ke - ${a}, urutan ke - ${b}, urutan ke - ${c}, urutan ke - ${d}, urutan ke - ${e}`) 
                }
            }
        }
    } 
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 2 \n")


for (x = 0; x < 4; x++) {
    for (y = 0; x < 4; x++) {
        for (z = 0; z < 4; z++) {
            for (t = 0; t < 4; t++) {
                for (s = 0; s < 4; s++) {
                    console.log (`Urutan ke - ${x}, urutan ke - ${y}, urutan ke - ${z}, urutan ke - ${t}, urutan ke - ${s}`)
                }
            }
        }
    }
}


console.log ("\n --- Batas --- \n")
