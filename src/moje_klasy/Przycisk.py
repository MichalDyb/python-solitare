#Klasa przechowujaca wymiary i pozycje przycisku, a także umożliwia sprawdzenie, czy kursor zostal na nim umieszczony
class Przycisk:
    #Zmienne przechowujace rozmiar przycisku
    szerokosc = 0
    wysokosc = 0
    #Zmienne przechowujace pozycje przycisku
    x = 0
    y = 0
    #Konstruktor pobierajacy argumenty
    def Przycisk(self, szerokosc = 0, wysokosc = 0, x = 0, y = 0):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.x = x
        self.y = y
    #Funkcja zwracajaca prawde, gdy kursor znajduje sie na przycisku
    def zaznaczony(self, pozycja):
        if pozycja[0] > self.x and pozycja[0] < self.x + self.szerokosc:
            if pozycja[1] > self.y and pozycja[1] < self.y + self.wysokosc:
                return True
        return False
    #Funkcja zwracajaca prawde, gdy kursor znajduje sie tylko na jednej karcie
    def zaznaczona_karta(self, pozycja):
        if pozycja[0] > self.x and pozycja[0] < self.x + self.szerokosc:
            if pozycja[1] > self.y and pozycja[1] < self.y + int(self.wysokosc * 0.175):
                return True
        return False
    #Funkcja zwracajaca prawde, gdy inny przycisk znajduje sie na przycisku
    def najechany(self, pozycja):
        if pozycja[0] > self.x - int(self.szerokosc * 0.75) and pozycja[0] < self.x + int(self.szerokosc * 0.75):
            if pozycja[1] > self.y - self.wysokosc and pozycja[1] < self.y + self.wysokosc:
                return True
        return False
