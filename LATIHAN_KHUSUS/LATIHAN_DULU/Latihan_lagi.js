// Bikin hello world

console.log ("Hello World")


console.log ("\n --- batas --- \n")




// Variabel dasar

var contoh = "Hello World"
console.log ("Contoh =", contoh)

console.log ("\n --- batas --- \n")


var contoh_2 = 12
console.log ("Contoh 2 =", contoh_2)


console.log ("\n --- batas --- \n")


var contoh_3 = 2.21
console.log ("Contoh =", contoh_3)


console.log ("\n --- batas --- \n")



// Tipe data pemrograman

var teks = "tipe string"
var angka = 12
var desimal = 2.12
var cek = true
var kosong = null

var tipe = `
- Teks    : ${teks}
- Angka   : ${angka}
- Desimal : ${desimal}
- Cek     : ${cek}
- Kosong  : ${kosong}
`

console.log (tipe)

console.log ("\n --- batas --- \n")




// Cek Tipe Pemrograman Dasar

var teks = "tipe string"
var angka = 12
var desimal = 2.12
var cek = true
var kosong = null

var cek_tipe = `
- Teks    : ${typeof (teks)}
- Angkla  : ${typeof (angka)}
- Desimal : ${typeof (desimal)}
- Cek     : ${typeof (cek)}
- Kosong  : ${typeof (kosong)}
`

console.log (cek_tipe)


console.log ("\n --- batas --- \n")



// profil Habib Muzakki

var nama = "Habib Muzakki"
var asal = "Kota Serang, Banten"
var alumni = "MAN 2 Kota Serang"
var cek = true
var coding = "HTML, CSS, JavaScript dan Python"
var kuliah = "Harkat Negeri Tegal"

var profil = `
- Nama   : ${nama}
- Asal   : ${asal}
- Alumni : ${alumni}
- Cek    : ${cek}
- Coding : ${coding}
- Kuliah : ${kuliah}
`

console.log (profil)


console.log ("\n --- batas --- \n")



// Switch Case

function der (w) {

     switch (w) {

          case 1:
               console.log ("Angka 1")
               break

          case 2:
               console.log ("Angka 2")
               break

          case 3:
               console.log ("Angka 3")
               break

          case 4:
               console.log ("Angka 4")
               break

          default:
               console.log ("Angka lain")
     }
}

der (1)
der (2)
der (3)
der (4)
der (5)


console.log ("\n --- batas --- \n")



// Percabangan dasar

var a = 10

if (a >= 5) {
     console.log (`Angka a besar, angka a = ${a}`)
}

else {
     console.log (`Angka a kecil, angka a = ${a}`)
}


console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan dasar

