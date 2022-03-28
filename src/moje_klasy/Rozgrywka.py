#Zaimportowanie klasy Talia i Muzyka
from moje_klasy.Talia import *
from moje_klasy.Muzyka import *
#Zaimportowanie funkcji deepcopy z biblioteki copy, do kopiowania list wielowymiarowych
from copy import deepcopy
#Utworzenie obiektu klasy muzyka
#Klasa bedaca odwzorowaniem mechaniki gry
class Rozgrywka:
    #Listy przechowujace kolumny kart w polu i ich kopie, uzywane w przypadku odnowienia danego rozdania
    robocze = []
    rezerwowe = []
    bazowe = []
    robocze_kopia = []
    rezerwowe_kopia = []
    bazowe_kopia = []
    #Zmienna przechowujaca, indeks obecnie widocznych kart w kolumnie rezerwowej
    rez_indeks = -1
    #Zmienna informujaca, czy w kolumnie rezerwowej rozdane beda 1 lub 3 karty
    tryb = False
    #Zmienna przechowujaca historie ruchow
    historia = []
    #Zmienne przechowujace, ilosc punktow i czas trwania rozgrywki i ilosc punktow bonusowych za czas oraz nazwe gracza
    wynik = 0
    czas = 0
    bonus = 0
    gracz = ""
    #Zmienna przechowująca, liczbę przetasowań stosu rezerwowego na potrzeby sztucznej inteligencji
    ruch = 0
    #Funkcja przywracajaca wartosci domyslne
    def wyczysc(self):
        self.robocze = []
        self.rezerwowe = []
        self.bazowe = []
        self.rez_indeks = -1
        self.historia = []
        self.wynik = 0
        self.bonus = 0
        self.czas = 0
        self.gracz = ""
        self.ruch = 0
    #Funkcja przywracajaca wartosci domyslne rozgrywki
    def resetuj(self):
        self.robocze = deepcopy(self.robocze_kopia)
        self.rezerwowe = deepcopy(self.rezerwowe_kopia.copy())
        self.bazowe = deepcopy(self.bazowe_kopia.copy())
        self.rez_indeks = -1
        self.historia = []
        self.wynik = 0
        self.bonus = 0
        self.czas = 0
        self.gracz = ""
    #Funkcja przydzielajaca karty z tali do odpowiednich kolumn
    def przydziel_karty(self, tryb: bool):
        #Dla trybu ustawia odpowiednia ilosc kart
        if tryb == False:
            self.tryb = 1
        else:
            self.tryb = 3
        #Tworzy obiekt klasy Talia i tworzy talie kart
        talia = Talia()
        talia.utworztalie()
        #Losuje karty z tali do kolumn roboczych
        for i in range(0, 7):
            kolumna = []
            for y in range(0, i + 1):
                kolumna.append(talia.losujkarte())
            self.robocze.append(kolumna)
        #Losuje karty z tali do kolumn rezerwowych, ilość kart w jednej kolumnie według trybu, dodatkowo odslania wszystkie karty
        while len(talia.karty) > 0:
            kolumna = []
            for i in range(self.tryb):
                x = talia.losujkarte()
                if x == False:
                    break
                kolumna.append(x)
            if len(kolumna) == 0:
                break
            for i in kolumna:
                i[2] = 1
            self.rezerwowe.append(kolumna)
        for i in range(4):
            self.bazowe.append([])
        #Utworzenie kopii zapasowej rozdanych kolumn, do przywrocenia wartoci domyslnych rozgrywki
        self.robocze_kopia = deepcopy(self.robocze)
        self.rezerwowe_kopia = deepcopy(self.rezerwowe)
        self.bazowe_kopia = deepcopy(self.bazowe)
        self.tryb_kopia = self.tryb
    #Funkcja porownojaca karty, w obszarze roboczym, jesli kolor jest rozny i karta mlodsza ma wartosc o 1 mniejsza, zwraca True
    def porownaj_robocze(self, mlodsza, starsza):
        if mlodsza[2] == 0 or starsza[2] == 0:
            return False
        if mlodsza[0] + 1 == starsza[0]:
            if mlodsza[1] % 2 != starsza[1] % 2:
                return True
        return False
    #Funkcja poronojaca karty, w obszarze bazowym jesli karty sa dokladnie takiego samego koloru i karta starsza ma wartosc 0 1 wieksza, zwraca True
    def porownaj_bazowe(self, starsza):
        if starsza[0] == 0 and len(self.bazowe[starsza[1]]) == 0:
            return True
        elif len(self.bazowe[starsza[1]]) != 0 and starsza[0] == self.bazowe[starsza[1]][len(self.bazowe[starsza[1]]) - 1][0] + 1:
            return True
        else:
            return False
    #Funkcja odslaniajaca ukryte karty
    def odslon_karty(self):
        for i in self.robocze:
            if len(i) > 0:
                i[len(i) - 1][2] = 1
    #Funkcja sprawdzajaca w kolumnie roboczej czy karta nie zostala odkryta
    def sprawdz_i_odslon(self, kolumna):
        if len(self.robocze[kolumna]) > 0:
            if self.robocze[kolumna][len(self.robocze[kolumna]) - 1][2] == 0:
                self.robocze[kolumna][len(self.robocze[kolumna]) - 1][2] = 1
                self.wynik += 5
                self.historia.append([-2, kolumna, 5])
    #Funkcja wywoływana po klknięciu w stos kart rezerwowych, iteruje przez kolejne karty w stosie
    def zwieksz_rezerwowe(self):
        if self.rez_indeks != -2:
            pusty = True
            for y in range(len(self.rezerwowe)):
                if len(self.rezerwowe[y]) != 0:
                    pusty = False
            if pusty:
                self.rez_indeks = -2
                return
            if self.rez_indeks == len(self.rezerwowe) - 1:
                self.rez_indeks = -1
                self.wynik -= 25
                self.historia.append([-1, -25])
                return True
            else:
                self.rez_indeks += 1
                if len(self.rezerwowe[self.rez_indeks]) == 0:
                    self.zwieksz_rezerwowe()
                else:
                    self.historia.append([-1, 0])
                    return True
        return False
    #Funkcja przenoszaca, automatycznie jedna karte, jesli jest taka mozliwosc
    def przenies_jedna_karte(self, stos, kolumna = -1, podkolumna = -1, ilosc = None):
        #Dla karty rezerwowej
        if stos == 0:
            #Dla stosu kart bazowych o odpowiadajacym kolorze
            if kolumna == -1:
                karta = self.rezerwowe[self.rez_indeks][len(self.rezerwowe[self.rez_indeks]) - 1]
                if self.porownaj_bazowe(karta):
                    self.historia.append([0, self.rez_indeks, 2, karta[1], 1, 15])
                    karta = self.rezerwowe[self.rez_indeks].pop(len(self.rezerwowe[self.rez_indeks]) - 1)
                    self.bazowe[karta[1]].append(karta)
                    self.wynik += 15
                    return True
            #Dla stosu kart roboczych, o odpowiedniej kolumnie
            elif kolumna != - 1:
                karta = self.rezerwowe[self.rez_indeks][len(self.rezerwowe[self.rez_indeks]) - 1]
                if len(self.robocze[kolumna]) == 0 or self.porownaj_robocze(karta, self.robocze[kolumna][len(self.robocze[kolumna]) - 1]):
                    self.historia.append([0, self.rez_indeks, 1, kolumna, 1, 5])
                    karta = self.rezerwowe[self.rez_indeks].pop(len(self.rezerwowe[self.rez_indeks]) - 1)
                    self.robocze[kolumna].append(karta)
                    self.wynik += 5
                    return True
        #Dla karty roboczej
        elif stos == 1:
            if ilosc is not None:
                dlugosc = len(self.robocze[kolumna]) - ilosc
                karta = self.robocze[kolumna][dlugosc]
                for i in range(dlugosc, len(self.robocze[kolumna])):
                    if self.robocze[kolumna][i][2] == 0:
                        return False
                if len(self.robocze[podkolumna]) == 0 or self.porownaj_robocze(karta, self.robocze[podkolumna][len(self.robocze[podkolumna]) - 1]):
                    while dlugosc < len(self.robocze[kolumna]):
                        self.robocze[podkolumna].append(self.robocze[kolumna].pop(dlugosc))
                    self.historia.append([1, kolumna, 1, podkolumna, ilosc, 0])
                    self.sprawdz_i_odslon(kolumna)
                    return True
            else:
                karta = self.robocze[kolumna][len(self.robocze[kolumna]) - 1]
                if self.porownaj_bazowe(karta):
                    self.historia.append([1, kolumna, 2, karta[1], 1, 10])
                    karta = self.robocze[kolumna].pop(len(self.robocze[kolumna]) - 1)
                    self.sprawdz_i_odslon(kolumna)
                    self.bazowe[karta[1]].append(karta)
                    self.wynik += 10
                    return True
            return False
        #Dla karty bazowej
        elif stos == 2:
            karta = self.bazowe[kolumna][len(self.bazowe[kolumna]) - 1]
            if ilosc is not None or self.porownaj_robocze(karta, self.robocze[podkolumna][len(self.robocze[podkolumna]) - 1]):
                self.historia.append([2, kolumna, 1, podkolumna, 1, 0])
                karta = self.bazowe[kolumna].pop(len(self.bazowe[kolumna]) - 1)
                self.robocze[podkolumna].append(karta)
                return
    #Funkcja cofajaca ruch i przywracajaca liczbe punktow z przed ruchu
    def cofnij_ruch(self):
        if len(self.historia) == 0:
            return False
        ruch = self.historia.pop(len(self.historia) - 1)
        #Cofniecie widocznych kolumn w stosie rezerwowym
        if ruch[0] == -1:
            #Jeśli zbiór kart rezerwowych jest pusty, zmienia indeks na indeks ostatniej kolumny
            if self.rez_indeks == -2 or self.rez_indeks == -1:
                self.rez_indeks = len(self.rezerwowe) - 1
                #Jesli w ostatniej kolumnie są karty, wychodzi z funkcji
                if len(self.rezerwowe[self.rez_indeks]) > 0:
                    return True
            #Jeśli wybrana zostałą kolumna domyśłna, nie są widoczne karty
            elif self.rez_indeks == -1:
                self.rez_indeks = len(self.rezerwowe) - 1
                #Jesli w ostatniej kolumnie są karty, wychodzi z funkcji i dodaje punkty
                if len(self.rezerwowe[self.rez_indeks]) > 0:
                    self.wynik -= ruch[1]
                    return True
            #Zmniejsza indeks
            self.rez_indeks -= 1
            #Jesli kolumna rezerwowa o danym indeksie jest pusta lub indeks wynosi -1 zmniejsza indeks
            while len(self.rezerwowe[self.rez_indeks]) == 0:
                self.rez_indeks -= 1
            return True
        #Zakrycie kart
        elif ruch[0] == -2:
            #Zakrywa odpowiednia karte
            self.robocze[ruch[1]][len(self.robocze[ruch[1]]) - 1][2] = 0
            self.wynik -= ruch[2]
            #Wywoluje rekurencyjnie funkcjie cofni_ruch, aby na zakrytej karcie znalazly sie inne karty
            self.cofnij_ruch()
        #Przeniesienie kart
        else:
            od = 0
            do = 0
            #Przypisanie zmiennej stosu do ktorego przeniesc karty
            if ruch[0] == 0:
                do = self.rezerwowe
            elif ruch[0] == 1:
                do = self.robocze
            elif ruch[0] == 2:
                do = self.bazowe
            #Przypisanie zmiennej stosu z którego przeniesc karty
            if ruch[2] == 0:
                od = self.rezerwowe
            elif ruch[2] == 1:
                od = self.robocze
            elif ruch[2] == 2:
                od = self.bazowe
            #Zmniejszenie ilosci punktow
            self.wynik -= ruch[5]
            #[1, kolumna, 1, podkolumna, ilosc, 0]
            #Przeniesienie kart w ich poprzednie miejsce
            dlugosc = len(od[ruch[3]]) - ruch[4]
            while dlugosc < len(od[ruch[3]]):
                do[ruch[1]].append(od[ruch[3]].pop(dlugosc))
            return True
    #Funkcja zwracajaca true jesli gracz ulozyl wszystkie karty
    def zwyciestwo(self):
        if len(self.bazowe) != 4:
            return False
        for i in self.bazowe:
            if len(i) != 13:
                return False
        return True
    #Zapisuje gracza do rankingu
    def zapisz_ranking(self):
        sciezka = path.join(path.dirname(__file__), "..")
        ranking_sciezka = path.join(sciezka, "ranking.txt")
        plik = 0
        #Sprawdza, czy plik nie zostaj luz utworzony
        try:
            plik = open(ranking_sciezka, 'r')
        except:
            plik = open(ranking_sciezka, 'x')
        #Czyta wszystkie wiersze z pliku
        wiersze = plik.readlines()
        for i in range(len(wiersze)):
            kolumna = wiersze[i].split(" ")
            if int(kolumna[1]) < self.wynik + self.bonus:
                wiersze.insert(i, self.gracz + " " + str(self.wynik + self.bonus) + " " + str(self.czas) + "\n")
                break
        else:
            wiersze.append(self.gracz + " " + str(self.wynik + self.bonus) + " " + str(self.czas) + "\n")
        if len(wiersze) == 0 :
            wiersze.insert(0, self.gracz + " " + str(self.wynik + self.bonus) + " " + str(self.czas) + "\n")
        if len(wiersze) > 20:
            wiersze = wiersze[0:20]
        #Otwiera plik w trybie do zapisu, czyszczac uprzednio plik
        plik = open(ranking_sciezka, 'w')
        plik.writelines(wiersze)
    #Funkcja zapisujaca liste kart do pliku
    def zapisz_liste(self, plik, karty):
        for i in range(len(karty)):
            if len(karty[i]) == 0:
                plik.write("!")
            else:
                for y in range(len(karty[i])):
                    plik.write(str(karty[i][y][0]) + ",")
                    plik.write(str(karty[i][y][1]) + ",")
                    plik.write(str(karty[i][y][2]))
                    if y < len(karty[i]) - 1:
                        plik.write("|")
            if i < len(karty) - 1:
                plik.write("&")
        plik.write("\n")
    #Funkcja zapisujaca liste historia do pliku
    def zapisz_historie(self, plik, karty):
        for i in range(len(karty)):
            for y in range(len(karty[i])):
                plik.write(str(karty[i][y]))
                if y < len(karty[i]) - 1:
                    plik.write(",")
            if i < len(karty) - 1:
                plik.write("&")
        if len(karty) == 0:
            plik.write("!")
        plik.write("\n")
    #Funkcja zapisujaca rozgrywke do pliku
    def zapisz_rozgrywke(self):
        sciezka = path.join(path.dirname(__file__), "..")
        zapis_sciezka = path.join(sciezka, "zapis.txt")
        plik = open(zapis_sciezka, 'w')
        #Do oddzielania zmiennych \n
        #Do oddzielania kolumn w liscie &
        #Dla pustych kolumn !
        #Do oddzielania kart |
        #Do oddzielania wartosci kart ,
        #Kolejność zapisu zmiennych
        #tryb = False
        #rez_indeks = -1
        #wynik = 0
        #czas = 0
        #robocze = []
        #robocze_kopia = []
        #rezerwowe = []
        #rezerwowe_kopia = []
        #bazowe = []
        #bazowe_kopia = []
        #historia = []
        plik.write(str(self.tryb) + "\n")
        plik.write(str(self.rez_indeks) + "\n")
        plik.write(str(self.wynik) + "\n")
        plik.write(str(self.czas) + "\n")
        self.zapisz_liste(plik, self.robocze)
        self.zapisz_liste(plik, self.robocze_kopia)
        self.zapisz_liste(plik, self.rezerwowe)
        self.zapisz_liste(plik, self.rezerwowe_kopia)
        self.zapisz_liste(plik, self.bazowe)
        self.zapisz_liste(plik, self.bazowe_kopia)
        self.zapisz_historie(plik, self.historia)
        plik.close()
    #Funkcja sprwadzajaca, czy zapisana zostala rozgrywka
    def wczytaj_sprawdz(self):
        sciezka = path.join(path.dirname(__file__), "..")
        zapis_sciezka = path.join(sciezka, "zapis.txt")
        plik = 0
        try:
            plik = open(zapis_sciezka, 'r')
        except:
            return  False
        wiersze = plik.readlines()
        if len(wiersze) == 0:
            plik.close()
            return False
        plik.close()
        return True
    #Funkcja zamieniajaca uprzednio zapisany wiersz na liste
    def wczytaj_liste(self, wiersz):
        kolumny = wiersz.split("&")
        lista = []
        if len(kolumny) == 1 and kolumny[0].rstrip() == "!":
            return lista
        for i in range(len(kolumny)):
            lista.append([])
        for y in range(len(lista)):
            #Jeśli kolumna w pliku nie jest pusta
            if kolumny[y] != "!":
                #Dzieli kolumne na karty
                karty = kolumny[y].split("|")
                for i in range(len(karty)):
                    #Dzieli karte na wartosci
                    wartosci = karty[i].split(",")
                    if wartosci[0].rstrip() == "!":
                        continue
                    karta = []
                    #Konwertuje wartosci i dodaje do listy tymczasowej
                    for w in range(len(wartosci)):
                        karta.append(int(wartosci[w].rstrip()))
                    #Lista tymczasowa zostaje przypisana do listy
                    lista[y].append(karta)
        return lista
    #Funkcja zamieniajaca uprzednio zapisany wiersz na liste histori
    def wczytaj_historie(self, wiersz):
        kolumny = wiersz.split("&")
        lista = []
        #Jeśli historia nie jest pusta
        if kolumny[0].rstrip() == "!":
            return lista
        for y in range(len(kolumny)):
            # Dzieli kolumne na wartosci
            wartosci = kolumny[y].split(",")
            if wartosci[0].rstrip() == "!":
                continue
            karta = []
            # Konwertuje wartosci i dodaje do listy tymczasowej
            for w in range(len(wartosci)):
                karta.append(int(wartosci[w].rstrip()))
            #Lista tymczasowa zostaje przypisana do listy
            lista.append(karta)
        return lista
    #Funkcja wczytująca rozgrywke z pliku, jeśli jest to możliwe
    def wczytaj_rozgrywke(self, zegar):
        sciezka = path.split(path.dirname(__file__))[0]
        zapis_sciezka = path.join(sciezka, "zapis.txt")
        plik = 0
        try:
            plik = open(zapis_sciezka, 'r')
        except:
            return  False
        #Dla każdego elementu z listy, usuwa znaki nowej lini
        wiersze = plik.readlines()
        for i in wiersze:
            i = i[0:len(i) - 1]
        #Konwersja i przypisanie zwyklych zmiennych
        self.tryb = int(wiersze[0])
        self.rez_indeks = int(wiersze[1])
        self.wynik = int(wiersze[2])
        zegar.sekundy = float(wiersze[3])
        zegar.sekundy_poprzednie = float(wiersze[3])
        #Konwersja i przypisanie list
        self.robocze = self.wczytaj_liste(wiersze[4])
        self.robocze_kopia = self.wczytaj_liste(wiersze[5])
        self.rezerwowe = self.wczytaj_liste(wiersze[6])
        self.rezerwowe_kopia = self.wczytaj_liste(wiersze[7])
        self.bazowe = self.wczytaj_liste(wiersze[8])
        self.bazowe_kopia = self.wczytaj_liste(wiersze[9])
        self.historia = self.wczytaj_historie(wiersze[10])
        plik.close()
    #Funkcja pełniąca role ai, przenosząca jednorazowo karty, lub przewijająca stos
    def sztuczna_inteligencja(self, zdarzenia):
        #Utworzenie obiektu klasy muzyka
        muzyka = Muzyka()
        #Próbuje przenieść karte z stosu roboczego do stosu bazowego
        for i in range(7):
            if len(self.robocze[i]) > 0:
                if self.przenies_jedna_karte(1, i):
                    self.ruch = 0
                    muzyka.odtworz("baza.wav")
                    return True
        #Jeśli nie wykonano ruchu, próbuje przemieszczać karty w stosie roboczym
        z = 12
        while z >= 0:
            for x in range(15):
                y = len(self.robocze) - 1
                while y >= 0:
                    if len(self.robocze[y]) == x:
                        for i in range(len(self.robocze[y])):
                            for d in range(7):
                                if d != y and self.robocze[y][i][0] == z:
                                    if i == 0 and len(self.robocze[d]) > 0 and self.przenies_jedna_karte(1, y, d, len(self.robocze[y]) - i):
                                        self.ruch = 0
                                        muzyka.odtworz("opuszczenie.wav")
                                        return True
                                    elif i != 0 and self.robocze[y][i - 1][2] == 0 and self.przenies_jedna_karte(1, y, d, len(self.robocze[y]) - i):
                                        self.ruch = 0
                                        muzyka.odtworz("opuszczenie.wav")
                                        return True
                                    elif i != 0 and len(self.robocze[d]) > 0 and self.robocze[y][i - 1][2] == 1 and self.robocze[y][i - 1][0] != self.robocze[d][len(self.robocze[d]) - 1][0] and self.przenies_jedna_karte(1, y, d, len(self.robocze[y]) - i):
                                        self.ruch = 0
                                        muzyka.odtworz("opuszczenie.wav")
                                        return True
                    y -= 1
            z -= 1
        #Jeśli nie wykonano ruchu, próbuje przenieść kartę z stosu rezerwowego, do stosu bazowego
        if len(self.rezerwowe[self.rez_indeks]) > 0:
            if self.przenies_jedna_karte(0):
                self.ruch = 0
                muzyka.odtworz("baza.wav")
                return True
        #Jeśli nie wykonano ruchu, próbuje przenieść karte z stosu rezerwowego do stosu roboczego
        if len(self.rezerwowe[self.rez_indeks]) > 0:
            for i in range(7):
                if self.przenies_jedna_karte(0, i):
                    self.ruch = 0
                    muzyka.odtworz("opuszczenie.wav")
                    return True
        #Jeśli nie wykonano ruchu i stos rezerwowy nie jest pusty, próbuje zwiększyć indeks kart rezerwowych
        #Zablokowane zostało ciągłe zwiększanie indeksu stosu kart rezerwowych, powodująć, że liczba przetasowań
        #nie może być większa niż liczba kolumn w tym stosie
        x = 0
        for i in self.rezerwowe:
            if len(i) > 0:
                x += 1
        if self.rez_indeks != -2:
            if self.ruch <= x + 2 :
                self.ruch += 1
                self.zwieksz_rezerwowe()
                muzyka.odtworz("rezerwowe.wav")
                return True
        self.gracz = "Przegrana"
        zdarzenia.typ_zdarzen = 2.4
        return False