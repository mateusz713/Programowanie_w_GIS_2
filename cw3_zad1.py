'''
Created on 05-11-2014

@author: Latino
'''
plik=open("dane.txt","r")
plik2=open("statystyki.txt","a")

wyrazy = plik.read()
wyrazy = str(wyrazy)
wyrazy = wyrazy.replace(".", " ")
wyrazy = wyrazy.replace(",", " ")
wyrazy = wyrazy.replace("\n", " ")
wyrazy = wyrazy.replace("  ", " ")
wyrazy = wyrazy.split(" ")
niepowtarzalne = list(set(wyrazy))
wynik = []

for i in niepowtarzalne:
    krotka = (wyrazy.count(i), i)
    wynik.append(krotka)

wynik.sort()
wynik = wynik[::-1]

plik2.writelines("Liczba wystapien wyrazu:\n");
plik2.writelines("\n");
for i in wynik:
    plik2.writelines(str(i)+"\n");

plik2.writelines("\n");
print "Wyniki dzialania w pliku statystyki :)"
plik.close()
plik2.close()