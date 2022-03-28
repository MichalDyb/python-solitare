#Zaimportowanie biblioteki random
import random

#Klasa tworzaca talie 52 kart
class Talia:
    #Lista przechowujaca karty
    karty = []
    #Funkcja tworzaca talie kart
    def utworztalie(self):
        pik = []
        kier = []
        trefl = []
        karo = []
        for i in range (0, 13):
            pik.append([i, 0, 0])
            kier.append([i, 1, 0])
            trefl.append([i, 2, 0])
            karo.append([i, 3, 0])
        self.karty.clear()
        self.karty.append(pik)
        self.karty.append(kier)
        self.karty.append(trefl)
        self.karty.append(karo)
    #Funkcja losujaca karte z utworzonej tali, w przypadku, gdy pula kart w tali sie wyczerpie zwraca wartosc False
    def losujkarte(self):
        if len(self.karty) == 0:
            return False
        x = random.randrange(0, len(self.karty))
        if len(self.karty[x]) == 0:
            self.karty.pop(x)
            return self.losujkarte()
        y = random.randrange(0, len(self.karty[x]))
        return self.karty[x].pop(y)