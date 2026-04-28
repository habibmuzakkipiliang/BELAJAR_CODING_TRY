// JavaScript Task

console.log ("Hello World")


console.log ("\n --- Batas --- \n")



console.log ("\n Variabel dan Tipe data pemrograman \n")


var nama = "Tes 1"
var angka = 34
var desimal = 44.23
var huruf = 'A'
var cek = true
var daftar = [
    
    "1. Mobil",
    "2. Motor", 
    "3. Kereta Api",
    "4. Bajai",
    
    ]


detail = `

- Nama    : ${nama}
- Angka   : ${angka}
- Desimal : ${desimal}
- Huruf   : ${huruf}
- Cek     : ${cek}
- Daftar  : 

`

console.log (detail)


for (a = 0; a < daftar.length; a++) {
    console.log (daftar [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")


var data = {
    "nama" : "Alan John",
    "asal" : "Amerika Serikat",
    "kerja" : "Software Engineer",
    "coding" : "HTML, CSS, JavaScript dan Python",
    
}


console.log ("Nama :", data ["nama"])

console.log ("Asal :", data ["asal"])

console.log ("Kerja :", data ["kerja"])

console.log ("Coding :", data ["coding"])


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Dasar \n")


var x = 20
var y = 5


console.log ("Tambah =", x + y)
console.log ("Kurang =", x - y)
console.log ("Kali =", x * y)
console.log ("Pangkat =", x ** y)
console.log ("Bagi =", x / y)
console.log ("Modulus =", x % y)


console.log ("\n --- Batas --- \n")





console.log ("\n Operator Perbandingan \n")


console.log ("Hasil =", x > y)
console.log ("Hasil =", x < y)
console.log ("Hasil =", x >= y)
console.log ("Hasil =", x <= y)
console.log ("Hasil =", x == y)
console.log ("Hasil =", x != y)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Logika \n")


console.log ("Hasil =", (x > y) && (x < y))
console.log ("Hasil =", (x < y) || (x > y))
console.log ("Hasil =", (! x))
console.log ("Hasil =", (! y))


console.log ("\n --- Batas --- \n")





console.log ("\n Percabangan Dasar \n")


var a = 9

if (a > 5) {
    console.log (`Besar, a = ${a}`)
}

else {
    console.log (`Kecil, a = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Dasar 1 \n")


var b = 3

if (b > 5) {
    console.log (`Besar, b = ${b}`)
}

else {
    console.log (`Kecil, b = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan 1 \n")


var c = 9

if (c > 5) {
    console.log (`Besar, c = ${c}`)
}

else if (c < 5) {
    console.log (`Kecil, c = ${c}`)
}

else {
    console.log (`Sama saja,  c = ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan 2 \n")


var d = 3 

if (d > 5) {
    console.log (`Besar, d = ${d}`)
}

else if (d < 5) {
    console.log (`Kecil, d = ${d}`)
}

else {
    console.log (`Sama saja, d = ${d}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 \n")


var skor = 9
var cek = true

if (cek) {
    if (skor > 5) {
        console.log (`Besar, skor = ${skor}`)
    }
    
    else if (skor < 5) {
        console.log (`Kecil, skor = ${skor}`)
    }
}

else {
    console.log (`Sama saja, skor = ${skor}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 2 \n")


var skor = 3
var cek = true

if (cek) {
    if (skor > 5) {
        console.log (`Besar, skor = ${skor}`)
    }
    
    else {
        console.log (`Kecil, skor = ${skor}`)
    }
}


else {
    console.log (`Sama saja, skor = ${skor}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia daftar JKT48 \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 13) && (usia <= 17)) {
        console.log (`Boleh daftar jkt48, usia = ${usia}`)
    }
    
    else if (usia > 17) {
        console.log (`Sudah lebih dari cukup, usia = ${usia}`)
    }
    
    else {
        console.log (`Masih belum cukup umur, usia = ${usia}`)
    }
}

else {
    console.log (`Di lain waktu daftarnya, usia = {usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia produktif manusia \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Sudah masuk usia produktif, usia = ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah lanjut usia, usia = ${usia}`)
    }
    
    else {
        console.log (`Masih dibawah usia produktif, usia = ${usia}`)
    }
}

else {
    console.log (`Usianya masih kecil, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar \n")


for (a = 0; a < 11; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 1 \n")


for (b = 0; b < 21; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 1 \n")


var a = 10

while (a < 21) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 2 \n")


var b = 15

while (b < 26) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 3 \n")


var c = 20

while (c < 31) {
    console.log (`Urutan ke - ${c}`)
    c++
}


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 1 \n")


var a = 10

do {
    console.log (`Urutan ke - ${a}`)
    a++
} while (a < 16)


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 2 \n")


var b = 15

do {
    console.log (`Urutan ke - ${b}`)
    b++
} while (b < 26)



console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 3 \n")


var c = 10

do {
    console.log (`Urutan ke - ${c}`)
    c++
} while (c < 26)


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested \n")


for (a = 0; a < 5; a++) {
    for (b = 0; b < 5; b++) {
        for (c = 0; c < 5; c++) {
            console.log (`Urutan ke - ${a}, urutan ke - ${b}, urutan ke - ${c}`)
        }
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 1 \n")


for (x = 0; x < 5; x++) {
    for (y = 0; y < 5; y++) {
        for (z = 0; z < 5; z++) {
            console.log (`Urutan ke - ${x}, urutan ke - ${y}, urutan ke - ${z}`)
        }
    }
}


console.log ("\n --- Batas --- \n")
