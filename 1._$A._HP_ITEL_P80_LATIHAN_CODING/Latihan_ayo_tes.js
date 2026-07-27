console.log ("\n Kalkulator dasar \n")

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


hasil_a = tambah (10, 10)
hasil_b = kurang (10, 5)
hasil_c = kali (10, 10)
hasil_d = bagi (10, 5)
hasil_e = pangkat (10, 10)


hitung = `
- Tambah  = ${hasil_a}
- Kurang  = ${hasil_b}
- Kali    = ${hasil_c}
- Bagi    = ${hasil_d}
- Pangkat = ${hasil_e}
`

console.log (hitung)


console.log ("\n --- batas --- \n")




console.log ("\n Tipe Data Pemrograman \n")

var teks = "Hujan"
var angka = 12
var desimal = 2.12
var cek = true
var char = 'a'
var kosong = null


tipe = `
- Teks    : ${teks}
- Angka   : ${angka}
- Desimal : ${desimal}
- Cek     : ${cek}
- Char    : ${char}
- Kosong  : ${kosong}
`


console.log (tipe)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Dasar \n")

function run (a) {
    
    if (a >= 5) {
        console.log (`Besar, angka a = ${a}`)
    }
    
    else {
        console.log (`Kecil, angka a = ${a}`)
    }
}

run (10)
run (9)
run (8)
run (7)
run (6)
run (5)
run (4)
run (3)
run (2)
run (1)


console.log ("\n --- batas -- \n")




console.log ("\n Fungsi dengan percabangan lanjutan \n")

function der (t) {
    
    if (t >= 8) {
        console.log (`Besar, angka t = ${t}`)
    }
    
    else if (t >= 5) {
        console.log (`Tengah, angka t = ${t}`)
    }
    
    else {
        console.log (`Kecil, angka t = ${t}`)
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



console.log ("\n Fungsi dengan Percabangan Skor \n")

function skor (f) {

     if (f >= 95) {
          console.log (`A, skor = ${f}`)
     }

     else if (f >= 90) {
          console.log (`B, skor = ${f}`)
     }

     else if (f >= 80) {
          console.log (`C, skor = ${f}`)
     }

     else if (f >= 70) {
          console.log (`D, skor = ${f}`)
     }

     else if (f >= 60) {
          console.log (`E, skor = ${f}`)
     }

     else if (f >= 50) {
          console.log (`F, skor = ${f}`)
     }

     else {
          console.log (`Jelek amat, skor = ${f}`)
     }
}

skor (100)
skor (90)
skor (80)
skor (70)
skor (60)
skor (50)
skor (40)


console.log ("\n --- batas --- \n")





console.log ("\n Fungsi dengan Percabangan Nested 1 \n")

function far (k) {

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

far (10)
far (9)
far (8)
far (7)
far (6)
far (5)
far (4)
far (3)
far (2)
far (1)

console.log ("\n --- batas --- \n")




console.log ("\n Switch Case  1 dengan int \n")

function kuo (p) {
    
    switch (p) {
        
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
            
        case 5:
            console.log ("Angka 5")
            break
            
        default:
        console.log ("Angka lain")
    }
}

kuo (1)
kuo (2)
kuo (3)
kuo (4)
kuo (5)
kuo (6)


console.log ("\n --- batas --- \n")




console.log ("\n Switch Case 2 dengan String \n")

function warna (b) {
    
    switch (b) {
        
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

warna ("Merah")
warna ("Kuning")
warna ("Hijau")
warna ("Hitam")


console.log ("\n --- batas --- \n")




console.log ("Fungsi return + percabangan dasar + mencari angka terkecil \n")

function angkan (i, p) {
    
    if (i < p) {
        return i
    }
    
    else {
        return p
    }
}

hasil_1 = angkan (1, 91)
hasil_2 = angkan (2, 31)
hasil_3 = angkan (3, 21)
hasil_4 = angkan (7, 11)
hasil_5 = angkan (2, 19)

console.log (hasil_1)
console.log (hasil_2)
console.log (hasil_3)
console.log (hasil_4)
console.log (hasil_5)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi return + percabangan dasar + mencari angka terbesar \n")

function desk (a, b) {
    
    if (a > b) {
        return a
    }
    
    else {
        return b
    }
}

hasil_k = desk (1, 10)
hasil_j = desk (3, 34)
hasil_g = desk (2, 24)
hasil_v = desk (7, 79)
hasil_x = desk (6, 27)

console.log (hasil_k)
console.log (hasil_j)
console.log (hasil_g)
console.log (hasil_v)
console.log (hasil_x)


console.log ("\n --- batas --- \n")




console.log ("\n For If Lanjutan \n")

for (a = 0; a < 11; a++) {
     if (a == 5) {
          continue
     }

     console.log (a)
}


console.log ("\n --- batas --- \n")



console.log ("\n For If lanjutan 2 \n")

for (r = 0; r < 11; r++) {
     if (r == 5) {
          break
     }

     console.log (r)
}

console.log ("\n --- batas --- \n")




console.log ("\n Array + For + If Lanjutan \n")

daf = ["Ranur", "Frank", "Ron", "Ajax", "Ajam"]

for (var a of daf) {
     if (a == "Ron") {
          continue
     }

     console.log (a)
}


console.log ("\n --- batas --- \n")



console.log ("\n Array + For + IF Lanjutan 1 \n")

ref = ["Hans", "Dans", "Rans", "Rons", "Fons"]

for (var b of ref) {
     if (b == "Rans") {
          break
     }

     console.log (b)
}


console.log ("\n --- batas --- \n")




console.log ("\n Struktur Data \n")

var data = {
     "teks" : "halo dunia",
     "angka" : 12,
     "desimal" : 3.14,
     "cek" : True,
     "kosong" : None,
}

console.log ("Teks :", data ["teks"])

console.log ("Angka :", data ["angka"])

console.log ("Desimal :", data ["desimal"])

console.log ("Cek :", data ["cek"])

console.log ("Kosong :", data ["kosong"])