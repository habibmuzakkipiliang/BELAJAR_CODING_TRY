console.log ("\n Fungsi dengan Percabangan dasar \n")

function dasar (a) {

     if (a >= 5) {
          console.log (`Besar, angka a = ${a}`)
     }

     else {
          console.log (`Kecil, angka a = ${a}`)
     }
}

dasar (10)
dasar (8)
dasar (5)
dasar (4)
dasar (3)
dasar (2)
dasar (1)


console.log ("\n --- batas --- \n")



console.log ("\n Fungsi dengan percabangan lanjutan \n")

function rur (r) {

     if (r >= 8) {
          console.log (`Besar, angka r = ${r}`)
     }

     else if (r >= 5) {
          console.log (`Tengah, angka r = ${r}`)
     }

     else {
          console.log (`Kecil, angka r = ${r}`)
     }
}

rur (10)
rur (9)
rur (8)
rur (7)
rur (6)
rur (5)
rur (4)
rur (3)
rur (2)
rur (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan percabangan nilai rapor \n")

function nilai (q) {

     if (q >= 90) {
          console.log (`A, nilai = ${q}`)
     }

     else if (q >= 80) {
          console.log (`B, nilai = ${q}`)
     }

     else if (q >= 70) {
          console.log (`C, nilai = ${q}`)
     }

     else if (q >= 60) {
          console.log (`D, nilai = ${q}`)
     }

     else if (q >= 50) {
          console.log (`E, nilai = ${q}`)
     }

     else {
          console.log (`Jelek amat, nilai = ${q}`)
     }
}

nilai (100)
nilai (90)
nilai (80)
nilai (70)
nilai (60)
nilai (50)
nilai (40)


console.log ("\n --- batas --- \n")




console.log ("\n Nested 1 \n")

function nes (y) {

     cek = true

     if (y >= 5) {
          if (cek) {
               console.log (`Besar, angka y = ${y}`)
          }
     }

     else {
          console.log (`Kecil, angka y = ${y}`)
     }
}

nes (10)
nes (9)
nes (8)
nes (7)
nes (6)
nes (5)
nes (4)
nes (3)
nes (2)
nes (1)


console.log ("\n --- batas --- \n")




console.log ("\n Usia produktif manusia \n")

function er (w) {

     if (w >= 15 && w <= 40) {
          console.log (`Termasuk usia produktif, usia = ${w}`)
     }

     else if (w > 40) {
          console.log (`Sudah tua usianya, usia = ${w}`)
     }

     else {
          console.log (`Usiannya masih kecil, usia = ${w}`)
     }
}

er (60)
er (50)
er (40)
er (30)
er (20)
er (10)
er (5)
er (4)


console.log ("\n --- batas --- \n")




console.log ("\n Usia kerja manusia \n")

function kerja (f) {
     
     if (f >= 23 && f <= 45) {
          console.log (`Boleh kerja, usia = ${f}`)
     }

     else if (f > 45) {
          console.log (`Sudah tua, usia = ${f}`)
     }

     else {
          console.log (`Masih kecil usianya, usia = ${f}`)
     }
}

kerja (60)
kerja (50)
kerja (40)
kerja (30)
kerja (20)
kerja (10)
kerja (5)


console.log ("\n --- batas --- \n")




console.log ("\n Usia daftar JKT48 \n")

function oshi (e) {

     if (e >= 13 && e <= 18) {
          console.log (`Boleh daftar jkt48, usia = ${e}`)
     }

     else if (e > 18) {
          console.log (`Sudah lebih dari cukup, usia = ${e}`)
     }

     else {
          console.log (`Masih belum boleh, usia = ${e}`)
     }
}

oshi (25)
oshi (24)
oshi (20)
oshi (19)
oshi (18)
oshi (17)
oshi (16)
oshi (15)
oshi (14)
oshi (13)
oshi (12)
oshi (11)


console.log ("\n --- batas --- \n")