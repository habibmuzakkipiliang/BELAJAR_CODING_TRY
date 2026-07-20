console.log ("\n Fungsi dengan Percabangan dasar \n")

function fun (a) {

     if (a >= 5) {
          console.log (`Besar, angka a = ${a}`)
     }

     else {
          console.log (`Kecil, angka a = ${a}`)
     }
}

fun (10)
fun (9)
fun (8)
fun (7)
fun (6)
fun (5)
fun (4)
fun (3)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function der (n) {

     if (n >= 8) {
          console.log (`Besar, angka n = ${n}`)
     }

     else if (n >= 5) {
          console.log (`Tengah, angka n = ${n}`)
     }

     else {
          console.log (`Kecil, angka n = ${n}`)
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




console.log ("\n Fungsi dengan Percabangan Nilai Rapor \n")

function der (j) {

     if (j >= 90) {
          console.log (`A, nilai = ${j}`)
     }

     else if (j > 80) {
          console.log (`B, nilai = ${j}`)
     }

     else if (j >= 70) {
          console.log (`C, nilai = ${j}`)
     }

     else if (j >= 60) {
          console.log (`D, nilai = ${j}`)
     }

     else if (j >= 50) {
          console.log (`E, nilai = ${j}`)
     }
     
     else {
          console.log (`Jelek amat, nilai = ${j}`)
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






console.log ("\n Usia produktif manusia \n")

function usia (l) {

     if (l >= 15 && l <= 50) {
          console.log (`Usia sudah produktif, usia = ${l}`)
     }

     else if (l > 50) {
          console.log (`Sudah tua usianya, usia = ${l}`)
     }

     else if (l < 15) {
          console.log (`Masih dibawah umur, usia = ${l}`)
     }

     else {
          console.log (`Masih kecil, usia nya = ${l}`)
     }
}

usia (70)
usia (60)
usia (50)
usia (40)
usia (30)
usia (20)
usia (10)


console.log ("\n --- batas --- \n")



console.log ("\n Fungsi dengan Usia masuk JKT48 \n")

function jkt48 (h) {

     if (h >= 13 && h <= 18) {
          console.log (`Sudah boleh masuk JKT48, usia = ${h}`)
     }

     else if (h > 18) {
          console.log (`Sudah lebih dari cukup, usia = ${h}`)
     }

     else {
          console.log (`Masih dibawah umur, usia = ${h}`)
     }
}

jkt48 (20)
jkt48 (19)
jkt48 (18)
jkt48 (17)
jkt48 (16)
jkt48 (15)
jkt48 (14)
jkt48 (13)
jkt48 (12)
jkt48 (11)


console.log ("\n --- batas --- \n")



console.log ("\n Fungsi dengan Usia Masuk JKT48 \n")

function run (s) {

     if (s >= 13 && s <= 19) {
          console.log (`Usia yang boleh masuk jkt48, usia = ${s}`)
     }

     else if (s > 19) {
          console.log (`Sudah lebih dari cukup, usia = ${s}`)
     }

     else {
          console.log (`Masih dibawah umur, usia = ${s}`)
     }
}

run (60)
run (50)
run (40)
run (30)
run (20)
run (10)


console.log ("\n --- batas --- \n")



console.log ("\n Fungsi dengan Nested 1 \n")

function deg (k) {

     cek = true

     if (k >= 5) {
          if (cek) {
               console.log (`Besar, angka k = ${k}`)
          }
     }

     else {
          console.log (`Kecil, angka k = ${k}`)
     }
}

deg (8)
deg (7)
deg (6)
deg (4)
deg (2)
deg (1)


console.log ("\n --- batas --- \n")




console.log ("\n Usia untuk kerja \n")

function der (l) {

     if (l >= 24 && l <= 40) {
          console.log (`Boleh kerja, usia = ${l}`)
     }

     else if (l > 40) {
          console.log (`Pensiun, usia = ${l}`)
     }

     else {
          console.log (`Belum boleh kerja, usia = ${l}`)
     }
}

der (60)
der (50)
der (40)
der (30)
der (20)
der (10)


console.log ("\n --- batas --- \n")




console.log ("\n For dasar \n")

for (a = 0; a < 11; a++) {
     console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- batas --- \n")



for (b = 1; b < 11; b++) {
     console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- batas --- \n")




for (c = 5; c < 21; c++) {
     console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n While dasar \n")

var a = 1

while (a < 11) {
     console.log (`Urutan ke - ${a}`)
     a++
}


console.log ("\n --- batas --- \n")




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

for (x = 1; x < 3; x++) {
     for (y = 1; y < 3; y++) {
          console.log (`Luar : ${x}, Dalam : ${y}`)
     }
}


console.log ("\n --- batas --- \n")




console.log ("\n Array 1 \n")

var df = ["Von", "Ros", "Rt", "VEr", "Hun", "Runt"]

df.push ("Rust")
df.push ("Cin")
df.push ("Fun")
df.push ("Vor")
df.push ("Ros")

for (a = 0; a < df.length; a++) {
     console.log (df [a])
}


console.log ("\n --- batas --- \n")




console.log ("\n Array 2 \n")

var tr = ["Hun", "Run", "Vor", "Rao", "Ben", "Re"]

tr.push ("Gur")
tr.push ("Yon")
tr.push ("Ver")
tr.push ("Rto")
tr.push ("Von")
tr.push ("Fan")

for (b = 0; b < tr.length; b++) {
     console.log (tr [b])
}


console.log ("\n --- batas --- \n")