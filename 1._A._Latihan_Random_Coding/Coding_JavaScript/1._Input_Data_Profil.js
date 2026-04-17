// Input Data Profil dalam Program Sederhana di JavaScript


console.log ("\n Input Data Profil dalam Program Sederhana di JavaScript \n")


var nama = prompt ("Masukkan nama : ")
var kelas = prompt ("Masukkan kelas :")
var absen = Number (prompt ("Masukkan nomor absen :"))
var sekolah = prompt ("Masukkan sekolah :")
var tinggi = prompt ("Masukkan tinggi badan :")
var berat =  prompt ("Masukkan berat badan :")
var coding = prompt ("Masukkan coding kamu : ")
var lomba = prompt ("Masukkan lomba yang pernah kamu ikuti : ")
var darah = prompt ("Masukkan golongan darah kamu : ")
var hobi = prompt ("Masukkan hobi kamu : ")


var detail = `

- Nama           : ${nama}
- Kelas          : ${kelas}
- Nomor Absen    : ${absen}
- Sekolah        : ${sekolah}
- Tinggi Badan   : ${tinggi}
- Berat Badan    : ${berat}
- Coding         : ${coding}
- Lomba          : ${lomba}
- Golongan darah : ${darah}
- Hobi           : ${hobi}

`

console.log (detail)


console.log ("\n --- Batas --- \n")




console.log ("\n Hasil Logika Sederhana \n")


var hasil = Number (prompt ("Masukkan logic 1 : ")) 


if (hasil > 80) {
    console.log (`Lulus dong, skor = ${hasil}`)
}

else if (hasil < 50) {
    console.log (`Belum dong, skor = ${hasil}`)
}

else {
    console.log (`Jangan dulu, skor = ${hasil}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Hasil Logika 1 \n")


var logic = Number (prompt ("Masukkan logic 2 : "))


if (logic > 5) {
    console.log (`Oke dong, logic = ${logic}`)
}

else {
    console.log (`Belum dong, logic = ${logic}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Logika Rapor Sederhana \n")


var rapor = Number (prompt ("Masukkan nilai rapor : "))


if (rapor >= 90) {
    console.log (`A, skor = ${rapor}`)
}

else if (rapor >= 80) {
    console.log (`B, skor = ${rapor}`)
}

else if (rapor >= 70) {
    console.log (`C, skor = ${rapor}`)
}

else if (rapor >= 60) {
    console.log (`D, skor = ${rapor}`)
}

else if (rapor >= 50) {
    console.log (`E, skor = ${rapor}`)
}

else if (rapor >= 40) {
    console.log (`F, skor = ${rapor}`)
}

else {
    console.log (`Jelek amat, skor = ${rapor}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested \n")


var tes = Number (prompt ("Masukkan tes 1 :"))
var cek = true

if (cek) {
    if (tes > 5) {
        console.log (`Oke, tes = ${tes}`)
    }
    
    else {
        console.log (`Belum boleh dong, tes = ${tes}`)
    }
}

else {
    console.log (`Jangan dulu dong, tes = ${tes}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Pendaftaran join JKT48 \n")


var usia = Number (prompt ("Masukkan usia kamu untuk Join JKT48 : "))
var cek = true


if (cek) {
    if ((usia >= 13) && (usia <= 19)) {
        console.log (`Boleh join JKT48, usia = ${usia}`)
    }
    
    else if (usia > 19) {
        console.log (`Sudah lebih dari cukup untuk join JKT48, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum boleh ikut join JKT48, usia = ${usia}`)
    }
}

else {
    console.log (`Gak lolos join JKT48, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Usia Produktif Manusia \n")


var usia = Number (prompt ("Masukkan usia kamu : "))
var cek = true


if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Usia produktif manusia, usia = ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah tua, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum masuk usia produktif, usia = ${usia}`)
    }
}

else {
    console.log (`Masih kecil usianya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar \n")


for (a = 0; a < 11; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




for (b = 0; b < 11; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")




for (c = 0; c < 11; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar \n")


var a = 5

while (a < 11) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




var b = 10

while (b < 16) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")




var c = 15

while (c < 21) {
    console.log (`Urutan ke - ${c}`)
    c++
}


console.log ("\n --- Batas --- \n")
