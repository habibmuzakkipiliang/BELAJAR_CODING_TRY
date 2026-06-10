# Objek data 4 Kitab Allah SWT yang harus diyakini Umat Islam


print ("\n Objek data 4 Kitab Allah SWT yang harus diyakini Umat Islam \n")


data = {
    
    "taurat" : {
        "deskripsi" : "Kitab ini merupakan wahyu pertama yang diturunkan dalam deretan empat kitab utama ini.",
        "penerima" : "Nabi Musa",
        "waktu_turun" : "Abad ke - 12 SM",
        "bahasa" : "Ibrani",
        "tujuan" : "Diturunkan untuk Bani Israil agar mereka tetap berada di jalan yang benar sesuai perintah Allah.",
        "isi_pokok" : "Mengandung hukum-hukum syariat dan kepercayaan yang benar, yang dikenal juga dengan The Ten Commandments (Sepuluh Perintah Allah).",
    },
    
    
    "zabur" : {
        "deskripsi" : "Kitab Zabur diturunkan setelah masa Nabi Musa, sebagai nyanyian pujian kepada Allah",
        "penerima" : "Nabi Daud",
        "waktu_turun" : "Abad ke - 10 SM",
        "tujuan" : "Menjadi pedoman bagi umat Nabi Daud (Bani Israil).",
        "isi_pokok" : "Berisi kumpulan doa, zikir, nasihat, dan hikmah. Berbeda dengan Taurat, Zabur tidak mengandung hukum syariat baru, melainkan mengikuti syariat Nabi Musa.",
    },
    
    "injil" : {
        "deskripsi" : "Kitab ini membawa kabar gembira mengenai kasih sayang Allah dan kedatangan rasul terakhir.",
        "penerima" : "Nabi ISA",
        "waktu_turun" : "Abad ke-1 M.",
        "bahasa" : "Suryani (Aram), Yunani, dan Latin",
        "tujuan" : "Menjadi pedoman bagi kaum Nasrani (Bani Israil pada masa itu).",
        "isi_pokok" : "Ajakan untuk hidup zuhud (tidak mengagungkan dunia), membersihkan jiwa, serta membenarkan ajaran dalam kitab-kitab sebelumnya sekaligus menghapus beberapa hukum di Taurat yang sudah tidak sesuai.",
        "injil_utama_modern" : "Matius, Johannes, Markus, Lukas",
    },
    
    
    "al-quran" : {
        "deskripsi" : "Kitab suci terakhir yang berfungsi sebagai penyempurna dan penjaga seluruh kitab sebelumnya",
        "penerima" : "Nabi Muhammad SAW.",
        "waktu_turun" : "Abad ke-7 M (610–632 M).",
        "tujuan" : "Untuk seluruh umat manusia hingga akhir zaman (Rahmatan lil 'Alamin).",
        "isi_pokok" : "Mencakup seluruh aspek kehidupan, mulai dari tauhid, ibadah, muamalah, akhlak, hukum, sejarah, hingga ilmu pengetahuan. Al-Qur'an adalah mukjizat terbesar yang keasliannya dijamin oleh Allah SWT hingga hari kiamat",
    },
}


for kitab, detail in data.items():
    
    print ("\n ------- \n")
    
    print ("\n Kitab        :", kitab);
    
    print ("\n Deskripsi    :",  detail ["deskripsi"])
    
    print ("\n Penerima     :", detail ["penerima"])
    
    print ("\n Waktu turun  :", detail ["waktu_turun"])

    print ("\n Tujuan       :", detail ["tujuan"])
    
    print ("\n Isi pokok    :", detail ["isi_pokok"])
    
    
    if detail.get ("injil_utama_modern"):
        print ("\n Kitab Utama :", detail ["injil_utama_modern"])