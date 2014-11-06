'''
Created on 05-11-2014

@author: Latino
'''
plik=open("menu_restauracji.txt","r")

menu={}
wyrazy = plik.read()
wyrazy = str(wyrazy)
wyrazy = wyrazy.replace("zl", " - ")
wyrazy = wyrazy.replace("\n", "")
wyrazy = wyrazy.split(" - ")
a=len(wyrazy)
del wyrazy[a-1]
aa=0

while aa<a-2:
    menu[wyrazy[aa]]=float(wyrazy[aa+1])
    aa=aa+2   
    
def kasa(zamowienie):
    cena = 0
    napiwek = 0
    for i in zamowienie:
        if i in menu:
            cena+=menu[i]
        napiwek = 0.2*cena
    print "Naleznosc: "+str(cena)+"zl     napiwek: "+str(napiwek)+"zl"
    return 0


kasa(["kapusta","zupa","czekolada"])
kasa(["kurczak","zupa"])

#print menu

plik.close()
