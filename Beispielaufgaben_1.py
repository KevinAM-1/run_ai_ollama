


class Doctor: 
    def __init__(self):
        super().__init__()
        
    def paperwork(self):
        try:
            super().paperwork()
            print("Signature Doctor")
        except AttributeError:
            print("Does Paperwork (Doctor)")
            print("Signature Doctor")
        
class Assistent:
    def __init__(self):
        super().__init__()
        
    def paperwork(self):
        print("Does Paperwork (Assistent)")
        
class DoctorsOffice:
    def __init__(self):
        self.doctor = Doctor()
        self.assistent = Assistent()
    
    def paperwork(self):
        self.doctor.paperwork()
        
do = DoctorsOffice()
do.paperwork()



