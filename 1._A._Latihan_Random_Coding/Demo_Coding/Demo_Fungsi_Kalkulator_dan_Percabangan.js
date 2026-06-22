console.log ("\n Fungsi Kalkulator dan Percabangan \n")


function kalkulator () {
    
    var a = 10
    var b = 5
    
    var tambah  = a + b 
    var kurang  = a - b 
    var kali    = a * b 
    var bagi    = a / b 
    var pangkat = a ** b
    var modulus = a % b 
    
    
    var hasil_1 = a > b
    var hasil_2 = a < b
    var hasil_3 = a >= b
    var hasil_4 = a <= b
    var hasil_5 = a == b
    var hasil_6 = a != b
    
    
    var hasil_7 = ((a > b) && (a < b))
    var hasil_8 = ((a < b) || (a > b))
    var hasil_9 = (!a)
    var hasil_10 = (!b)
    
    
    detail = `
    
    Tambah  = ${tambah}
    Kurang  = ${kurang}
    Kali    = ${kali}
    Bagi    = ${bagi}
    Pangkat = ${pangkat}
    Modulus = ${modulus}
    
    -------------------
    
    
    Hasil = ${hasil_1}
    Hasil = ${hasil_2}
    Hasil = ${hasil_3}
    Hasil = ${hasil_4}
    Hasil = ${hasil_5}
    Hasil = ${hasil_6}
    
    -------------------
    
    
    Hasil = ${hasil_7}
    Hasil = ${hasil_8}
    Hasil = ${hasil_9}
    Hasil = ${hasil_10}
    
    -------------------
    
    `
    
    console.log (detail)
  
}  
    
kalkulator ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Percabangan Dasar \n")

function des (a) {
    
    if (a > 5) {
        console.log (`Angka Besar, a = ${a}`)
    }
    
    else {
        console.log (`Angka Kecil, a = ${a}`)
    }
}

des (10)
des (3)
des (15)
des (4)
   
   
console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Percabangan dasar 2 \n")

function en (b) {
    
    if (b > 5) {
        console.log (`Angka besar, b = ${b}`)
    }
    
    else {
        console.log (`Angka kecil, b = ${b}`)
    }
}

en (10)
en (4)
en (8)
en (3)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi percabangan lanjutan 1 \n")

function ran (c) {
    
    if (c > 5) {
        console.log (`Angka besar, c = ${c}`)
    }
    
    else if (c < 5) {
        console.log (`Angka kecil, c = ${c}`)
    }
    
    else {
        console.log (`Sama saja, c = ${c}`)
    }
}

ran (10)
ran (3)
ran (7)
ran (3)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Percabangan Lanjutan 2 \n")

function kok (d) {
    
    if (d > 5) {
        console.log (`Angka besar, d = ${d}`)
    }
    
    else if (d < 5) {
        console.log (`Angka kecil, d = ${d}`)
    }
    
    else {
        console.log (`Sama saja, d = ${d}`)
    }
}

kok (10)
kok (3)
kok (6)
kok (3)
kok (9)
kok (4)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Percabangan Nested 1 \n")

function dek (usia) {
    
    var cek = true
    
    if (usia >= 15) {
        if (cek == true) {
            console.log (`Boleh dong, usia = ${usia}`)
        }
        
        else if (usia <= 15) {
            console.log (`Belum dong, usia = ${usia}`)
        }
    }
    
    else {
        console.log (`Sama saja, usia = ${usia}`)
    }
}


dek (20)
dek (13)
dek (19)
dek (20)
dek (10)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Percabangan Nested 2 \n")

function jun (usia) {
    
    var cek = true
    
    if (usia >= 5) {
        if (cek == true) {
            console.log (`Oke dong, usia = ${usia}`)
        }
        
        else {
            console.log (`Belum oke dong, usia = ${usia}`)
        }
    }
    
    else {
        console.log (`Masih belum sama sekali, usia = ${usia}`)
    }
}

jun (10)
jun (3)
jun (8)
jun (2)


console.log ("\n --- Batas --- \n")
