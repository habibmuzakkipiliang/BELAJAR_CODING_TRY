// Percabangan dasar, Switch Case, lanjutan dan nested 

console.log ("\n Percabangan dasar, Switch Case, Lanjutan dan Nested \n")


console.log ("\n Percabangan dasar \n")


var a = 9

if (a > 5) {
    console.log ("Besar")
}

else {
    console.log ("Kecil")
}


console.log ("\n --- Batas --- \n")




var b = 4

if (b > 5) {
    console.log ("Besar")
}

else {
    console.log ("Kecil")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case \n")


var a = 3

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


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 1 \n")


var b = 2 

switch (b) {
    
    case 1:
        console.log ("Iya")
        break
        
    case 2:
        console.log ("Tidak")
        break
        
    default:
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 2 \n")


var kondisi = 3

switch (kondisi) {
    
    case 1:
        console.log ("Laper dan haus banget")
        break
        
    case 2:
        console.log ("Laper dan haus dikit")
        break
        
    case 3:
        console.log ("Laper dan haus sedang")
        break
        
    case 4:
        console.log ("Kenyang dikit dan agak mending")
        break
        
    case 5:
        console.log ("Kenyang poll dan stabil")
        break
        
    default:
    console.log ("Gak apa - apa kok")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 3 \n")


var nilai = 100

switch (nilai) {
    
    case 100:
        console.log ("Mantap Jiwa")
        break
        
    case 95:
        console.log ("Mantap dikit")
        break
        
    case 90:
        console.log ("Mantap sedang")
        break
        
    case 85:
        console.log ("B +")
        break
        
    case 80:
        console.log ("B")
        
    case 75:
        console.log ("C")
        break
        
    default:
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan \n")


var a = 9

if (a > 5) {
    console.log ("Besar")
}

else if (a < 5) {
    console.log ("Kecil")
}

else {
    console.log ("Basic")
}


console.log ("\n --- Batas --- \n")




var b = 3

if (b > 5) {
    console.log ("Besar")
}

else if (b < 5) {
    console.log ("Kecil")
}

else {
    console.log ("Basic")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Tangga Lanjutan \n")


var a = 10

if (a > 7) {
    console.log ("Besar")
}

else if (a == 6) {
    console.log ("6")
}

else if (a == 5) {
    console.log ("5")
}

else if (a == 4) {
    console.log ("4")
}

else if (a == 3) {
    console.log ("3")
}

else if (a == 2) {
    console.log ("2")
}

else if (a == 1) {
    console.log ("1")
}

else {
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Tangga Lanjutan 2 \n")


var b = 2

if (b > 5) {
    console.log ("Besar")
}

else if (b == 6) {
    console.log ("6")
}

else if (b == 5) {
    console.log ("5")
}

else if (b == 4) {
    console.log ("4")
}

else if (b == 3) {
    console.log ("3")
}

else if (b == 2) {
    console.log ("2")
}

else if (b == 1) {
    console.log ("1")
}

else {
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 level 1 \n")

var a = 9
var cek = true

if (cek) {
    if (a > 5) {
        console.log ("Besar")
    }
    
    else if (a < 5) {
         console.log ("Kecil")
    }
}

else {
    console.log ("Basic")
}


console.log ("\n --- Batas --- \n")




var b = 3
var cek = true

if (cek) {
    if (b > 5) {
        console.log ("Besar")
    }
    
    else if (b < 5) {
        console.log ("Kecil")
    }
}

else {
    console.log ("Basic")
}


console.log  ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 2 level 1 \n")

var a = 9
var cek = true

if (cek) {
    if (a > 5) {
        console.log ("Besar")
    }
    
    else {
        console.log ("Kecil")
    }
}

else {
    console.log ("Basic")
}


console.log ("\n --- Batas --- \n")




var b = 3
var cek = true

if (cek) {
    if (b > 5) {
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




console.log ("\n Percabangan Nested level 2 \n")


var umur = 17
var sim = true

if (sim) {
    if (umur >= 17) {
        console.log ("Boleh ambil dan tes sim")
    }
    
    else if (umur < 17) {
         console.log ("Belum boleh ambil dan tes sim")
    }
}

else {
    console.log ("Jangan sama sekali")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested level 2 (Member JKT48) \n")


var usia = 18
var cek = true

if (cek) {
    if (usia >= 13) {
        console.log ("Boleh ikut audisi dan gabung JKT48")
    }
    
    else if (usia < 13) {
        console.log ("Gak boleh ikut audisi JKT48")
    }
}

else {
    console.log ("Jangan ikut dulu ya")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested level 2 (Kerja IT dan Teknologi dan Coding) \n")


var usia = 19
var cek = true

if (cek) {
    if (usia >= 25) {
        console.log ("Boleh kerja dong")
    }
    
    else if (usia < 25) {
        console.log ("Belum bisa ya")
    }
}

else {
    console.log ("Kembali ke semula")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested level 2 (Teknologi dan Coding) \n")


var usia = 23
var cek = true

if (cek) {
    if (usia >= 20) {
        console.log ("Boleh dan Gabung")
    }
    
    else if (usia < 20) {
        console.log ("Gak bisa dulu")
    }
}

else {
    console.log ("Pindah ke yang lain")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested level 3 (member JKT48 tahap 2) \n")


var umur = 15
var cek = true

if (cek) {
    if ((umur >= 13) && (umur <= 17)) {
        console.log ("Boleh gabung dan ikut audisi JKT48")
    }
    
    else if (umur > 17) {
        console.log ("Wah, lebih dari cukup guys ya")
    }
    
    else {
        console.log ("Sabar ya bagi teman - teman yang masih dibawah 13 tahun")
    }
}

else {
    console.log ("Jangan ikut sama sekali")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested level 3 (SIM) \n")


var umur = 19
var sim = true

if (sim) {
    if ((umur >= 17) && (umur <= 25)) {
        console.log ("Boleh punya dan ambil SIM")
    }
    
    else if (umur > 25) {
        console.log ("Sudah matang mentalnya")
    }
    
    else {
        console.log ("Belum boleh punya SIM")
    }
}

else {
    console.log ("Jangan dulu ya")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested Level 3 (Usia dalam produktif kerja) \n")


var usia = 30
var cek = true

if (cek) {
    if ((usia >= 25) && (usia <= 45)) {
        console.log ("Usia yang produktif dan mateng")
    }
    
    else if (usia > 45) {
        console.log ("Bukan usia produktif, sudah mulai tua")
    }
    
    else {
        console.log ("Bukan usia produktif, masih muda")
    }
}

else {
    console.log ("Masih remaja banget")
}


console.log ("\n --- Batas --- \n")