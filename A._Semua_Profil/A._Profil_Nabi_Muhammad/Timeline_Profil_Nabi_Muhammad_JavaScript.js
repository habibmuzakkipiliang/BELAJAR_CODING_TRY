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