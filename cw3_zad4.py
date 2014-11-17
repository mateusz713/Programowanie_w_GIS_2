'''
Created on 05-11-2014

@author: Latino
'''
class Wojownik:
    def __init__(self,imie,nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko
    def get_imie(self):
        return self.__imie
    def set_imie(self,imie):
        self.__imie=imie
    def get_nazwisko(self):
        return self.__nazwisko
    def set_nazwisko(self,nazwisko):
        self.__nazwisko=nazwisko
    def podaj_imie(self):
        print "Jestem "+self.imie+" "+self.nazwisko+" wojownik z woli Pana!"
        

class Rycerz(Wojownik):
    def __init__(self,imie,nazwisko,status):
        Wojownik.__init__(self, imie, nazwisko)
        self.status=status
    def podaj_imie(self):
        print "Jam jest "+self.status+" "+self.imie+" "+self.nazwisko+" rycerz z woli Pana!"
    def bij_wroga(self):
        print "Bic psubraty!"
        
class Sad:
    def podaj_wyrok(self):
        print "skazuje Cie niegodziwcze!" 
        
class Paladyn(Rycerz, Sad):
    pass
        
class Lucznik(Wojownik):
    def __init__(self,imie,nazwisko):
        Wojownik.__init__(self,imie,nazwisko)
    def podaj_imie(self):
        print "Jestem "+self.imie+" "+self.nazwisko+" lucznik"
    def przygotuj_orez(self):
        print "Naciagac cieciwe!" 
    def bij_wroga(self):
        print "Strzelam!"


zbyszko = Wojownik("Zbyszek", "Silnoreki")
zbyszko.podaj_imie()
zbyszko2 = Rycerz("Zbych", "Szybkonogi","Szlachcic")
zbyszko2.podaj_imie()
zbyszko3 = Paladyn("Zbychu", "Wielki","Paladyn")
zbyszko3.podaj_imie()
zbyszko3.podaj_wyrok()
