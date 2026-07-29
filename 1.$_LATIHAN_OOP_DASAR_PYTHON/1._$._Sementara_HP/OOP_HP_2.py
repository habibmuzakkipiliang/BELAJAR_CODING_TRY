class Home:
    
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
        
        
    def out (self):
        print (f"- Rumah {self.nama} berwarna {self.warna}")
        
        
hasil_1 = Home ("Habib", "Oren")

hasil_2 = Home ("Raff", "Kuning")


hasil_1.out ()
hasil_2.out ()