console.log ("\n Fungsi dengan Percabangan Dasar \n")

function run (j) {
    
    if (j >= 5) {
        console.log (`Besar, angka j = ${j}`)
    }
    
    else {
        console.log (`Kecil, angka j = ${j}`)
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



console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function er (w) {
    
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

er (10)
er (9)
er (8)
er (7)
er (6)
er (5)
er (4)
er (3)
er (2)
er (1)


console.log ("\n --- batas --- \n")




console.log ("\n Nested 1 \n")

function wer (s) {
    
    cek = true
    
    if (s >= 5) {
        if (cek) {
            console.log (`Besar, angka s = ${s}`)
        }
    }
    
    else {
        console.log (`Kecil, angka s = ${s}`)
    }
}

wer (10)
wer (9)
wer (8)
wer (7)
wer (6)
wer (5)
wer (4)
wer (3)
wer (2)
wer (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan pembagian nilai rapor \n")

function rapor (d) {
    
    if (d >= 90) {
        console.log (`A, nilai = ${d}`)
    }
    
    else if (d >= 80) {
        console.log (`B, nilai = ${d}`)
    }
    
    else if (d >= 70) {
        console.log (`C, nilai = ${d}`)
    }
    
    else if (d >= 60) {
        console.log (`D, nilai = ${d}`)
    }
    
    else if (d >= 50) {
        console.log (`E, nilai = ${d}`)
    }
    
    else {
        console.log (`Jelek, nilai = ${d}`)
    }
}

rapor (95)
rapor (90)
rapor (80)
rapor (70)
rapor (65)
rapor (60)
rapor (50)
rapor (30)
rapor (20)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Angka Terbesar \n")

function besar (u, k) {
    
    if (u > k) {
        return u
    }
    
    else {
        return k
    }
}

console.log (besar (10, 8))
console.log (besar (90, 8))
console.log (besar (3, 12))
console.log (besar (23, 4))



console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Angka Terkecil \n")

function kecil (x, y) {
    
    if (x < y) {
        return x
    }
    
    else {
        return y
    }
}

console.log (kecil (2, 20))
console.log (kecil (20, 4))
console.log (kecil (90, 3))
console.log (kecil (12, 9))
console.log (kecil (34, 8))


console.log ("\n --- batas --- \n")




console.log ("\n For dasar \n")

for (a = 0; a < 11; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n For dasar 2 \n")

for (c = 1; c < 11; c++) {
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




console.log ("\n While dasae 2 \n")


var b = 11

while (b > 0) {
    console.log (`Urutan ke - ${b}`)
    b--
}


console.log ("\n --- batas --- \n")




console.log ("\n Array 1 \n")

var dat = ["Ron", "Var", "Roa", "Rou", "Lam", "Fer", "Rot", "Ber"]

for (a = 0; a < dat.length; a++) {
    console.log (dat [a])
}


console.log ("\n --- batas --- \n")





console.log ("\n Array 2 \n")

var er = ["Gun", "Ver", "Roas", "Lambert", "Bertha", "Hujan", "Api", "Best"]

for (b = 0; b < er.length; b++) {
    console.log (er [b])
}


console.log ("\n --- batas --- \n")




console.log ("\n Dictionary \n")

var der = {
    "nama" : "Habib Muzakki",
    "asal" : "Kota Serang",
    "usia" : 12,
    "cek" : true,
}

console.log ("Nama :", der ["nama"])
console.log ("Asal :", der ["asal"])
console.log ("Usia :", der ["usia"])
console.log ("Cek :", der ["cek"])