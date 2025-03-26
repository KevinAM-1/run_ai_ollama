

### Aufgabe 2 - Dependency injection

Folgenden sind 3 Klassen , die den Arbeitsablauf in einer Arztpraxis (`DoctorsOffice`) modellieren. Verändern Sie die Klassen `Doctor` und `Assistent` nicht. 
Wie können Sie dennoch erreichen, dass der Papierkram, den der Arzt gern weitergeben würde, von seinem Assistenten erledigt wird? Jedoch kann nur der Arzt eine Unterschrift ausstellen.
```
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
```


