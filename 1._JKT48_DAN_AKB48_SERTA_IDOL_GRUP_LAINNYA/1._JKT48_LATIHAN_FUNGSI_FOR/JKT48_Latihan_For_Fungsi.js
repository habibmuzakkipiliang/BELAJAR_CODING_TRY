// Latihan Fungsi dengan contoh kasus beragam seperti JKT48, agar gak mudah bosan sama sekali 


function main () {
    
    console.log ("\n Latihan Fungsi dengan contoh kasus beragam seperti JKT48, agar gak mudah bosan sama sekali \n")
    
    
    console.log ("\n 20 Top Member JKT48 paling populer di Indonesia tahun 2026 \n")
    
    
    var jkt48 = [
        
       "1. Feni Fitriyanti",
       "2. Fiony Alveria",
       "3. Freya Jayawardhana", 
       "4. Angelina Christy (Christy)", 
       "5. Jessica Chandra (Jessi)",
       "6. Marsha Lenathea",
       "7. Gita Sekar Andarini",
       "8. Mutiara Azzahra (Muthe)",
       "9. Kathrina Irene (Atin)",
       "10. Lulu Salsabila",
       "11. Greesella Adhalia (Greesel)",
       "12. Indah Cahya",
       "13. Cornelia Vanisa (Oniel)",
       "14. Aurellia (Lia)",
       "15. Fritzy Rosmerian",
       "16. Michelle Alexandra (Michie)",
       "17. Helisma Putri (Eli)",
       "18. Cathleen Hana Nixie (Cathy)",
       "19. Febriolla Sinambela (Olla)",
       "20. Gracie Octaviani (Gracie)", 
       
        
    ]
    
    
    for (a = 0; a < jkt48.length; a++) {
        console.log (jkt48 [a])
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Pakai Var 
    
    console.log ("\n Pakai Var \n")
    
    var teks = "ini teks"
    var angka = 34
    var desimal = 45.35
    var cek = true
    
    
    console.log ("Teks :", teks)
    console.log ("Angka :", angka)
    console.log ("Desimal :", desimal)
    console.log ("Cek :", cek)
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Pakai Const 
    
    console.log ("\n Pakai Const \n")
    
    const teks_a = "ini teks"
    const angka_a = 34
    const desimal_a = 45.35
    const cek_a = true
    
    
    console.log ("Teks a :", teks_a)
    console.log ("Angka a :", angka_a)
    console.log ("Desimal a :", desimal_a)
    console.log ("Cek a :", cek_a)
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Pakai Let 
    
    console.log ("\n Pakai Let \n")
    
    
    let teks_b = "ini teks"
    let angka_b = 34
    let desimal_b = 45.35
    let cek_b = true 
    
    
    console.log ("Teks b :", teks_b)
    console.log ("Angka b :", angka_b)
    console.log ("Desimal b :", desimal_b)
    console.log ("Cek b :", cek_b)
    
    
    console.log ("\n --- Batas --- \n")




    // Tipe data dasar

    var teks = "Halo Tes"
    var angka = 23
    var desimal = 34.32
    var cek_1 = true
    var cek_2 = false
    var list = [1, 2, 3, 4, 5, 6, 7, 8]

    console.log ("Teks =", teks)
    console.log ("Angka =", angka)
    console.log ("Desimal =", desimal)
    console.log ("Cek 1 =", cek_1)
    console.log ("Cek 2 =", cek_2)
    console.log ("List =", list)


    console.log ("\n --- Batas --- \n")
    



    // Membedakan Var, let dan Const 

    console.log ("\n Membedakan Var, Let dan Const \n")


    console.log ("\n Pake Var \n")


    var teks_x = "Halo Teks"
    var angka_x = 12
    var desimal_x = 34.3
    var cek_x = true
    var cek_x = false
    

    console.log ("Teks =", teks_x)
    console.log ("Angka =", angka_x)
    console.log ("Desimal =", desimal_x)
    console.log ("Cek K =", cek_x)
    console.log ("Cek M =", cek_x)
    

    console.log ("\n --- Batas --- \n")



    // Pake let

    console.log ("\n Pake Let \n")


    let teks_s = "Halo Teks"
    let angka_s = 12
    let desimal_s = 34.3
    let cek_s = true
    let cek_3 = false

    
    console.log ("Teks S =", teks_s)
    console.log ("Angka S =", angka_s)
    console.log ("Desimal S =", desimal_s)
    console.log ("Cek S =", cek_s)
    console.log ("Cek 3 =", cek_3)


    console.log ("\n --- Batas --- \n")




    // Pake Const

    console.log ("\n Pake Const \n")


    const teks_e = "Halo Teks"
    const angka_e = 12
    const desimal_e = 34.3
    const cek_e = true
    const cek_ek = false


    console.log ("Teks E =", teks_e)
    console.log ("Angka E =", angka_e)
    console.log ("Desimal E =", desimal_e)
    console.log ("Cek E =", cek_e)
    console.log ("Cek EK =", cek_ek)


    console.log ("\n --- Batas --- \n")
    

    
    
    // Manipulasi String 
    
    
    console.log ("\n Manipulasi String \n")
    
    
    var tulis = "JKT48"
    
    console.log (`Halo anak ${tulis}`)
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    var tes = "Freya JKT48"
    
    console.log (`Halo kapten ${tes}`)
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    var center = "Fiony JKT48"
    
    console.log (`Halo center ${center}`)
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    var manajer = "Melody Laksani"
    
    console.log (`Halo manajer umum JKT48 ${manajer}`)
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    var wakil = "Shani Indira Natio"
    
    console.log (`Halo wakil manajer umum JKT48 ${wakil}`)
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // For dasar
    
    console.log ("\n For dasar \n")
    
    
    for (a = 0; a < 10; a++) {
        console.log ("a", a)
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // While dasar 
    
    console.log ("\n While dasar \n")
    
    
    var a = 5
    
    while (a < 10) {
        console.log ("a", a)
        a++ 
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Do While dasar
    
    console.log ("\n Do While dasar \n")
    
    
    var a = 3
    
    do {
        console.log ("a", a)
        a++
    } while (a < 10)
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // For nested 
    
    console.log ("\n For Nested \n")
    
    
    for (a = 0; a < 2; a++) {
        for (b = 0; b < 4; b++) {
            console.log ("a", a, "b", b)
        }
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Percabangan Dasar
    
    console.log ("\n Percabangan dasar \n")
    
    
    var a = 3
    
    if (a > 5) {
        console.log ("Bagus")
    }
    
    else {
        console.log ("Kecil")
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Percabangan Nested 1
    
    console.log ("\n Percabangan Nested 1 \n")
    
    
    var member = 9
    var cek = true
    
    if (member > 7) {
        if (cek) {
            console.log ("Iya, lulus dan jadi anggota tetap JKT48")
        }
        
    else if (member < 5) {
            console.log ("Iya, turun jadi Trainee JKT48")
        }
    } 
    
    else {
        console.log ("Gak lulus sama sekali")
    }
    
    
    console.log ("\n --- Batas --- \n")
    
    
    
    
    // Switch Case
    
    console.log ("\n Switch Case \n")
    
    
    var kondisi = 2
    
    switch (kondisi) {
        
        case 1:
            console.log ("Laper banget")
            break
            
        case 2:
            console.log ("Laper dikit")
            break
            
        case 3:
            console.log ("Laper biasa")
            break
            
        case 4:
            console.log ("Kenyang biasa")
            break
            
        case 5:
            console.log ("Kenyang dikit")
            break
            
        case 6:
            console.log ("Kenyang banget")
            break
            
        default:
        console.log ("Biasa aja deh")
        
    }
    
    
    console.log ("\n --- Batas --- \n")
    
}

main ()




function profil () {
    
    // Profil JKT48 
    
    
    console.log ("\n Profil JKT48 \n")
    
    
    var data = {
        
        "nama_grup" : "JKT48",
        "asal_negara" : "Indonesia",
        "pendiri" : "Yasushi Akimoto",
        "berdiri_tahun" : "2011",
        "berdiri_bulan" : "17 Desember",
        "era_sekarang" : "JKT48 FIGHT",
        "kapten_jkt48" : "Freya JKT48 (gen 7)",
        "manajer_jkt48" : "Melody Laksani (Eks Kapten JKT48 gen 1)",
        "wakil_manajer_jkt48" : "Shani Indira Natio (Eks Kapten JKT48 gen 3)",
    }
    
    
    console.log ("Nama grup :", data ["nama_grup"])
    
    console.log ("Asal negara :", data ["asal_negara"])
    
    console.log ("Pendiri :", data ["pendiri"])
    
    console.log ("Berdiri tahun :", data ["berdiri_tahun"])
    
    console.log ("Berdiri bulan :", data ["berdiri_bulan"])
    
    console.log ("Era sekarang :", data ["era_sekarang"])
    
    console.log ("Kapten JKT48 :", data ["kapten_jkt48"])
    
    console.log ("Manajer JKT48 :", data ["manajer_jkt48"])
    
    console.log ("Wakil manager JKT48 :", data ["wakil_manajer_jkt48"])
    
    
    console.log  ("\n --- Batas --- \n")
    
    
}

profil ()




// Fungsi dasar

console.log ("\n Fungsi dasar \n")


function dasar () {
    console.log ("Hello Dapeng")
}

dasar ()


console.log ("\n --- Batas --- \n")





// Fungsi dasar 2

console.log ("\n Fungsi dasar 2 \n")


function dust () {
    console.log ("Hello Dun")
}

dust ()
dust ()
dust ()
dust ()


console.log ("\n --- Batas --- \n")




// Fungsi dasar 3

console.log ("\n Fungsi dasar 3 \n")


function der () {
    console.log ("Hello Arif")
    console.log ("Hello Hayyan")
    console.log ("Hello Jansen")
    console.log ("Hello Yusuf")
}

der ()


console.log  ("\n --- Batas --- \n")




// Fungsi dengan parameter

console.log ("\n Fungsi dengan parameter \n")


function unter (nama) {
    console.log ("Hello " + nama)
}

unter ("JKT48 Mantap Jiwa Guys")
unter ("JKT48 Early")
unter ("JKT48 Golden Era")
unter ("JKT48 New Era")
unter ("JKT48 Fight")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan parameter 1 \n")


function fos (nama) {
    console.log ("Hello " + nama)
}

fos ("AKB48")
fos ("JKT48")
fos ("KLP48")
fos ("MNL48")
fos ("Quadlips")
fos ("BNK48")
fos ("TSH48")
fos ("TPE48")
fos ("CGM48")
fos ("Raintree Non Grup 48")
 
 
console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan parameter 2 \n")


function det (nama) {
    console.log ("Hello " + nama)
    console.log ("Hello " + nama)
    console.log ("Hello " + nama)
    console.log ("Hello " + nama)
    console.log ("Hello " + nama)
}

det ("Python")
det ("JavaScript")
det ("Java")
det ("C#")
det ("C++ / C")
det ("Dart (Flutter)")
det ("PHP")

console.log ("\n --- Batas --- \n")




// Fungsi dengan return

console.log ("\n Fungsi dengan return \n")


function tambah (a, b) {
    return a + b
}

var hasil = tambah (10, 10)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




function kurang (e, d) {
    return e - d
}

var hasil = kurang (20, 5)
console.log ("Kurang =", hasil)


console.log ("\n --- Batas --- \n")




function kali (r, t) {
    return r * t
}

var hasil = kali (10, 10)
console.log ("Kali =", hasil)


console.log ("\n --- Batas --- \n")




function pangkat (k, l) {
    return k ** l
}

var hasil = pangkat (10, 3)
console.log ("Pangkat =", hasil)


console.log ("\n --- Batas --- \n")




function bagi (k, n) {
    return k / n
}

var hasil = bagi (10, 5)
console.log ("Bagi =", hasil)


console.log  ("\n --- Batas --- \n")




function modulus (x, y) {
    return x % y
}

var hasil = modulus (10, 3)
console.log ("Modulus =", hasil)