#Zaimportowanie biblioteki pygame i klasy przycisk
import pygame
from moje_klasy.Przycisk import *
#Zaimportowanie klasy path z bliblioteki os, zapewnia ona, że ścieżki dostępu do plików będą działały zarówno w systemie unix i windows
from os import path
from sys import exit

#Klasa przechowujaca okno, informacje o dostepnym obszarze roboczym i wyswietlacej menu oraz rozgrywke
class Okno:
    #Zmienna przechowujaca aktualnie wyswietlane okno
    ekran = 0
    #Sprawdza, czy grafiki kart zostaly juz wczytane
    rozgrywka_skalowana = False
    #Zmienne przechowujace rozdzielczosc okna
    szerokosc = 0
    wysokosc = 0
    #Zmienna przechowujaca sciezka do folderu projektu
    sciezka = path.split(path.dirname(__file__))[0]
    #Zmienna przechowujaca sciezka do folderu z grafikami
    sciezka_okno = path.join(path.join(sciezka, "moje_grafiki"), "okno")
    sciezka_karty = path.join(path.join(sciezka, "moje_grafiki"), "karty")
    #Zmienna przechowujaca elementy okna jak grafika, ikona, tlo, opcje itd.
    opis = "Solitare Klondlike"
    ikona = path.join(sciezka_okno, "ikona.png")
    tlo = pygame.image.load(path.join(sciezka_okno, "tlo.png"))
    #Listy przechowujaca grafiki kart i wymiary kart ich przyciski
    baza = []
    baza_przycisk = []
    for i in range(4):
        baza_przycisk.append(Przycisk())
    tyl_przycisk = []
    for i in range(2):
        tyl_przycisk.append(Przycisk())
    karty = []
    karty_przycisk = [] * 4
    for i in range(4):
        karty_przycisk.append([])
        for y in range(13):
            karty_przycisk[i].append(Przycisk())
    robocze_przycisk = []
    for i in range(7):
        robocze_przycisk.append(Przycisk())
    karty_x = 0
    karty_y = 0
    #Lista przechowujaca przyciski menu glownego lub menu rozgrywki
    opcje = []
    for i in range(6):
        opcje.append(Przycisk())
    #Zmienna przechowujaca etykiete okna autora i przycisk powrotu do menu
    autor_etykieta = Przycisk()
    autor_powrot = Przycisk()
    #Zmienne przechowujaca etykiete okna dialogowego i 2 przyciskow opcji oraz i przycisk powrotu
    dialog_etykieta = Przycisk()
    dialog1 = Przycisk()
    dialog2 = Przycisk()
    dialog_powrot = Przycisk()
    #Funkcja tworzaca i wyswietlajaca okno
    def utworz_okno(self):
        #Inicjalizuje wszystkie moduly pygame
        pygame.init()
        #Ustawienie etykiety programu i ikony programu
        pygame.display.set_caption(self.opis)
        pygame.display.set_icon(pygame.image.load(self.ikona))
        #Pobiera rozdzielczosc monitora i zapisuje do pamieci obiektu
        rozdzielczosc = pygame.display.Info()
        self.szerokosc = rozdzielczosc.current_w
        self.wysokosc = rozdzielczosc.current_h
        self.rozgrywka_szerokosc = 0
        self.rozgrywka_wysokosc = 0
        #Tworzy nowe okno i skaluje tlo oraz menu
        self.ekran = pygame.display.set_mode((self.szerokosc - 100, self.wysokosc - 100), pygame.RESIZABLE)
        self.tlo = pygame.transform.scale(self.tlo, (self.szerokosc, self.wysokosc))
        self.skaluj_menu_glowne()
    #Funkcja wylaczajaca okno
    def wylacz_okno(self):
        pygame.display.quit()
        exit(0)
    #Funkcja skalujaca rozmiar okna i zapisujaca nowe wymiary do pamieci obiektu
    def skaluj_okno(self, zdarzenie):
        #Inicjalizuje wszystkie moduly pygame
        pygame.init()
        #Pobiera rozmiar zdarzenia VIDEORESIZE
        self.szerokosc, self.wysokosc = zdarzenie.size
        #Sprawdza czy, wymiary okna nie sa zbyt male.
        if self.szerokosc < 1366:
            self.szerokosc = 1366
        if self.wysokosc < 768:
            self.wysokosc = 768
        #Tworzy nowe okno i skaluje zawartosc
        self.ekran = pygame.display.set_mode((self.szerokosc, self.wysokosc), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.tlo = pygame.transform.scale(self.tlo, (self.szerokosc, self.wysokosc))
    #Funkcja wyswietlajaca tlo
    def wyswietl_tlo(self):
        self.ekran.blit(self.tlo, (0, 0))
    #Funkcja wyswietlajaca obramowanie dla przycisku
    def wyswietl_obramowanie(self, kolor, przycisk, grubosc):
        grubosc = int(przycisk.szerokosc * grubosc * 0.01)
        pygame.draw.line(self.ekran, kolor, (przycisk.x, przycisk.y), (przycisk.x + przycisk.szerokosc, przycisk.y), grubosc)
        pygame.draw.line(self.ekran, kolor, (przycisk.x, przycisk.y + przycisk.wysokosc), (przycisk.x + przycisk.szerokosc, przycisk.y + przycisk.wysokosc), grubosc)
        pygame.draw.line(self.ekran, kolor, (przycisk.x, przycisk.y), (przycisk.x, przycisk.y + przycisk.wysokosc), grubosc)
        pygame.draw.line(self.ekran, kolor, (przycisk.x + przycisk.szerokosc, przycisk.y), (przycisk.x + przycisk.szerokosc, przycisk.y + przycisk.wysokosc), grubosc)
    #Funkcja wyswietlajaca wiadomosc i wysrodkowujaca ja w elemencie
    def wyswietl_wiadomosc(self, kolor, element, wiadomosc, rozmiar, x = 0, y = 0, czcionka = "arial"):
        #Ustala format czcionki
        czcionka = pygame.font.SysFont(czcionka, int(element.wysokosc * 0.09 * rozmiar))
        #Renderuje wiadomosc
        wiadomosc = czcionka.render(wiadomosc, True, kolor)
        #Pobiera wymiary wiadomosci
        wiadomosc_powierzchnia = wiadomosc.get_rect()
        #Ustala srodek wiadomosci
        wiadomosc_powierzchnia.center = (element.x + int(element.szerokosc / 2) + int(element.szerokosc / 2 * x * 0.1), element.y + int(element.wysokosc / 2) + int(element.wysokosc / 2 * y * 0.1))
        #Wyswietla wiadomosc, w odpowiadajacym jej miejscu
        self.ekran.blit(wiadomosc, wiadomosc_powierzchnia)
    #Funkcja skalujaca menu glowne
    def skaluj_menu_glowne(self):
        #Oblicza pozycje i rozmiary przyciskow menu
        szerokosc = int(self.szerokosc * 0.3)
        x = int((self.szerokosc - szerokosc) / 2)
        wysokosc = int((self.wysokosc * 0.50) / 6)
        y = int((self.wysokosc - wysokosc * 6) / 7)
        odstep = y
        #Dla kazdego przycisku przypisany zostaje wymiar i wspolrzedne, wraz z zwiekszajacym sie odstepem
        for przycisk in self.opcje:
            przycisk.szerokosc = szerokosc
            przycisk.x = x
            przycisk.wysokosc = wysokosc
            przycisk.y = odstep
            odstep = odstep + y + wysokosc
    #Funkcja wyswietlajaca menu glowne
    def wyswietl_menu_glowne(self):
        #Zmienne przechowujace kolory
        kolor_obramowania = (105, 189, 210)
        kolor_tekstu = (55, 55, 55)
        #Wydrukowanie obramowania dla kazdego przycisku
        for przycisk in self.opcje:
            self.wyswietl_obramowanie(kolor_obramowania, przycisk, 1.5)
        #Wyswietlenie tekstu wewnatrz kazdego przycisku
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[0], "Nowa gra", 10)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[1], "Wczytaj", 10)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[2], "Komputer", 10)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[3], "Ranking", 10)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[4], "Autor", 10)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[5], "Wylacz", 10)
    #Funkcja skalujaca menu, autora
    def skaluj_menu_autora(self):
        self.autor_etykieta.szerokosc = int(self.szerokosc * 0.33)
        self.autor_etykieta.x = int(self.szerokosc * 0.33)
        self.autor_etykieta.wysokosc = int(self.wysokosc * 0.33)
        self.autor_etykieta.y = int(self.wysokosc * 0.33)
        self.autor_powrot.szerokosc = int(self.autor_etykieta.szerokosc * 0.75)
        self.autor_powrot.x = self.autor_etykieta.x + int(self.autor_etykieta.szerokosc * 0.125)
        self.autor_powrot.wysokosc = int(self.autor_etykieta.wysokosc * 0.25)
        self.autor_powrot.y = self.autor_etykieta.y + int(self.autor_etykieta.wysokosc * 0.625)
    #Funkcja wyswietlajaca menu, autora
    def wyswietl_menu_autora(self):
        kolor_obramowania = (105, 189, 210)
        kolor_tekstu = (55, 55, 55)
        self.wyswietl_obramowanie(kolor_obramowania, self.autor_etykieta, 2)
        self.wyswietl_wiadomosc(kolor_tekstu, self.autor_etykieta, "Autor:", 3, 0, -6)
        self.wyswietl_wiadomosc(kolor_tekstu, self.autor_etykieta, "Michał Dybaś", 3, 0, -1)
        self.wyswietl_obramowanie(kolor_obramowania, self.autor_powrot, 2)
        self.wyswietl_wiadomosc(kolor_tekstu, self.autor_powrot, "Powrót", 10)
    #Funkcja skalujaca uniwersalne menu dialogowe
    def skaluj_menu_dialogowe(self):
        self.dialog_etykieta.szerokosc = int(self.szerokosc * 0.33)
        self.dialog_etykieta.x = int(self.szerokosc * 0.33)
        self.dialog_etykieta.wysokosc = int(self.wysokosc * 0.33)
        self.dialog_etykieta.y = int(self.wysokosc * 0.33)
        self.dialog2.szerokosc = int(self.dialog_etykieta.szerokosc * 0.75)
        self.dialog2.x = self.dialog_etykieta.x + int(self.dialog_etykieta.szerokosc * 0.125)
        self.dialog2.wysokosc = int(self.dialog_etykieta.wysokosc * 0.25)
        self.dialog2.y = self.dialog_etykieta.y + int(self.dialog_etykieta.wysokosc * 0.650)
        self.dialog1.szerokosc = self.dialog2.szerokosc
        self.dialog1.x = self.dialog2.x
        self.dialog1.wysokosc = self.dialog2.wysokosc
        self.dialog1.y = self.dialog_etykieta.y + int(self.dialog_etykieta.wysokosc * 0.325)
        self.dialog_powrot.szerokosc = int(self.dialog2.szerokosc * 0.8)
        self.dialog_powrot.x = self.dialog2.x + int(self.dialog2.szerokosc * 0.1)
        self.dialog_powrot.wysokosc = int(self.dialog2.wysokosc * 0.9)
        self.dialog_powrot.y = self.dialog_etykieta.y + int(self.dialog_etykieta.wysokosc * 1.1)
    #Funkcja wyswietlajaca uniwersalne menu dialogowe
    def wyswietl_menu_dialogowe(self, etykieta_tekst, opcja1_tekst = None, opcja2_tekst = None, powrot_tekst = None, x = -7):
        kolor_obramowania = (105, 189, 210)
        kolor_tekstu = (55, 55, 55)
        self.wyswietl_obramowanie(kolor_obramowania, self.dialog_etykieta, 2)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, etykieta_tekst, 2.5, 0, x)
        if opcja1_tekst != None:
            self.wyswietl_obramowanie(kolor_obramowania, self.dialog1, 2)
            self.wyswietl_wiadomosc(kolor_tekstu, self.dialog1, opcja1_tekst, 8)
        if opcja2_tekst != None:
            self.wyswietl_obramowanie(kolor_obramowania, self.dialog2, 2)
            self.wyswietl_wiadomosc(kolor_tekstu, self.dialog2, opcja2_tekst, 8)
        if powrot_tekst != None:
            self.wyswietl_obramowanie(kolor_obramowania, self.dialog_powrot, 2)
            self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_powrot, powrot_tekst, 10)
    #Funkcja skalujaca menu rozgrywki
    def skaluj_menu_rozgrywki(self):
        for i in range(6):
            self.opcje[i].szerokosc = int(self.szerokosc * 0.167)
            self.opcje[i].x = 0
            if i > 0:
                self.opcje[i].x = self.opcje[i - 1].x + self.opcje[i - 1].szerokosc
            self.opcje[i].wysokosc = int(self.wysokosc * 0.06)
            self.opcje[i].y = 0
    #Funkcja wyswietlajaca menu
    def wyswietl_menu_rozgrywki(self, rozgrywka, zegar):
        #Zmienne przechowujace kolory
        kolor_obramowania = (105, 189, 210)
        kolor_tekstu = (55, 55, 55)
        #Wydrukowanie obramowania dla kazdego przycisku
        for przycisk in self.opcje:
            self.wyswietl_obramowanie(kolor_obramowania, przycisk, 1.5)
        #Wyswietlenie tekstu wewnatrz kazdego przycisku
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[0], "Ponów grę", 7)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[1], "Zapisz grę", 7)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[2], "Menu główne", 7)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[3], "Cofnij ruch", 7)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[4], "Czas: " + zegar.pobierz_czas() , 7)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[5], "Wynik: " + str(rozgrywka.wynik), 7)
    #Funkcja wyswietlajaca menu
    def wyswietl_menu_rozgrywki_ai(self, rozgrywka, zegar):
        #Zmienne przechowujace kolory
        kolor_obramowania = (105, 189, 210)
        kolor_tekstu = (55, 55, 55)
        #Wydrukowanie obramowania dla kazdego przycisku
        self.wyswietl_obramowanie(kolor_obramowania, self.opcje[0], 1.5)
        self.wyswietl_obramowanie(kolor_obramowania, self.opcje[1], 1.5)
        self.wyswietl_obramowanie(kolor_obramowania, self.opcje[2], 1.5)
        self.wyswietl_obramowanie(kolor_obramowania, self.opcje[3], 1.5)
        self.wyswietl_obramowanie(kolor_obramowania, self.opcje[4], 1.5)
        self.wyswietl_obramowanie(kolor_obramowania, self.opcje[5], 1.5)
        #Wyswietlenie tekstu wewnatrz kazdego przycisku
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[0], "Menu główne", 7)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[1], "Komputer", 7)
        czas = zegar.sekundy
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
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[2], "Czas: " + czas , 7)
        self.wyswietl_wiadomosc(kolor_tekstu, self.opcje[3], "Wynik: " + str(rozgrywka.wynik), 7)
    #Funkcja skalujaca rozgrywke
    def skaluj_rozgrywke(self):
        #W przypadku gry rozgrywka zostala juz stworzona i powracamy do rozgrywki, sprawdza czy konieczne jest jej skalowanie
        #Ten fragment znaczaca przyspiesza dzialanie programu
        if self.rozgrywka_skalowana:
            pygame.init()
            if self.rozgrywka_szerokosc == self.szerokosc and self.rozgrywka_wysokosc == self.wysokosc:
                return
        self.rozgrywka_skalowana = True
        self.rozgrywka_szerokosc = self.szerokosc
        self.rozgrywka_wysokosc = self.wysokosc
        #Tworzy nowe listy przechowujaca grafiki kart
        self.tyl = []
        for i in range(2):
            self.tyl.append([])
        self.baza = []
        for i in range(4):
            self.baza.append([])
        self.karty = []
        for i in range(4):
            self.karty.append([])
        #Laduje grafiki kart do list
        for i in range(len(self.tyl)):
            self.tyl[i] = pygame.image.load(path.join(self.sciezka_karty, "tyl" + str(i) + ".png"))
        for i in range(len(self.baza)):
            self.baza[i] = pygame.image.load(path.join(self.sciezka_karty, "baza" + str(i) + ".png"))
        for i in range(len(self.karty)):
            for y in range(13):
                self.karty[i].append(pygame.image.load(path.join(self.sciezka_karty, str(y) + str(i) + ".png")))
        #Oblicza wymiary kart
        self.karty_x = int(self.szerokosc * 0.08)
        self.karty_y = int(self.karty_x * 1.5)
        #Skaluje zaladowane grafiki kart
        for i in range(len(self.tyl)):
            self.tyl[i] = pygame.transform.scale(self.tyl[i], (self.karty_x, self.karty_y))
        for i in range(len(self.baza)):
            self.baza[i] = pygame.transform.scale(self.baza[i], (self.karty_x, self.karty_y))
        for y in range(len(self.karty)):
            for i in range(len(self.karty[y])):
                self.karty[y][i] = pygame.transform.scale(self.karty[y][i], (self.karty_x, self.karty_y))
        #Ustawia wymiary przyciskow
        for i in self.tyl_przycisk:
            i.szerokosc = self.karty_x
            i.wysokosc = self.karty_y
        for i in self.baza_przycisk:
            i.szerokosc = self.karty_x
            i.wysokosc = self.karty_y
        for y in self.karty_przycisk:
            for i in y:
                i.szerokosc = self.karty_x
                i.wysokosc = self.karty_y
        for i in self.robocze_przycisk:
            i.szerokosc = self.karty_x
            i.wysokosc = self.karty_y
        #Ustawienie polozenia pol wiadacych, wzorcowych to obliczania polozenia pol pozostalych
        #Obliczenie odstepu pomiedzy przyciskami
        odstep = int((self.szerokosc * 0.7 - 7 * self.karty_x) / 6) + self.karty_x
        #Obliczenie wspolrzednych kolumny rezerwowej
        self.tyl_przycisk[0].x = self.tyl_przycisk[1].x = int(self.szerokosc * 0.15)
        self.tyl_przycisk[0].y = self.tyl_przycisk[1].y = int(self.wysokosc * 0.075)
        #Obliczenie wspolrzednych kolumn roboczych
        for i in self.robocze_przycisk:
            i.y = int(self.wysokosc * 0.1) + self.karty_y
        self.robocze_przycisk[0].x = self.tyl_przycisk[0].x
        self.robocze_przycisk[1].x = self.robocze_przycisk[0].x + odstep
        self.robocze_przycisk[2].x = self.robocze_przycisk[1].x + odstep
        self.robocze_przycisk[3].x = self.robocze_przycisk[2].x + odstep
        self.robocze_przycisk[4].x = self.robocze_przycisk[3].x + odstep
        self.robocze_przycisk[5].x = self.robocze_przycisk[4].x + odstep
        self.robocze_przycisk[6].x = self.robocze_przycisk[5].x + odstep
        #Obliczenie wspolrzednych kolumn bazowych
        self.baza_przycisk[0].y = self.baza_przycisk[1].y = self.baza_przycisk[2].y = self.baza_przycisk[3].y = int(self.wysokosc * 0.075)
        self.baza_przycisk[3].x = self.robocze_przycisk[6].x
        self.baza_przycisk[2].x = self.baza_przycisk[3].x - odstep
        self.baza_przycisk[1].x = self.baza_przycisk[2].x - odstep
        self.baza_przycisk[0].x = self.baza_przycisk[1].x - odstep
    #Funkcja wyswietlajaca karte
    def wyswietl_karte(self, karta, przycisk):
        self.ekran.blit(karta, (przycisk.x, przycisk.y))
    #Funkcja obliczajaca wspolrzedne kart na podstawie obliczonych poprzednio kolumn
    def karty_wspolrzedne(self, rozgrywka):
        #Oblicza wspolrzedne kart w kolumnach roboczych
            for y in range(len(rozgrywka.robocze)):
                i = 0
                while i < len(rozgrywka.robocze[y]):
                    if i == 0:
                        self.karty_przycisk[rozgrywka.robocze[y][i][1]][rozgrywka.robocze[y][i][0]].x = self.robocze_przycisk[y].x
                        self.karty_przycisk[rozgrywka.robocze[y][i][1]][rozgrywka.robocze[y][i][0]].y = self.robocze_przycisk[y].y
                    else:
                        self.karty_przycisk[rozgrywka.robocze[y][i][1]][rozgrywka.robocze[y][i][0]].x = self.karty_przycisk[rozgrywka.robocze[y][i - 1][1]][rozgrywka.robocze[y][i - 1][0]].x
                        if rozgrywka.robocze[y][i - 1][2] == 0:
                            odstep = int(self.karty_y * 0.075)
                        else:
                            odstep = int(self.karty_y * 0.175)
                        self.karty_przycisk[rozgrywka.robocze[y][i][1]][rozgrywka.robocze[y][i][0]].y = odstep + self.karty_przycisk[rozgrywka.robocze[y][i - 1][1]][rozgrywka.robocze[y][i - 1][0]].y
                    i += 1
        #Oblicza wspolrzedne kart w kolumnach bazowych
            for y in range(len(rozgrywka.bazowe)):
                i = 0
                while i < len(rozgrywka.bazowe[y]):
                    self.karty_przycisk[rozgrywka.bazowe[y][i][1]][rozgrywka.bazowe[y][i][0]].x = self.baza_przycisk[y].x
                    self.karty_przycisk[rozgrywka.bazowe[y][i][1]][rozgrywka.bazowe[y][i][0]].y = self.baza_przycisk[y].y
                    i += 1
        #Oblicza wspolrzedne kart w kolumnach rezerwowych
            odstep = int(self.karty_x * 0.3)
            for y in range(len(rozgrywka.rezerwowe)):
                i = 0
                while i < len(rozgrywka.rezerwowe[y]):
                    self.karty_przycisk[rozgrywka.rezerwowe[y][i][1]][rozgrywka.rezerwowe[y][i][0]].y = self.baza_przycisk[0].y
                    if i == 0:
                        self.karty_przycisk[rozgrywka.rezerwowe[y][i][1]][rozgrywka.rezerwowe[y][i][0]].x = self.robocze_przycisk[1].x
                    else:
                        self.karty_przycisk[rozgrywka.rezerwowe[y][i][1]][rozgrywka.rezerwowe[y][i][0]].x = odstep + self.karty_przycisk[rozgrywka.rezerwowe[y][i - 1][1]][rozgrywka.rezerwowe[y][i - 1][0]].x
                    i += 1
    #Funkcja wyswietlajaca rozgrywke
    def wyswietl_rozgrywke(self, rozgrywka, nad = None):
        #Wyswietla szkielet rozgrywki
        if rozgrywka.rez_indeks != -1:
            self.wyswietl_karte(self.tyl[0], self.tyl_przycisk[0])
        else:
            self.wyswietl_karte(self.tyl[1], self.tyl_przycisk[0])
        for i in range(len(self.baza)):
            self.wyswietl_karte(self.baza[i], self.baza_przycisk[i])
        for i in range(len(self.robocze_przycisk)):
            self.wyswietl_karte(self.tyl[1], self.robocze_przycisk[i])
        #Wyswietla karty w kolumnach roboczych
        for y in range(len(rozgrywka.robocze)):
            i = 0
            if nad is not None:
                if nad == y and nad < len(rozgrywka.robocze) - 1:
                    y += 1
                    continue
            while i < len(rozgrywka.robocze[y]):
                if rozgrywka.robocze[y][i][2] == 0:
                    self.wyswietl_karte(self.tyl[0], self.karty_przycisk[rozgrywka.robocze[y][i][1]][rozgrywka.robocze[y][i][0]])
                else:
                    self.wyswietl_karte(self.karty[rozgrywka.robocze[y][i][1]][rozgrywka.robocze[y][i][0]], self.karty_przycisk[rozgrywka.robocze[y][i][1]][rozgrywka.robocze[y][i][0]])
                i += 1
        if nad is not None and nad < len(rozgrywka.robocze) - 1:
            i = 0
            while i < len(rozgrywka.robocze[nad]):
                if rozgrywka.robocze[nad][i][2] == 0:
                    self.wyswietl_karte(self.tyl[0], self.karty_przycisk[rozgrywka.robocze[nad][i][1]][rozgrywka.robocze[nad][i][0]])
                else:
                    self.wyswietl_karte(self.karty[rozgrywka.robocze[nad][i][1]][rozgrywka.robocze[nad][i][0]], self.karty_przycisk[rozgrywka.robocze[nad][i][1]][rozgrywka.robocze[nad][i][0]])
                i += 1
        #Wyswietla karty w kolumnach bazowych
        for y in range(len(rozgrywka.bazowe)):
            i = 0
            while i < len(rozgrywka.bazowe[y]):
                self.wyswietl_karte(self.karty[rozgrywka.bazowe[y][i][1]][rozgrywka.bazowe[y][i][0]], self.karty_przycisk[rozgrywka.bazowe[y][i][1]][rozgrywka.bazowe[y][i][0]])
                i += 1
        #Wyswietla aktualnie dostepne karty rezerwowe
        for y in range(len(rozgrywka.rezerwowe)):
            i = 0
            if y == rozgrywka.rez_indeks:
                while i < len(rozgrywka.rezerwowe[y]):
                    self.wyswietl_karte(self.karty[rozgrywka.rezerwowe[y][i][1]][rozgrywka.rezerwowe[y][i][0]], self.karty_przycisk[rozgrywka.rezerwowe[y][i][1]][rozgrywka.rezerwowe[y][i][0]])
                    i += 1
        #Wyswietla 2 tlo w przypadku braku kart w kolumnach rezerwowych
        if rozgrywka.rez_indeks == - 2:
            self.wyswietl_karte(self.tyl[1], self.tyl_przycisk[0])
    #Wyswietla menu wygranej gry
    def wyswietl_menu_wygrana(self, informacja, wynik, bonus, czas, nazwa):
        kolor_obramowania = (105, 189, 210)
        kolor_tekstu = (55, 55, 55)
        self.wyswietl_obramowanie(kolor_obramowania, self.dialog_etykieta, 2)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, informacja, 4, 0, -14)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, wynik, 2, 0, -7)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, bonus, 2, 0, -3.5)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, czas, 2, 0 , 0)
        self.wyswietl_obramowanie(kolor_obramowania, self.dialog2, 2)
        if len(nazwa) == 0:
            self.wyswietl_wiadomosc((200, 50, 50), self.dialog2, "Wpisz nazwę:", 8)
        else:
            self.wyswietl_wiadomosc(kolor_tekstu, self.dialog2, nazwa, 8)
        self.wyswietl_obramowanie(kolor_obramowania, self.dialog_powrot, 2)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_powrot, "Powrót", 10)
    #Wyswietla menu wygranej gry
    def wyswietl_menu_wygrana_ai(self, wynik, bonus, czas, nazwa):
        kolor_obramowania = (105, 189, 210)
        kolor_tekstu = (55, 55, 55)
        self.wyswietl_obramowanie(kolor_obramowania, self.dialog_etykieta, 2)
        if nazwa == "Wygrana":
            self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, "Zwycięstwo AI", 4, 0, -14)
        elif nazwa == "Przegrana":
            self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, "Porażka AI", 4, 0, -14)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, wynik, 2, 0, -7)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, bonus, 2, 0, -3.5)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, czas, 2, 0 , 0)
        self.wyswietl_obramowanie(kolor_obramowania, self.dialog2, 2)
        self.wyswietl_wiadomosc((200, 50, 50), self.dialog2, "Komputer AI", 8)
        self.wyswietl_obramowanie(kolor_obramowania, self.dialog_powrot, 2)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_powrot, "Powrót", 10)
    def wyswietl_menu_ranking(self):
        kolor_obramowania = (105, 189, 210)
        kolor_tekstu = (55, 55, 55)
        #self.wyswietl_obramowanie(kolor_obramowania, self.dialog_etykieta, 2)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, "RANKING", 3, 0, -26)
        self.dialog_powrot.y = int(self.wysokosc * 0.9)
        self.wyswietl_obramowanie(kolor_obramowania, self.dialog_powrot, 2)
        self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_powrot, "Powrót", 10)
        plik = 0
        #Sprawdza, czy plik został utworzony
        try:
            plik = open(path.join(self.sciezka, "ranking.txt"), 'r')
        except:
            plik = open(path.join(self.sciezka, "ranking.txt"), 'x')
        #Czyta wszystkie wiersze z pliku
        wiersze = plik.readlines()
        if len(wiersze) == 0:
            self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, "Pusty", 2.5, 0, -22)
        else:
            for i in range(len(wiersze)):
                kolummna = wiersze[i].split(" ")
                tekst = "Gracz: " + kolummna[0] + "  Wynik:" + kolummna[1] + "  Czas: " + kolummna[2][:len(kolummna[2]) -1]
                if i < 20:
                    self.wyswietl_wiadomosc(kolor_tekstu, self.dialog_etykieta, tekst, 1.5, 0, -22 + i * 2.2)