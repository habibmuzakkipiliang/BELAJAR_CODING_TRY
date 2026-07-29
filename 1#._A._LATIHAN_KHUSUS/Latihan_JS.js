// Tipe data pemrograman

var teks = "Halo Dunia"
var angka = 12
var desimal = 1.12
var cek = true
var kosong = null

var tipe = `
- Teks : ${teks}
- Angka : ${angka}
- Desimal : ${desimal}
- Cek : ${cek}
- Kosong : ${kosong}
`

console.log (tipe)


console.log ("\n --- batas --- \n")



// Cek tipe data 

var teks = "Halo Dunia"
var angka = 12
var desimal = 1.12
var cek = true
var kosong = null

var cek_tipe = `
- Teks : ${typeof (teks)}
- Angka : ${typeof (angka)}
- Desimal : ${typeof (desimal)}
- Cek : ${typeof (cek)}
- Kosong : ${typeof (kosong)}
`

console.log (cek_tipe)


console.log ("\n --- batas --- \n")





// Bikin latihan JS

var r = 9
var u = 5

var hasil = r * u
console.log (`Total = ${hasil}`)


console.log ("\n --- batas --- \n")



// latihan pake Fungsi

var x = 9
var y = 6

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

console.log ("Hasil tambah =", tambah (x, y))
console.log ("Hasil kurang =", kurang (x, y))
console.log ("Hasil kali =", kali (x, y))
console.log ("Hasil pangkat =", pangkat (x, y))


console.log ("\n --- batas --- \n")



// Latihan bikin nama + percabangan dasar

var nama = "Habib"

if (nama == "Habib") {
     console.log ("Nama kamu Habib")
}

else {
     console.log ("Bukan Habib")
}


console.log ("\n --- batas --- \n")



// Latiha bikin nama pake fungsi

var nama_1 = "Habib"

function cek_nama (nama) {

     if (nama == "Habib") {
          console.log ("Nama kamu Habib")
     }

     else {
          console.log ("Bukan Habib")
     }
}

cek_nama (nama_1)
cek_nama (nama_1)
cek_nama (nama_1)
cek_nama (nama_1)
cek_nama (nama_1)


console.log ("\n --- batas --- \n")




// Fungsi dengan mencari angka terbesar

function angka_terbesar (k, l) {
     
     if (k > l) {
          return k
     }
     
     else {
          return l
     }
}

console.log ("Angka besar =", angka_terbesar (10, 9))
console.log ("Angka besar =", angka_terbesar (9, 12))
console.log ("Angka besar =", angka_terbesar (3, 90))
console.log ("Angka besar =", angka_terbesar (6, 34))


console.log ("\n --- batas --- \n")



// Fungsi dengan mencari angka terkecil

function angka_terkecil (x, y) {

     if (x < y) {
          return x 
     }

     else {
          return y
     }
}

console.log ("Angka terkecil =", angka_terkecil (10, 9))
console.log ("Angka terkecil =", angka_terkecil (4, 13))
console.log ("Angka terkecil =", angka_terkecil (8, 12))
console.log ("Angka terkecil =", angka_terkecil (9, 12))
console.log ("Angka terkecil =", angka_terkecil (3, 19))


console.log ("\n --- batas --- \n")




// Fungsi dengan angka terkecil 

function angka_terkecil (a, b) {

     if (a < b) {
          return a
     }

     else {
          return b
     }
}

console.log ("Angka terkecil =", angka_terkecil (10, 8))
console.log ("Angka terkecil =", angka_terkecil (10, 3))
console.log ("Angka terkecil =", angka_terkecil (3, 90))
console.log ("Angka terkecil =", angka_terkecil (6, 99))


console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan dasar

function dasar (a) {

     if (a >= 5) {
          console.log (`Besar, angka a = ${a}`)
     }

     else {
          console.log (`Kecil, angka a = ${a}`)
     }
}

