class Member:
     
     def __init__(self, nama, asal, usia):
          self.nama = nama
          self.asal = asal
          self.usia = usia
                  
     def data (self):
          print (f"- {self.nama}, dan berasal dari {self.asal}, dan berusia {self.usia}")
                
jkt48_1 = Member ("Christy JKT48", "Jakarta", "26")
jkt48_2 = Member ("Gracie JKT48", "Jakarta", "18")
jkt48_3 = Member ("Michie JKT48", "Palembang", "17")

jkt48_1.data ()
jkt48_2.data ()
jkt48_3.data ()