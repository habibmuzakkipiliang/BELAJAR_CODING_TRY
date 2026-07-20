class TeamLove:  
     
     def __init__(self, nama, usia):
          self.nama = nama
          self.usia = usia
        
     def aksi (self):
          print (f"- {self.nama} dan berusia {self.usia}")
              
team_1 = TeamLove ("Gracie JKT48", 18)
team_2 = TeamLove ("Michie JKT49", 17)
team_3 = TeamLove ("Lily JKT48", 18)
team_4 = TeamLove ("Lana JKT48", 19)
team_5 = TeamLove ("Fiony JKT48", 24)
team_6 = TeamLove ("Anin", 20)

team_1.aksi ()
team_2.aksi ()
team_3.aksi ()
team_4.aksi ()
team_5.aksi ()
team_6.aksi ()