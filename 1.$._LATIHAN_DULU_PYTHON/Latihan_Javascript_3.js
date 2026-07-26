console.log ("Hello World")



console.log ("\n --- batas --- \n")




console.log ("\n Variabel dasar \n")

var teks_1 = "Hello World"
console.log (teks_1)


var angka_1 = 12
console.log (angka_1)


var desimal_1 = 12.12
console.log (desimal_1)


console.log ("\n --- batas --- \n")




console.log ("\n F String \n")

var nama = "Habib Muzakki"
var asal = "Kota Serang, Banten"
var jurusan = "D4 Vokasi Teknik Informatika"
var kuliah = "Universitas Harkat Negeri Tegal"
var coding = "HTML, CSS, JavaScript dan Python"
var lomba = "Finalis OSN-K Informatika 2025"
var alumni = "MAN 2 KOTA SERANG (Kelas Agama)"
var bidang = "Web Developer dan Python"


profil = `
- Nama lengkap : ${nama}
- Asal daerah  : ${asal}
- Jurusan      : ${jurusan}
- Kuliah       : ${kuliah}
- Coding       : ${coding}
- Lomba        : ${lomba}
- Alumni       : ${alumni}
- Bidang       : ${bidang}
`

console.log (profil)


console.log ("\n --- batas --- \n")





console.log ("\n Operator dasar \n")

function tambah (x, y) {
    return x + y
}


function kurang (x, y) {
    return x - y
}


function kali (x, y) {
    return x * y
}


function pangkat (x, y) {
    return x ** y
}


hasil_a = tambah (10, 10)
hasil_b = kurang (15, 10)
hasil_c = kali (10, 10)
hasil_d = pangkat (10, 3)


var hitung = `
- Tambah  = ${hasil_a}
- Kurang  = ${hasil_b}
- Kali    = ${hasil_c}
- Pangkat = ${hasil_d}
`

console.log (hitung)


console.log ("\n --- batas --- \n")




console.log ("\n Operasi Perbandingan \n")

var x = 10
var y = 5


var banding = `
- Hasil = ${x > y}
- Hasil = ${x < y}
- Hasil = ${x >= y}
`

console.log (banding)


console.log ("\n --- batas --- \n")




console.log ("\n Operasi Logika \n")

var logic = `
- Hasil = ${x > y && x < y}
- Hasil = ${x < y || x > y}
- Hasil = ${! (x > y)}
- Hasil = ${! (x < y)}
`

console.log (logic)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Dasar \n")

function dasar (l) {

    if (l >= 5) {
        console.log (`Besar, angka l = ${l}`)
    }

    else {
        console.log (`Kecil, angka l = ${l}`)
    }
}

dasar (10)
dasar (7)
dasar (6)
dasar (5)
dasar (3)
dasar (2)
dasar (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function run (w) {

    if (w >= 8) {
        console.log (`Besar, angka w = ${w}`)
    }

    else if (w >= 5) {
        console.log (`Tengah, angka w = ${w}`)
    }

    else {
        console.log (`Kecil, angka w = ${w}`)
    }
}

run (10)
run (9)
run (8)
run (5)
run (4)
run (3)
run (2)
run (1)


console.log ("\n --- batas --- \n")




console.log ("\n Error Handling \n")
try {
    var b = 10 / a
    console.log (b)
}

catch (Error) {
    console.log (`Gagal`)
}

finally {
    console.log (`Selesai`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Error Handling \n")

try {
    var n = 10 + 10
    console.log (n)
}

catch (Error) {
    console.log (`Gagal`)
}

finally {
    console.log (`Selesai`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Raise Error Handling \n")

function dun (k) {

    try {

        if (k < 0) {
            throw ("Minus")
        }

        if (k >= 8) {
            console.log (`Besar, angka k = ${k}`)
        }

        else if (k >= 5) {
            console.log (`Tengah, angka k = ${k}`)
        }

        else {
            console.log (`Kecil, angka k = ${k}`)
        }
    }

    catch (Error) {
        console.log (`Angka minus, angka k = ${k}`)
    }
}

dun (-10)
dun (-8)
dun (-4)
dun (10)
dun (9)
dun (7)
dun (5)
dun (4)
dun (2)
dun (1)


console.log ("\n --- batas --- \n")




console.log ("\n For dasar \n")

for (a = 0; a < 11; a++) {
    console.log (`Urutan ke ${a}`)
}


console.log ("\n --- batas --- \n")




for (b = 1; b < 11; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- batas --- \n")




for (c = 5; c < 11; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- batas --- \n")



console.log ("\n While dasar \n")

a = 1

while (a < 11) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- batas --- \n")




console.log ("\n While dasar 2 \n")

b = 10

while (b > 0) {
    console.log (`Urutan ke - ${b}`)
    b--
}


console.log ("\n --- batas --- \n")




console.log ("\n Do While dasar \n")

a = 1

do {
    console.log (`Urutan ke - ${a}`)
    a++
}

while (a < 11)


console.log ("\n --- batas --- \n")



console.log ("\n For Nested \n")

for (a = 1; a < 5; a++) {
    for (b = 1; b < 5; b++) {
        console.log (`Luar : ${a} dan Dalam : ${b}`)
    }
}


console.log ("\n --- batas --- \n")




console.log ("\n For Nested 2 \n")

for (x = 1; x < 4; x++) {
    for (y = 1; y < 4; y++) {
        for (z = 1; z < 4; z++) {
            console.log (`x : ${x}, y : ${y}, z : ${z}`)
        }
    }
}


console.log ("\n --- batas --- \n") 