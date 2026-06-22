// Latihan Project Sederhana JavaScript

console.log ("\n Latihan Project Sederhana JavaScript \n")


var tes = "Ayo Latihan JavaScript untuk memulai Project nya \n"
console.log (tes)




var nama = prompt ("Nama kamu siapa ? ")
var asal = prompt ("Dari mana asal kamu ? ")
var tinggal = prompt ("Tempat tinggal kamu dimana ? ")
var usia = Number (prompt ("Usia kamu berapa ? "))
var hobi = prompt ("Hobi kamu apa ? ")
var darah = prompt ("Golongan darah ? ")
var suku = prompt ("Suku kamu ? ")
var agama = prompt ("Agama kamu ? ")
var fans = prompt ("Fans kamu ? ")


console.log ("\n --- Batas --- \n")




if (usia >= 25) {
    console.log ("Usia lebih dari 25 tahun")
}

else if (usia >= 24) {
    console.log ("Usia kamu 24 tahun")
}

else if (usia >= 23) {
    console.log ("Usia kamu 23 tahun")
}

else if (usia >= 22) {
    console.log ("Usia kamu 22 tahun")
}

else if (usia >= 21) {
    console.log ("Usia kamu 21 tahun")
}

else if (usia >= 20) {
    console.log ("Usia kamu 20 tahun")
}

else if (usia >= 19) {
    console.log ("Usia kamu 19 tahun")
}

else if (usia >= 18) {
    console.log ("Usia kamu 18 tahun")
}

else if (usia >= 17) {
    console.log ("Usia kamu 17 tahun")
}

else if (usia >= 16) {
    console.log ("Usia kamu 16 tahun")
}

else {
    console.log ("Usia kamu dibawah 16 tahun")
}


console.log ("\n --- Batas --- \n")




var profil = `

--- Profil ---

- Nama    : ${nama}
- Asal    : ${asal}
- Alamat  : ${tinggal}
- Usia    : ${usia}
- Hobi    : ${hobi}
- Darah   : ${darah}
- Suku    : ${suku}
- Agama   : ${agama}
- Fans    : ${fans}


`


console.log (profil)


console.log ("\n --- Batas --- \n")




console.log ("\n Oshi Saya \n")

var oshi = [
    
    "1. Michie JKT48",
    "2. Gracie JKT48",
    "3. Lily JKT48",
    "4. Fritzy JKT48",
    "5. Anindya JKT48",
    "6. Christy JKT48",
    "7. Freya JKT48",
    
    ]
    
    
for (a = 0; a < oshi.length; a++) {
    console.log (oshi [a])
}
    
    
console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Dasar Login \n")

var login = "mark"
var passoword = "kino"

if ((login == "mark") && (passoword == "kino")) {
    console.log ("Benar")
}

else {
    console.log ("Salah")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Percabangan Dasar \n")

function wen (an) {
     
    if (an >= 5) {
        console.log (`Besar, angka = ${an}`)
    }
    
    else {
        console.log (`Kecil, angka = ${an}`)
    }
}

wen (10)
wen (3)
wen (9)
wen (3)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Percabangan Lanjutan 1 \n")

function er (b) {

    if (b >= 10) {
        console.log (`Besar, angka = ${b}`)
    }

    else if (b == 5) {
        console.log (`Setengah, angka = ${b}`)
    }

    else {
        console.log (`Kurang, angka = ${b}`)
    }
}

er (10)
er (3)
er (1)
er (10)
er (6)

console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Percabangan Nested 1 \n")

function fur (d) {

    var cek = true

    if (d >= 10) {
        if (cek == true) {
            console.log (`Besar, angka = ${d}`)
        }

        else if (d <= 5) {
            console.log (`Kecil, angka = ${d}`)
        }
    }

    else {
        console.log (`Sama saja, angka = ${d}`)
    }
}

fur (10)
fur (3)
fur (2)
fur (8)
fur (9)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Percabangan Nested 2 \n")

function hun (e) {
    
    var cek = true
    
    if (e >= 10) {
        if (cek == true) {
            console.log (`Besar, angka = ${e}`)
        }

        else {
            console.log (`Kecil, angka = ${e}`)
        }
    }

    else {
        console.log (`Sama saja, angka = ${e}`)
    }
}

hun (10)
hun (3)
hun (9)
hun (3)
hun (7)


console.log ("\n --- Batas -- \n")





console.log ("\n Fungsi Percabangan Nested Majemuk Kompleks \n")

function op (usia, uang) {
    
    var cek = true
    
    if ((usia >= 15) && (uang >= 5000)) {
        if (cek == true) {
            console.log (`Berarti kamu udah cukup, usia = ${usia}, uang = ${uang}`)
        }
        
        else if ((usia <= 15) && (uang <= 5000)) {
            console.log (`Kamu belum cukup, usia = {usia}, uang = {uang}`)
        }
        
        else {
            console.log (`Kamu masih ada waktu, usia = ${usia}, uang = ${uang}`)
        }
    }
    
    else {
        console.log (`Kamu belum ada sama sekali, usia = ${usia}, uang = ${uang}`)
    }
}

op (10, 3000)
op (19, 6000)
op (12, 10000)