dasar (10)
dasar (9)
dasar (8)
dasar (7)
dasar (6)
dasar (5)
dasar (4)
dasar (3)
dasar (2)
dasar (1)


console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan lanjutan 

function percabangan_1 (b) {

     if (b >= 8) {
          console.log (`Besar, angka b = ${b}`)
     }

     else if (b >= 5) {
          console.log (`Tengah, angka b = ${b}`)
     }

     else {
          console.log (`Kecil, angka b = ${b}`)
     }
}

percabangan_1 (10)
percabangan_1 (9)
percabangan_1 (8)
percabangan_1 (7)
percabangan_1 (6)
percabangan_1 (5)


console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan lanjutan 

function nested (j) {

     cek = true

     if (j >= 5) {
          if (cek) {
               console.log (`Besar, angka j = ${j}`)
          }

          else {
               console.log (`Tengah, angka j = ${j}`)
          }
     }

     else {
          console.log (`Kecil, angka j = ${j}`)
     }
}

nested (10)
nested (9)
nested (8)
nested (7)
nested (6)
nested (5)
nested (4)


console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan usia produktif manusia

function fer (f) {

     if (f >= 15 && f <= 40) {
          console.log (`usia yang sudah produktif, usia = ${f}`)
     }

     else if (f > 40) {
          console.log (`usia yang sudah lanjut, usia = ${f}`)
     }

     else {
          console.log (`masih kecil umurnya, usia = ${f}`)
     }
}

fer (10)
fer (9)
fer (8)
fer (7)
fer (6)
fer (5)
fer (4)
fer (3)
fer (2)
fer (1)


console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan usia produktif manusia

function usia (f) {

     if (f >= 15 && f <= 40) {
          console.log (`sudah masuk usia produktif, usia = ${f}`)
     }

     else if (f > 40) {
          console.log (`sudah tua, usia = ${f}`)
     }

     else {
          console.log (`masih kecil, usia = ${f}`)
     }
}

usia (60)
usia (50)
usia (40)
usia (30)
usia (20)
usia (10)
usia (5)


console.log ("\n --- batas --- \n")




// Fungsi dengan usia masuk jkt48

function oshi (f) {

     if (f >= 13 && f < 19) {
          console.log (`sudah boleh masuk jkt48, usia = ${f}`)
     }

     else if (f > 19) {
          console.log (`sudah lebih dari cukup, usia = ${f}`)
     }

     else {
          console.log (`masih kecil, usia = ${f}`)
     }
}

oshi (10)
oshi (9)
oshi (8)
oshi (7)
oshi (6)
oshi (5)
oshi (4)
oshi (3)
oshi (2)
oshi (1)


console.log ("\n --- batas --- \n")



// For dasar 1

for (a = 0; a < 11; a++) {
     console.log (`urutan ke - ${a}`)
}

console.log ("\n --- batas --- \n")



// For dasar 2

for (b = 1; b < 11; b++) {
     console.log (`urutan ke - ${b}`)
}

console.log ("\n --- batas --- \n")



// for dasar 3

for (h = 0; h < 15; h++) {
     console.log (`urutan ke - ${h}`)
}

console.log ("\n --- batas --- \n")



// For dasar 

for (g = 0; g < 11; g++) {
     console.log (`urutan ke - ${g}`)
}


console.log ("\n --- batas --- \n")



// While dasar

var a = 1

while (a < 11) {
     console.log (`urutan ke - ${a}`)
     a++
}

console.log ("\n --- batas --- \n")




// While dasar 1

b = 10

while (b > 0) {
     console.log (`urutan ke - ${b}`)
     b--
}


console.log ("\n --- batas --- \n")



// Do While dasar

var b = 1

do {
     console.log (`urutan ke - ${b}`)
     b++
}

while (b < 11)


console.log ("\n --- batas --- \n")




// While dasar

f = 15

while (f > 0) {
     console.log (`urutan ke - ${f}`)
     f--
}

console.log ("\n --- batas --- \n")