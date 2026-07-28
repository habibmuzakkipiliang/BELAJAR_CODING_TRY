class Negara:
     
     def __init__(self, negara, ibukota):
          self.negara = negara
          self.ibukota = ibukota
          
     def out (self):
          print (f"- {self.negara}, {self.ibukota}")  
          
hasil_1 = Negara ("Indonesia", "Jakarta")
hasil_2 = Negara ("Malaysia", "Kuala Lumpur")
hasil_3 = Negara ("Singapura", "Singapura")
hasil_4 = Negara ("Filipina", "Manila")
hasil_5 = Negara ("Thailand", "Bangkok")

hasil_1.out ()
hasil_2.out ()
hasil_3.out ()
hasil_4.out ()
hasil_5.out ()


