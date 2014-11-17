'''
Created on 05-11-2014

@author: Latino
'''
import math

class Zespolona:
    def __init__(self,r,u):
        self.r=r
        self.u=u
    def get_r(self):
        return self.__r
    def set_r(self,r):
        self.__r=r
    def get_u(self):
        return self.__u
    def set_u(self,u):
        self.__u=u
    def __str__(self):
        return "zespolona = "+str(self.r)+" + "+str(self.u)+"i"
    
    def modul2(self): 
        return "modul liczby = "+str(math.sqrt(self.r**2+self.u**2))
    
    def dodaj_zespolona2(self,z2): 
        nowar=self.r+z2.r;
        nowau=self.u+z2.u;
        return "wynik dodawania = "+str(nowar)+" + "+str(nowau)+"i"
    
    def odejmij_zespolona2(self,z2): 
        nowar=self.r-z2.r;
        nowau=self.u-z2.u;
        return "wynik odejmowania = "+str(nowar)+" + "+str(nowau)+"i"

z1 = Zespolona(2,3)
z2 = Zespolona(1,3)
print str(z1)
print z1.modul2()
print z1.dodaj_zespolona2(z2)
print z1.odejmij_zespolona2(z2)