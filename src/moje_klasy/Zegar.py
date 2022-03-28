#Zaimportowanie biblioteki pygame
import pygame
#Klasa pełniąca rolę zegara dla rozgrywki
class Zegar:
    sekundy = 0
    sekundy_poprzednie = 0
    wlaczony = False
    stoper = pygame.time.Clock()
    #Funkcja uruchamiajaca licznik z wartoscia 0
    def uruchom_odnowa(self):
        self.sekundy = 0
        self.sekundy_poprzednie = 0
        self.stoper.tick()
        self.wlaczony = False
    #Funkcja urchamiajaca licznik z liczba sekund podana jako argument
    def uruchom_czas(self, czas):
        self.sekundy = czas
        self.sekundy_poprzednie = czas
        self.stoper.tick()
        self.wlaczony = False
    #Funkcja pauzujaca licznik
    def pauza(self):
        self.sekundy_poprzednie = self.sekundy
        self.wlaczony = False
    #Funkcja uruchamiajaca licznik z wartoscia poprzednio zapisana
    def start(self):
        if self.wlaczony == False:
            self.sekundy = self.sekundy_poprzednie
            self.stoper.tick()
            self.wlaczony = True
    #Zwraca czas w formacie minuty:sekundy
    def pobierz_czas(self):
        czas = 0
        self.sekundy += self.stoper.tick() / 1000.0
        if self.wlaczony:
            czas = self.sekundy
        else:
            czas = self.sekundy_poprzednie
        minuty = int(czas / 60)
        sekundy = int(czas) - minuty * 60
        if minuty < 10:
            minuty = "0" + str(minuty)
        else:
            minuty = str(minuty)
        if sekundy < 10:
            sekundy = "0" + str(sekundy)
        else:
            sekundy = str(sekundy)
        czas = minuty + ":" + sekundy
        return czas
    #Funkcja zwracajaca ilosc sekund
    def pobierz_sekundy(self):
        self.sekundy += self.stoper.tick() / 1000.0
        return int(self.sekundy)
    #Funkcja podejmij decyzje, Zwracajaca true jeśli sekundy w zegarze sa wieksze lub rowne od sekund podanych jako argument, i ustawiajaca wartosc zegara na 0
    #zapewnia to podejmowanie decyzji co okresloną ilość czasu
    def podejmij_decyzje(self, sekundy):
        self.sekundy += self.stoper.tick() / 1000.0
        if self.sekundy >= sekundy:
            self.sekundy = 0
            return True
        return False