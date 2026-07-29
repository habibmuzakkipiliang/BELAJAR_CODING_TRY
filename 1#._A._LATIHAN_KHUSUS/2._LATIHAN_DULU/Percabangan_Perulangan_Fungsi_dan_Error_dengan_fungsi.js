// Switch Case 1

function dek (m) {

     switch (m) {

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

dek (1)
dek (2)
dek (3)
dek (4)
dek (5)


console.log ("\n --- batas --- \n")




// Switch Case 2

function ger (p) {

     switch (p) {

          case "Merah":
               console.log ("Warna merah")
               break

          case "Kuning":
               console.log ("Warna kuning")
               break

          case "Hijau":
               console.log ("Warna hijau")
               break

          default:
               console.log ("Warna lain")
     }
}

ger ("Merah")
ger ("Kuning")
ger ("Hijau")
ger ("Hitam")


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

function lan (e) {

     if (e >= 8) {
          console.log (`Besar, angka e = ${e}`)
     }

     else if (e >= 5) {
          console.log (`Tengah, angka e = ${e}`)
     }

     else {
          console.log (`Kecil, angka e = ${e}`)
     }
}

lan (10)
lan (9)
lan (8)
lan (7)
lan (6)
lan (5)
lan (4)
lan (3)
lan (2)
lan (1)


console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan rapor 

function rapor (f) {

     if (f >= 95) {
          console.log (`A, nilai = ${f}`)
     }

     else if (f >= 90) {
          console.log (`B, nilai = ${f}`)
     }

     else if (f >= 80) {
          console.log (`C, nilai = ${f}`)
     }

     else if (f >= 70) {
          console.log (`D, nilai = ${f}`)
     }

     else if (f >= 60) {
          console.log (`E, nilai = ${f}`)
     }

     else if (f >= 50) {
          console.log (`F, nilai = ${f}`)
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
rapor (5)


console.log ("\n --- batas --- \n")



// Fungsi dengan Percabangan Nested 1 

function der (d) {
     
     cek = true

     if (d >= 5) {
          if (cek) {
               console.log (`Besar, angka d = ${d}`)
          }

          else {
               console.log (`Tengah, angka d = ${d}`)
          }
     }

     else {
          console.log (`Kecil, angka e = ${e}`)
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




// Fungsi dengan Percabangan Nested 2 

function fer (k) {

     cek = true

     if (k >= 8) {
          if (cek) {
               console.log (`Besar, angka k = ${k}`)
          }

          else if (k >= 5) {
               console.log (`Tengah, angka k = ${k}`)
          }
     }

     else {
          console.log (`Kecil, angka k = ${k}`)
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




// Fungsi Usia Produktif manusia

function pro (j) {

     if (j >= 15 && j <= 40) {
          console.log (`Usia sudah produktif, usia = ${j}`)
     }

     else if (j > 40) {
          console.log (`Sudah tua usiannya, usia = ${j}`)
     }

     else {
          console.log (`Masih kecil usiannya, usia = ${j}`)
     }
}

pro (50)
pro (40)
pro (30)
pro (20)
pro (10)
pro (5)
pro (3)


console.log ("\n --- batas --- \n")




// Fungsi dengan Percabangan Usia masuk JKT48

function der (e) {

     if (e >= 13 && e <= 19) {
          console.log (`Usia yang sudah boleh, usia = ${e}`)
     }

     else if (e > 19) {
          console.log (`Sudah lebih dari cukup, usia = ${e}`)
     }

     else {
          console.log (`Masih kecil usiannya, usia = ${e}`)
     }
}

der (30)
der (20)
der (10)
der (5)
der (2)


console.log ("\n --- batas --- \n")




// For dasar 

for (a = 1; a < 11; a++) {
     console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- batas --- \n")



// For dasar 2 

for (b = 0; b < 11; b++) {
     console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- batas --- \n")




// Struktur data

var dat = ["Halo Dunia", "Halo Fire", "Halo World", "Fireball"]

for (a = 0; a < dat.length; a++) {
     console.log (dat [a])
}


console.log ("\n --- batas --- \n")




// Struktur data 2

var der = ["Valid", "Notch", "Fall", "None"]

for (b = 0; b < der.length; b++) {
     console.log (der [b])
}


console.log ("\n --- batas --- \n")