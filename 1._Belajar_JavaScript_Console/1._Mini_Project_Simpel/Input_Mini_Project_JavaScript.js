// Mini Project JavaScript

console.log ("\n Mini Project JavaScript \n")


// Input dan Output Sederhana


var a = parseInt (prompt ("Masukkan 1 + 1 = "))

if (a == 2) {
    console.log ("Benar")
}

else {
    console.log ("Salah")
}

console.log ("Hasil =", a)



console.log ("\n ----- Batas --- \n")




var b = parseInt (prompt ("1 * 1 = ? "))

if (b == 1) {
    console.log ("Benar")
}

else {
    console.log ("Salah")
}


console.log ("Hasil =", b)


console.log ("\n --- Batas --- \n")



// Input profil saya 

var nama = prompt ("Nama kamu  ?")
var kelas = prompt ("Dari kelas ?")
var absen = prompt ("Absen ke berapa ?")
var sekolah = prompt ("Dari sekolah mana ?")
var coding = prompt ("Belajar coding apa aja ?")
var tinggi = prompt ("Berapa tinggi badan kamu ??")
var berat = prompt ("Berapa berat badan kamu ??")


console.log ("Nama :", nama)
console.log ("Kelas :", kelas)
console.log ("Absen :", absen)
console.log ("Sekolah :", sekolah)
console.log ("Coding :", coding)
console.log ("Tinggi badan :", tinggi)
console.log ("Berat badan :", berat)


console.log ("\n", `Halo semuanya, saya ${nama}, dari kelas ${kelas}, absen ke - ${absen}, dari sekolah ${sekolah}, saya belajar coding yaitu ${coding}, tinggi badan saya adalah ${tinggi}, dan berat badan saya adalah ${berat}`)


console.log ("\n --- Batas --- \n")




// Kalkulator penjumlahan

console.log ("Kalkulator Penjumlahan")

a = parseInt (prompt ("angka a : "))
b = parseInt (prompt ("Angka b :"))

console.log ("Hasil =", a + b)




c = parseInt (prompt ("Angka c : "))
d = parseInt (prompt ("Angka d : "))

console.log ("Hasil =", c + d)




e = parseInt (prompt ("Angka e : "))
f = parseInt (prompt ("Angka f : "))

console.log ("Hasil =", e + f)


console.log ("\n --- Batas --- \n")




// Fungsi dan kombinasinya

console.log ("Fungsi dan kombinasinya \n")

function tes () {
    
    console.log ("Kalkulator Penjumlahan dalam Fungsi \n")
    
    
    var a = parseInt (prompt ("Angka a :"))
    var b = parseInt (prompt ("Angka b :"))
    
    
    console.log ("Hasil =", a + b)
    
    
    
    
    var c = parseInt (prompt ("Angka c :"))
    var d = parseInt (prompt ("Angka d :"))
    var e = parseInt (prompt ("Angka e :"))
    
    
    console.log ("Hasil =", c + d + e)
    
    
    console.log ("\n --- Batas --- \n")
}

tes ()


console.log ("\n --- Batas --- \n")




// Fungsi dan kombinasinya 

console.log ("\n Fungsi dan kombinasinya \n")


function tes () {
    
    console.log ("Kalkulator Fungsi Perjumlahan \n")
    
    var a = 40
    var b = 5
    
    
    console.log ("Hasil =", a + b)
    
    
    var c = 45
    var d = 34
    var e = 3
    
    console.log ("Hasil =", c + d - e)
    
    
    console.log ("\n --- Batas --- \n")
    
    
    console.log ("Kalkulator Fungsi Perkalian \n")
    
    var r = 10
    var k = 120
    var d = 34
    
    console.log ("Hasil =", r * k * d)
}

tes ()




console.log ("\n --- Batas --- \n")




// Fungsi dan Kombinasinya 2

console.log ("\n Fungsi dan Kombinasi 2")


function task () {
    
    console.log ("Percabangan dan Perulangan di dalam fungsi \n")
    
    console.log ("\n Percabangan Dasar \n")
    
    var a = 9
    
    if (a > 5) {
        console.log ("Besar")
    }
    
    else {
        console.log ("Kecil")
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    var b = 7
    
    if (b > 5 ) {
        console.log ("Besar")
    }
    
    else {
        console.log ("Kecil")
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Percabangan Lanjutan 
    
    console.log ("Percabangan Lanjutan \n")
    
    
    var c = 9
    
    if (c > 5) {
        console.log ("Besar")
    }
    
    else if (c < 5) {
        console.log ("Kecil")
    }
    
    else {
        console.log ("Semula")
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    var d = 4 
    
    if (d > 5) {
        console.log ("Besar")
    }
    
    else if (d < 5) {
        console.log ("Kecil")
    }
    
    else {
        console.log ("Semula")
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    // Percabangan Tangga Lanjutan 
    
    console.log ("Percabangan Tangga Lanjutan")
    
    var d = 9
    
    if (d > 7) {
        console.log ("Besar")
    }
    
    else if (d == 7) {
        console.log ("7")
    }
    
    else if (d == 6) {
        console.log ("6")
    }
    
    else if (d == 5) {
        console.log ("5")
    }
    
    else if (d == 4) {
        console.log ("4")
    }
    
    else if (d == 3) {
        console.log ("3")
    }
    
    else if (d == 2) {
        console.log ("2")
    }
    
    else if (d == 1) {
        console.log ("1")
    }
    
    else {
        console.log ("Semula")
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Percabangan Nested 
    
    console.log ("\n Percabangan Nested \n")
    
    var d = 10
    var cek = true
    
    if (cek) {
        if (d > 5) {
            console.log ("Besar")
        }
        
        else {
            console.log ("Kecil")
        }
    }
    
    else {
        console.log ("Semula")
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Percabangan Nested 1
    
    console.log ("\n Percabangan Nested 1 \n")
    
    
    var r = 3
    var cek = true
    
    if (cek) {
        if (r > 5) {
            console.log ("Besar")
        }
        
        else if (r < 5) {
            console.log ("Kecil")
        }
    }
    
    else {
        console.log ("Semula")
    }
}

task ()


console.log ("\n --- Batas --- \n")


function tam () {
    
    // Switch Case di dalam Fungsi 
    
    console.log ("Switch Case di dalam Fungsi \n")
    
    var a = 6
    
    switch (a) {
        
        case 1:
            console.log ("1")
            break
            
        case 2:
            console.log ("2")
            break
            
        case 3:
            console.log ("3")
            break
            
        case 4:
            console.log ("4")
            break
            
        case 5:
            console.log ("5")
            break 
            
        case 6:
            console.log ("6")
            break
            
        default:
        console.log ("Semula")
    }
}

tam ()


console.log ("\n --- Batas --- \n")




function perc () {
    
    // Perulangan For, While dan Do-While di dalam Fungsi
    
    
    console.log ("Perulangan For, While dan Do-While di dalam Fungsi \n")
    
    
    console.log ("\n Perulangan For dasar \n")
    
    
    
    for (a = 0; a < 6; a++) {
        console.log ("a", a)
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    for (b = 0; b < 6; b++) {
        console.log ("b", b)
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    for (c = 0; c < 6; c++) {
        console.log ("c", c)
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    // Perulangan While dasat
    
    
    console.log ("\n Perulangan While dasar \n")
    
    
    var a = 0 
    
    while (a < 6) {
        console.log ("a", a)
        a++
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    var b = 0
    
    while (b < 6) {
        console.log ("b", b)
        b++
    }
    
    
    
    console.log ("\n --- Batas --- \n")
}

perc ()