console.log ("\n Profil Nabi Muhammad SAW \n")


var nama = "Nabi Muhammad (Ahmad)"
var hari_lahir = "Hari Subuh Senin"
var tanggal_lahir = "12 Rabbiul Awal / Tahun Gajah / 20 April 571 Masehi"
var ayah = "Abdullah"
var ibu = "Aminah"
var kakek = "Abdul Muthalib"
var masa_kecil = "Penggembala"
var masa_remaja = "Pedagang"
var status = "Yatim Piatu"


console.log ("Nama :", nama)
console.log ("Hari Lahir :", hari_lahir)
console.log ("Tanggal lahir :", tanggal_lahir)
console.log ("Nama Ayah :", ayah)
console.log ("Nama Ibu :", ibu)
console.log ("Nama kakek :", kakek)
console.log ("Masa kecil :", masa_kecil)
console.log ("Masa remaja :", masa_remaja)
console.log ("Status :", status)




// Menggunakan List untuk menyimpan kronologi

var sejarah = [
    "- 2 Bulan dikandungan, ayahnya meninggal",
    "- Umur 6 tahun, ibunya wafat",
    "- Umur 8 tahun, kakeknya wafat",
    "- Umur 25 tahun, menikah dengan Khadijah",
    "- Umur 30 tahun, mempersatukan bangsa pada peristiwa peletakan batu Hajar Aswad",
    "- Umur 40 tahun, diangkat menjadi Rasul",
    "- Umur 63 tahun, wafat di Madinah Al Munawwarah, pada senin, 12 Rabbiul Awal tahun 11 Hijriah, 8 Juni 632 Masehi"
]

console.log ("\n--- Garis Waktu Perjalanan Hidup --- \n")


// Menggunakan loop agar tidak perlu mengetik print berkali-kali



for (poin = 0; poin < sejarah.length; poin++) {
    console.log (sejarah [poin])
}