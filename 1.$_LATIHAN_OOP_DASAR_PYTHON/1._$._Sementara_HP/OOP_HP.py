class Kucing:
    
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
        
        
    def out (self):
        print (f"- Kucing {self.nama}, dan berwarna {self.warna}")
        
        
kucing_1 = Kucing ("Ivan", "Putih")

kucing_2 = Kucing ("Rafa", "Hitam")


kucing_1.out ()
kucing_2.out ()