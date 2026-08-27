function dasar () {
     console.log ("Hello World")
}

dasar ()


console.log ("\n --- batas --- \n")




function nama (sapa) {
     console.log (`Halo saya ${sapa} dari jakarta timur`)
}

nama ("Royyan")
nama ("Fayyan")
nama ("Arroyan")
nama ("Rutter")
nama ("Gitter")


console.log ("\n --- batas --- \n")




// Fungsi dengan parameter

function des (nama) {
     console.log (`Halo saya ${nama} dari jakarta timur`)
}

des ("Fayyan")
des ("Rayyan")
des ("Jonan")
des ("Donho")
des ("Jonho")
des ("Mas Hoho")


console.log ("\n --- batas --- \n")



// Fungsi dengan return

function der (nama) {
     return `Halo saya ${nama} dari Jakarta TImur`
}

console.log (nama ("Hayyan"))
console.log (nama ("Yun"))
console.log (nama ("Jundy"))
console.log (nama ("Kop"))
console.log (nama ("Gunner"))
console.log (nama ("Loper"))


console.log ("\n --- batas --- \n")



// Fungsi return dengan operator

var x = 20
var y = 10

function tambah (x, y) {
     return x + y
}

function kurang (x, y) {
     return x - y
}

function kali (x, y) {
     return x * y
}

function bagi (x, y) {
     return x / y
}

function pangkat (x, y) {
     return x ** y
}

console.log (tambah (x, y))
console.log (kurang (x, y))
console.log (kali (x, y))
console.log (bagi (x, y))
console.log (pangkat (x, y))


console.log ("\n --- batas --- \n")



// Fungsi return dengan luas rumus bangun datar

function persegi (s) {
     return s * s
}

function persegi_panjang (p, l) {
     return p * l
}

function segitiga (a, t) {
     return a * t / 2
}

function belah_ketupat (d1, d2) {
     return d1 * d2 / 2
}

function lingkaran (phi, r) {
     return phi * r * r
}

console.log (persegi (10))
console.log (persegi_panjang (10, 15))
console.log (segitiga (10, 12))
console.log (belah_ketupat (34, 14))


console.log ("\n --- batas --- \n")




// Arrow Fungsi

var dasar = () => {
     console.log ("Hello World")
}

dasar ()


console.log ("\n --- batas --- \n")



// Arrow Fungsi 

var tes = () => {
     console.log ("Hello World")
     console.log ("Hello Fun")
     console.log ("Hello Jansen")
}

tes ()


console.log ("\n --- batas --- \n")



// Arrow Fungsi 

var gun = (nama) => {
     console.log (`Halo aku ${nama} dari Jakarta Utara`)
}

gun ("Tes")


console.log ("\n --- batas --- \n")




var bust = (x, y) => {
     return x + y * y
}

console.log (bust (10, 10, 10))


console.log ("\n --- batas --- \n")



// Array 1

var arr = ["Halo Dunia", "Halo Tegal", "Halo Semarang", "Halo Jateng"]

arr.push ("Halo Jatim")
arr.push ("Halo Jakarta pusat")
arr.push ("Halo Jakarta Timur")
arr.push ("Halo Jakarta Selatan")

for (i = 0; i < arr.length; i++) {
     console.log (arr [i])
}


console.log ("\n --- batas --- \n")




// Dictionary 

var data = {
     "nama" : "Habib muzakki",
     "asal" : "Kota Serang",
     "cek" : true,
     "coding" : "HTML, CSS, JavaScript dan Python",
     "tinggi" : "170 cm",
     "berat" : "60 kg",
}

for (k in data) {
     console.log (`${k} : ${data [k]}`)
}


console.log ("\n --- batas --- \n")




// Array 1

var data = [
     "1. Halo Dunia",
     "2. Halo Fast", 
     "3. Halo Dunia ku",
     "4. Halo Indonesia",
     "5. Halo Tes",
     "6. Halo Kompling"
]

data.push ("Halo Aku")
data.push ("Halo Tes")
data.push ("Halo Den")
data.push ("Halo Vest")

for (k = 0; k < data.length; k++) {
     console.log (data [k])
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




// Fungsi dengan percabangan dasar 2

function das (b) {

     if (b > 0) {
          console.log (`Angka positif, angka b = ${b}`)
     }

     else {
          console.log (`Angka negatif, angka b = ${b}`)
     }
}

das (-10)
das (-9)
das (-8)
das (7)
das (6)
das (5)
das (10)


console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan lanjutan

function fer (j) {

     if (j > 0) {
          console.log (`Angka j positif, angka j = ${j}`)
     }

     else if (j < 0) {
          console.log (`Angka j negatif, angka j = ${j}`)
     }

     else {
          console.log (`Angka nol, angka j = ${j}`)
     }
}

fer (-19)
fer (-23)
fer (-24)
fer (23)
fer (12)
fer (34)


console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan nested 

function der (k) {

     cek = true

     if (k >= 5) {
          if (cek) {
               console.log (`Besar, angka k = ${k}`)
          }

          else {
               console.log (`Kecil, angka k = ${k}`)
          }
     }

     else {
          console.log (`Kecil, angka k = ${k}`)
     }
}

der (10)
der (9)
der (8)
der (7)
der (6)
der (5)
der (4)
der (3)
der (2)
der (1)


console.log ("\n --- batas --- \n")




// Usia produktif manusia 

function fer (k) {

     if (k >= 15 && k <= 40) {
          console.log (`usia produktif manusia, usia = ${k}`)
     }

     else if (k > 40) {
          console.log (`usia sudah tua, usia = ${k}`)
     }

     else {
          console.log (`masih muda, usia = ${k}`)
     }
}

fer (70)
fer (60)
fer (50)
fer (40)
fer (30)
fer (20)
fer (10)


console.log ("\n --- batas --- \n")




function der (h) {

     cek = true

     if (h >= 5 && h <= 10) {
          if (cek) {
               console.log (`angka besar, angka h = ${h}`)
          }

          else {
               console.log (`angka tengah, angka h = ${h}`)
          }
     }

     else {
          console.log (`Angka kecil, angka h = ${h}`)
     }
}

der (10)
der (9)
der (8)
der (7)
der (6)
der (7)
der (5)
der (4)
der (3)
der (2)
der (1)


console.log ("\n --- batas --- \n")



