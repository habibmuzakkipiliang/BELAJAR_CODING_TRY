class JKT48:
    
    def __init__(self, nama, team):
        self.nama = nama
        self.team = team
        
        
    def aksi (self):
        print (f"- {self.nama} dan Tim : {self.team}")

        
hasil_1 = JKT48 ("Michie", "Love")
hasil_2 = JKT48 ("Gracie", "Love")


hasil_1.aksi ()
hasil_2.aksi ()