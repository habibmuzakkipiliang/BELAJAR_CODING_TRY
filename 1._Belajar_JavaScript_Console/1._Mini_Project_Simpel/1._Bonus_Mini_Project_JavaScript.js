console.log ("\n Mini Project JavaScript \n")


console.log ("\n Data Variabel dasar \n")


var nama = "Habib Muzakki"
var panggilan = "Habib"
var kelas = "12 Agama"
var absen = 15
var sekolah = "MAN 2 KOTA SERANG"
var coding = "HTML, CSS, JavaScript dan Python"
var tinggi = "170 cm"
var berat = "60 kg"


console.log ("Nama lengkap :", nama)
console.log ("Nama panggilan :", panggilan)
console.log ("Kelas :", kelas)
console.log ("Absen :", absen)
console.log ("Coding :", coding,)
console.log ("Tinggi badan :", tinggi)
console.log ("Berat badan :", berat)


console.log ("\n", `Halo, saya ${nama}, dipanggil ${panggilan}, dari kelas ${kelas}, absen ke- ${absen}, dari sekolah ${sekolah}, dan saya mempelajari coding ${coding}, tinggi badan saya adalah ${tinggi},  berat badan saya adalah ${berat}`)


console.log ("\n --- Batas --- \n")




// Kalkulator Perjumlahan Sederhana

console.log ("Kalkulator Perjumlahan")

var a = 10
var b = 5

console.log ("hasil = ", a + b)




var x = 10
var y = 15

console.log ("Hasil = ", x + y)


console.log ("\n --- Batas --- \n")




// Kalkulator Pengurangan Sederhana 

console.log ("Kalkulator Pengurangan")

var c = 15
var d = 9

console.log ("Hasil = ", c - d)




var r = 20
var k = 5

console.log ("Hasil =", r - k)




var k = 50
var b = 40
var r = 30

console.log ("Hasil =", k - b - r)


console.log ("\n --- Batas --- \n")




// Kalkulator Perkalian

console.log ("Kalkulator Perkalian")

var n = 10
var k = 50


console.log ("Hasil =", n * k)




var e = 80
var r = 10
var m = 20

console.log ("Hasil =", e * r * m)


console.log ("\n --- Batas --- \n")




// Kalkulator Pangkat

console.log ("\n Kalkulator Pangkat \n")


var r = 10
var m = 5

console.log ("Hasil =", r ** m)




var e = 15
var j = 5

console.log ("Hasil =", e ** j)


console.log ("\n --- Batas --- \n")




// Kalkulator Modulus

console.log ("\n Kalkulator Modulus \n")


var h = 5
var u = 3

console.log ("Hasil =", h % u)




var y = 9
var k = 2

console.log ("Hasil =", y % k)




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
    
    
    
    var w = 45
    var j = 30
    var h = 10
    
    console.log ("Hasil =", w * j * h)
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
    
    
    
    
    var ket = "Yes"
    
    switch (ket) {
        
        case 1:
            console.log ("Yes")
            break
            
        case 2:
            console.log ("No")
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
    
    
    
    for (d = 0; d < 6; d++) {
        console.log ("d", d)
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    for (e = 0; e < 6; e++) {
        console.log ("e", e)
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    // Perulangan While dasar
    
    
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
    
    
    var c = 0
    
    while (c < 6) {
        console.log ("c", c)
        c++
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    var d = 0 
    
    while (d < 6) {
        console.log ("d", d)
        d++
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    var e = 0
    
    while (e < 6) {
        console.log ("e", e)
        e++
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Do While dasar
    
    console.log ("\n Do While Dasar \n")
    
    
    
    var a = 0
    
    do {
        console.log ("a", a)
        a++
    } while (a < 6)
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    var b = 0
    
    do {
        console.log ("b", b)
        b++
    } while (b < 6)
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    var c = 0
    
    do {
        console.log ("c", c)
        c++
    } while (c < 6)
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    var d = 0
    
    do {
        console.log ("d", d)
        d++
    } while (d < 6)
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    var e = 0
    
    do {
        console.log ("e", e)
        e++
    } while (e < 6)
    
    
}

perc ()


console.log ("\n --- Batas --- \n")





function tin () {
    
    // For Nested
    
    
    console.log ("\n For Nested \n")
    
    
    for (a = 0; a < 3; a++) {
        for (b = 0; b < 2; b++) {
            console.log ("b", b, "a", a)
        }
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    for (c = 0; c < 2; c++) {
        for (d = 0; d < 3; d++) {
            console.log ("d", d, "c", c)
        }
    }
    
    
    
    console.log ("\n --- Batas --- \n")
    
}

tin ()