function dasar (a) {

     if (a >= 5) {
          console.log (`Angka a besar, angka a = ${a}`)
     }

     else {
          console.log (`Angka a kecil, angka a = ${a}`)
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



// Percabangan lanjutan 1, studi kasus angka positif

var angka = 12

if (angka > 0) {
     console.log (`Angka positif, angka = ${angka}`)
}

else if (angka < 0) {
     console.log (`Angka minus, angka = ${angka}`)
}

else {
     console.log (`Angka nol, angka = ${angka}`)
}


console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan lanjutan, studi kasus angka positif

function angka_1 (c) {

     if (angka_1 > 0) {
          console.log (`Angka positif, angka = ${angka}`)
     }

     else if (angka_1 < 0) {
          console.log (`Angka negatif, angka = ${angka}`)
     }

     else {
          console.log (`Angka nol, angka = ${angka}`)
     }
}

angka_1  (10)
angka_1  (-10)
angka_1 (-3)
angka_1 (-12)
angka_1 (10)
angka_1 (34)
angka_1 (12)
angka_1 (-23)
angka_1 (-45)


console.log ("\n --- batas --- \n")





// Fungsi dengan percabangan nilai skor

function rapor (k) {

     if (k >= 95) {
          console.log (`A, nilai = ${k}`)
     }

     else if (k >= 90) {
          console.log (`B, nilai = ${k}`)
     }

     else if (k >= 80) {
          console.log (`C, nilai = ${k}`)
     }

     else if (k >= 75) {
          console.log (`D, nilai = ${k}`)
     }

     else if (k >= 70) {
          console.log (`E, nilai = ${k}`)
     }

     else if (k >= 60) {
          console.log (`F, nilai = ${k}`)
     }

     else if (k >= 50) {
          console.log (`Nikai setengah jelek, nilai = ${k}`)
     }

     else {
          console.log (`Jelek banget, nilai = ${k}`)
     }
}

rapor (100)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (40)
rapor (30)
rapor (20)
rapor (10)


console.log ("\n --- batas --- \n")




// Fungsi dengan Percabangan Nested

function nested (j) {

     cek = true

     if (j >= 5) {
          if (cek) {
               console.log (`Angka j besar, angka j = ${j}`)
          }

          else {
               console.log (`Angka j kecil, angka j = ${j}`)
          }
     }

     else {
          console.log (`Angka kecil, angka j = ${j}`)
     }
} 

nested (10)
nested (9)
nested (8)
nested (7)
nested (6)
nested (5)
nested (4)
nested (2)
nested (1)


console.log ("\n --- batas --- \n")




// Error Handling Raise Exception

function tes (f) {

     try {

          if (f < 0) {
               throw new ("Angka minus")
          }

          if (f >= 5) {
               console.log (`Angka f besar, angka f = ${f}`)
          }

          else {
               console.log (`Angka f kecil, angka f = ${f}`)
          }
     }

     catch (Error) {
          console.log (`Angka minus, angka f = ${f}`)
     }
}

tes (-10)
tes (-44)
tes (10)
tes (9)
tes (8)
tes (7)
tes (6)
tes (5)
tes (4)
tes (3)
tes (2)
tes (1)


console.log ("\n --- batas --- \n")



// Error Handling Percabangan Lanjutan Raise Exception

function lank (i) {

     try {
          
          if (i < 0) {
               throw new ("Angka minus")
          }

          if (i >= 8) {
               console.log (`Angka i besar, angka i = ${i}`)
          }

          else if (i >= 5) {
               console.log (`Angka i tengah, angka i = ${i}`)
          }

          else {
               console.log (`Angka i kecil, angka i = ${i}`)
          }
     }

     catch (Error) {
          console.log (`Angka minus, angka i = ${i}`)
     }
}

lank (-10)
lank (-4)
lank (-5)
lank (-9)
lank (10)
lank (9)
lank (8)
lank (7)
lank (6)
lank (5)
lank (4)
lank (3)
lank (2)
lank (1)


console.log ("\n --- batas --- \n")




// Error Handling 

try {
     var a =  an / 0
     console.log (a)
}

catch (Error) {
     console.log ("Angka yang salah")
}

finally {
     console.log ("Selesai")
}


console.log ("\n --- batas --- \n")



// Error Handling 2

try {
     var b = rt / 0
     console.log (b)
}

catch (Error) {
     console.log ("Angka yang salah")
}

finally {
     console.log ("Selesai")
}


console.log ("\n --- batas --- \n")



// Error Handling 

try {
     var h = 10 + 10
     console.log (h)
}

catch (Error) {
     console.log ("Angka yang salah")
}

finally {
     console.log ("Selesai")
}


console.log ("\n --- batas --- \n")



// For dasar

for (j = 0; j < 11; j++) {
     console.log (`urutan ke - ${j}`)
}

console.log ("\n --- batas --- \n")



// For dasar 2

for (h = 0; h < 16; h++) {
     console.log (`urutan ke - ${h}`)
}

console.log ("\n --- batas --- \n")



// For dasar 3

for (d = 1; d < 21; d++) {
     console.log (`urutan ke - ${d}`)
}


console.log ("\n --- batas --- \n")



// For dasar 

for (r = 1; r < 21; r++) {
     console.log (`Urutan ke - ${r}`)
}

console.log ("\n --- batas --- \n")



// While dasar

a = 1

while (a < 11) {
     console.log (`urutan ke - ${a}`)
     a++
}

console.log ("\n --- batas --- \n")




// While dasar

b = 20

while (b > 0) {
     console.log (`urutan ke - ${b}`)
     b--
}

console.log ("\n --- batas --- \n")




// For Nested

for (x = 1; x < 11; x++) {
     for (y = 1; y < 11; y++) {
          for (z = 1; z < 11; z++) {
               console.log (`x : ${x}, y : ${y}, z : ${z} `)
          }
     }
}


console.log ("\n --- batas --- \n")



// Do While dasar

var h = 1

do {
     console.log (`urutan ke - ${h}`)
     h++
}

while (h < 11)


console.log ("\n --- batas --- \n")




// Dictionary 

var data = {
     "nama" : "Habib Muzakki",
     "asal" : "Kota Serang", 
     "coding" : "HTML, CSS, JavaScript, Python"
}

for (var j in data) {
     console.log (`${j} : ${data [j]}`)
}


console.log ("\n --- batas --- \n")




// Arrow Fungsi 

var burst = () => {
     console.log ("Hello World")
}

burst ()


console.log ("\n --- batas --- \n")



// Arrow fungsi

var gun = () => {
     console.log ("Hello World")
     console.log ("Hello Guys")
     console.log ("Hello Bang")
     console.log ("Hello Gun")
}

gun ()


console.log ("\n --- batas --- \n")



// Arrow Fungsi dengan parameter

var fun = (nama) => {
     console.log (`Halo saya ${nama} dari Jakarta Timur`)
}

fun ("Rayyan")
fun ("Fayyan")
fun ("Hujjan")
fun ("Gunner")


console.log ("\n --- batas --- \n")



// Arrow fungsi parameter dengan oshi jkt48

var fer = (nama, asal, gen) => {
     console.log (`${nama}, berasal dari daerah ${asal}, dan dari gen ${gen}`)
}

fer ("Christy", "Jakarta", 7)
fer ("Jessi", "Jakarta", 7)
fer ("Fiony", "Tangerang", 8)
fer ("Marsha", "Jakarta", 8)


console.log ("\n --- batas --- \n")



// Arrow Fungsi dengan kalkulator

var kal = (x, y) => {
     return x + y
}

var jel = (x, y) => {
     return x - y
}

var ber = (x, y) => {
     return x ** y
}

console.log (kal (10, 9))
console.log (jel (10, 7))
console.log (ber (8, 12))


console.log ("\n --- batas --- \n")