// Input Data formulir sederhana Logika Kuliah SNBT dan UM PTKIN dan Beasiswa Full dan Bootcamp dan Kursus IT


console.log ("\n Input Data formulir sederhana Logika Kuliah SNBT dan UM PTKIN dan Beasiswa Full dan Bootcamp dan Kursus IT \n")


var nama = prompt ("Masukkan nama kamu : ")
var kelas = prompt ("Masukkan kelas kamu : ")
var absen = Number (prompt ("Masukkan nomor absen : "))
var sekolah = prompt ("Masukkan sekolah kamu : ")
var tinggi = prompt ("Masukkan tinggi badan kamu : ")
var berat = prompt ("Masukkan berat badan kamu : ")
var ujian = prompt ("Lokasi ujian SNBT : ")




var profil = ` 

- Nama         : ${nama}
- Kelas        : ${kelas}
- Nomor Absen  : ${absen}
- Asal Sekolah : ${sekolah}
- Tinggi badan : ${tinggi}
- Berat badan  : ${berat}
- Ujian SNBT   : ${ujian}


- Terimakasih sudah isi data formulir di pelayanan kami

- Nikmati hidup kamu dengan tenang dan damai

`

console.log (profil)


console.log ("\n --- Batas --- \n")




console.log ("\n Logic masuk kuliah saat SNBT (Control Flow Ledder Logic) \n")


var hasil = Number (prompt ("Masukkan data kamu (HASIL SNBT) : "))


if (hasil >= 90) {
    console.log (`Lulus dong,  berarti boleh kuliah, hasil = ${hasil}`)
}

else if (hasil >= 80) {
    console.log (`Masih aman dong, tetap konsisten, hasil = ${hasil}`)
}

else if (hasil >= 70) {
    console.log (`Tenang aja, masih ada jalur lain misalnya UM PTKIN dan Beasiswa IT lainnya, hasil = ${hasil}`)
}

else if (hasil >= 60) {
    console.log (`Semangat dong, masih ada jalur lain lagi dong, hasil = ${hasil}`)
}

else if (hasil >= 20) {
    console.log (`Sabar dan tenang, tapi masih ada jalur dan jalan lain dengan dibarengi usaha, hasil = ${hasil}`)
}

else if (hasil >= 10) {
    console.log (`Ikut Bootcamp dan Beasiswa IT Swasta aja, hasil = ${hasil}`)
}

else {
    console.log (`Gap year tahun depan, hasil = ${hasil}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Ulang Kata biar semangat dong (For Looping) \n")


var kata = prompt ("Masukkan kata kamu yang bikin semangat ya : ")


for (a = 0; a < 50; a++) {
    console.log (`${a + 1}, ${kata}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Hitung Angka Random sampai berapa (While Looping) \n")


var b = Number (prompt ("Masukkan angka random : "))


while (b < 15) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")
