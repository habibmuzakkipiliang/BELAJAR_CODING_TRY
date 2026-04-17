// Program Kartu Ucapan

console.log ("Program Kartu Ucapan \n")

var raya = prompt ("Hari raya apa : ")
var kata_tambahan = prompt ("Kata Tambahan :")
var tahun = Number (prompt("Tahun berapa : "))
var nama = prompt ("Nama kamu siapa : ")
var panggil = prompt ("Nama panggilan apa : ")
var kelas = prompt ("Dari kelas apa : ")
var asal = prompt ("Asal daerah apa : ")
var marga = prompt ("Marga nya apa : ")
var suku = prompt ("Suku apa : ")
var fans = prompt ("Kamu ngefans siapa : ")
var oshi = prompt ("Kamu oshi nya siapa : ")


var ucapan = ` \n Selamat ${raya} ${tahun}, ${kata_tambahan}

Salam dari :

- Nama    : ${nama}
- Panggil : ${panggil}
- Kelas   : ${kelas}
- Asal    : ${asal}
- Marga   : ${marga}
- Suku    : ${suku}
- Fans    : ${fans}
- Oshi    : ${oshi}

`

console.log (ucapan)