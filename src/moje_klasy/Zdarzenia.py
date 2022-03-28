#Zaimportowanie biblioteki pygame i klasy Muzyka
from moje_klasy.Muzyka import *
#Utworzenie obiektu klasy muzyka
muzyka = Muzyka()

#Definicja funkcji pobierajacej i obslugujacej zdarzenia
class Zdarzenia:
    #Zmienna przechowujaca typ zdarzen, ktore aktualnie przetwarza obiekt
    typ_zdarzen = 0
    #Funkcja obslugujaca zdarzenia wystepujace w menu glownym
    def obsluga_zdarzen_menu_glowne(self, ekran):
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        zdarzenie = pygame.event.wait()
        #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
        if zdarzenie.type == pygame.QUIT:
            ekran.wylacz_okno()
        #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna i menu
        elif zdarzenie.type == pygame.VIDEORESIZE:
            ekran.skaluj_okno(zdarzenie)
            ekran.skaluj_menu_glowne()
        #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na opcje z menu glownego
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            #Dla opcji nowa gra, zmienia typ zdarzenia i przechodzi do menu tworzenia nowej gry
            if ekran.opcje[0].zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_dialogowe()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 1.1
            #Dla opcji wczytaj, zmienia typ zdarzenia, skaluje okno dialogowe i przechodzi do okna wczytania gry
            elif ekran.opcje[1].zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_dialogowe()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 1.7
            #Dla opcji Test AI przechodzi do menu tworzenia nowej gry dla test ai
            elif ekran.opcje[2].zaznaczony(zdarzenie.pos):
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 2.1
            elif ekran.opcje[3].zaznaczony(zdarzenie.pos):
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 3
            elif ekran.opcje[4].zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_autora()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 4
            #Dla opcji wylacz, konczy dzialanie programu
            elif ekran.opcje[5].zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_dialogowe()
                self.typ_zdarzen = 0.1
    #Funkcja obslugujaca zdarzenia okna dialogowego pytajacego czy wylaczyc gre
    def obsluga_zdarzen_wylacz(self, ekran):
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        zdarzenie = pygame.event.wait()
        #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
        if zdarzenie.type == pygame.QUIT:
            ekran.wylacz_okno()
        #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
        elif zdarzenie.type == pygame.VIDEORESIZE:
            ekran.skaluj_okno(zdarzenie)
            ekran.skaluj_okno_dialogowe()
        #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na opcje z okna dialogowego
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            #Dla opcji Tak wylacza gre
            if ekran.dialog1.zaznaczony(zdarzenie.pos):
                ekran.wylacz_okno()
            #Dla opcji Nie skaluje menu glowne i powraca do menu glownego
            elif ekran.dialog2.zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_glowne()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 0
    #Funkcja obslugujaca zdarzenia tworzenia nowej gry
    def obsluga_zdarzen_nowa_gra(self, ekran, rozgrywka, zegar, zegar_ai, typ_zdarzen = 1.2):
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        zdarzenie = pygame.event.wait()
        #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
        if zdarzenie.type == pygame.QUIT:
            ekran.wylacz_okno()
        #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
        elif zdarzenie.type == pygame.VIDEORESIZE:
            ekran.skaluj_okno(zdarzenie)
            ekran.skaluj_menu_dialogowe()
        #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na opcje z okna dialogowego
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            #Dla opcji 1 Karta tworzy rozgrywke z 1 rozdaniem, skaluje rozgrywke i przechodzi do rozgrywki
            if ekran.dialog1.zaznaczony(zdarzenie.pos):
                rozgrywka.wyczysc()
                rozgrywka.przydziel_karty(False)
                rozgrywka.odslon_karty()
                ekran.skaluj_menu_rozgrywki()
                ekran.skaluj_rozgrywke()
                zegar.uruchom_odnowa()
                zegar_ai.uruchom_odnowa()
                muzyka.odtworz("przetasowanie.wav")
                self.typ_zdarzen = typ_zdarzen
            #Dla opcji 3 Karty, tworzy rozgrywkie z 3 rozdaniem, skaluje rozgrywke i przechodzi do rozgrywki
            elif ekran.dialog2.zaznaczony(zdarzenie.pos):
                rozgrywka.wyczysc()
                rozgrywka.przydziel_karty(True)
                rozgrywka.odslon_karty()
                ekran.skaluj_menu_rozgrywki()
                ekran.skaluj_rozgrywke()
                zegar.uruchom_odnowa()
                zegar_ai.uruchom_odnowa()
                muzyka.odtworz("przetasowanie.wav")
                self.typ_zdarzen = typ_zdarzen
            #Dla opcji powrot
            elif ekran.dialog_powrot.zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_glowne()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 0
    #Funkcja obslugujaca zdarzenia rozgrywki
    def obsluga_zdarzen_rozgrywka(self, ekran, rozgrywka, zegar):
        pygame.event.pump()
        #Sprwdza, czy wygrano grę, jeśli tak zapisuje wynik i czar oraz oblicza bonus punktow za czas, po czym przechodzi do menu wygranej
        if rozgrywka.zwyciestwo():
            rozgrywka.czas = zegar.pobierz_czas()
            mnoznik = int(zegar.pobierz_sekundy() / 20)
            if rozgrywka.tryb == True:
                rozgrywka.bonus = 500 - 15 * mnoznik
            else:
                rozgrywka.bonus = 350 - 15 * mnoznik
            muzyka.odtworz("wygrana.wav")
            self.typ_zdarzen = 1.6
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        for zdarzenie in pygame.event.get():
            ekran.wyswietl_tlo()
            ekran.wyswietl_menu_rozgrywki(rozgrywka, zegar)
            ekran.karty_wspolrzedne(rozgrywka)
            ekran.wyswietl_rozgrywke(rozgrywka)
            pygame.display.flip()
            #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
            if zdarzenie.type == pygame.QUIT:
                ekran.wylacz_okno()
            #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
            elif zdarzenie.type == pygame.VIDEORESIZE:
                ekran.skaluj_okno(zdarzenie)
                ekran.skaluj_menu_rozgrywki()
                ekran.skaluj_rozgrywke()
            #Obsluguje zdarzenia myszy, dla rozgrywki, lewy klawisz myszy
            elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            #Zmienna sprawdzajaca czy jakas kolumna nie zostala juz nacisnieta
                nacisniety = True
            #Dla klikniecia w opcje z menu rozgrywki
                #Dla opcji ponów gra, skaluj okno dialogowe i przejdz do okna dialogowego pytającego czy rozpocząć gre od nowa
                if ekran.opcje[0].zaznaczony(zdarzenie.pos):
                    ekran.skaluj_menu_dialogowe()
                    zegar.pauza()
                    muzyka.odtworz("myszka.wav")
                    self.typ_zdarzen = 1.3
                #Dla opcji zapisz, skaluj okno dialogowe i przejd do okna dialogowego pytającego czy zapisać rozgrywkę
                elif ekran.opcje[1].zaznaczony(zdarzenie.pos):
                    ekran.skaluj_menu_dialogowe()
                    zegar.pauza()
                    muzyka.odtworz("myszka.wav")
                    self.typ_zdarzen = 1.4
                #Dla opcji powrot do menu głownego, skaluj okno dialogowe i przejdz do okna dialogowego
                elif ekran.opcje[2].zaznaczony(zdarzenie.pos):
                    ekran.skaluj_menu_dialogowe()
                    zegar.pauza()
                    muzyka.odtworz("myszka.wav")
                    self.typ_zdarzen = 1.5
                #Dla opcji cofnij cofa ostatni ruch i odejmuje lub dodaje punkty
                elif ekran.opcje[3].zaznaczony(zdarzenie.pos):
                    if rozgrywka.cofnij_ruch():
                        muzyka.odtworz("myszka.wav")
                        zegar.start()
                #Pokazanie kolejnej kolumny ze stosu kart rezerwowych
                elif ekran.tyl_przycisk[0].zaznaczony(zdarzenie.pos):
                    rozgrywka.zwieksz_rezerwowe()
                    zegar.start()
                    muzyka.odtworz("rezerwowe.wav")
                #Klikniecie lewym klawiszem myszy na ostatnia karte z kolumny rezerwowej
                elif len(rozgrywka.rezerwowe[rozgrywka.rez_indeks]) > 0:
                    muzyka.odtworz("podniesienie.wav")
                    kol = rozgrywka.rezerwowe[rozgrywka.rez_indeks][len(rozgrywka.rezerwowe[rozgrywka.rez_indeks]) - 1]
                    if rozgrywka.rez_indeks > -1 and ekran.karty_przycisk[kol[1]][kol[0]].zaznaczony(zdarzenie.pos):
                        #Dopoki myszka jest wcisnieta
                        while True:
                            #Czekaj na zdarzenia
                            pygame.event.pump()
                            zdarzenie = pygame.event.wait()
                            #W przypadku podniesienia lewego przycisku myszy, sprawdza, czy karta nie zostala upuszczona na, którejś z kolumn,
                            #jeśli tak wywołuje funkcje przeniesiena_jednej_karty, która przenosi karty jesli jest to zgodne z zasadami gry
                            if zdarzenie.type == pygame.MOUSEBUTTONUP and zdarzenie.button == 1:
                                #Dla kolumny bazowej
                                if ekran.baza_przycisk[kol[1]].najechany([ekran.karty_przycisk[kol[1]][kol[0]].x, ekran.karty_przycisk[kol[1]][kol[0]].y]):
                                    rozgrywka.przenies_jedna_karte(0)
                                    zegar.start()
                                    muzyka.odtworz("baza.wav")
                                    break
                                #Dla kolumny roboczej
                                for y in range(len(rozgrywka.robocze)):
                                    i = len(rozgrywka.robocze[y])
                                    #Dla kolumn roboczych pusty, jeśli zaznaczona przenosi karte bez porownania
                                    if i == 0 and ekran.robocze_przycisk[y].najechany([ekran.karty_przycisk[kol[1]][kol[0]].x, ekran.karty_przycisk[kol[1]][kol[0]].y]):
                                        rozgrywka.przenies_jedna_karte(0, y)
                                        zegar.start()
                                        muzyka.odtworz("opuszczenie.wav")
                                        break
                                    #Dla kolumn roboczych posiadajacych karty
                                    elif i > 0:
                                        if ekran.karty_przycisk[rozgrywka.robocze[y][i - 1][1]][rozgrywka.robocze[y][i - 1][0]].najechany([ekran.karty_przycisk[kol[1]][kol[0]].x, ekran.karty_przycisk[kol[1]][kol[0]].y]):
                                            rozgrywka.przenies_jedna_karte(0, y)
                                            zegar.start()
                                            muzyka.odtworz("opuszczenie.wav")
                                            break
                                break
                            #Zmienia wspolrzedzne karty, by podazala za kursorem
                            elif zdarzenie.type == pygame.MOUSEMOTION:
                                ekran.karty_przycisk[kol[1]][kol[0]].x = zdarzenie.pos[0] - int(ekran.karty_x * 0.5)
                                ekran.karty_przycisk[kol[1]][kol[0]].y = zdarzenie.pos[1] - int(ekran.karty_y * 0.5)
                                ekran.wyswietl_tlo()
                                ekran.wyswietl_menu_rozgrywki(rozgrywka, zegar)
                                ekran.wyswietl_rozgrywke(rozgrywka)
                                pygame.display.flip()
                            nacisniety = False
                #Klikniecie lewym klawiszem myszy na ostatnia karte ze stosu kart bazowych
                if nacisniety:
                    kol = None
                    b = 0
                    for i in range(4):
                        if ekran.baza_przycisk[i].zaznaczony(zdarzenie.pos) and len(rozgrywka.bazowe[i]) > 0:
                            kol = rozgrywka.bazowe[i][len(rozgrywka.bazowe[i]) - 1]
                            b = i
                    if kol is not None:
                        muzyka.odtworz("podniesienie.wav")
                        #Dopoki myszka jest wcisnieta
                        while True:
                            # Czekaj na zdarzenia
                            pygame.event.pump()
                            zdarzenie = pygame.event.wait()
                            # W przypadku podniesienia lewego przycisku myszy, sprawdza, czy karta nie zostala upuszczona na, którejś z kolumn,
                            # jeśli tak wywołuje funkcje przeniesiena_jednej_karty, która przenosi karty jesli jest to zgodne z zasadami gry
                            if zdarzenie.type == pygame.MOUSEBUTTONUP and zdarzenie.button == 1:
                                # Dla kolumny roboczej
                                for y in range(len(rozgrywka.robocze)):
                                    i = len(rozgrywka.robocze[y])
                                    # Dla kolumn roboczych pusty, jeśli zaznaczona przenosi karte bez porownania
                                    if i == 0 and ekran.robocze_przycisk[y].najechany([ekran.karty_przycisk[kol[1]][kol[0]].x, ekran.karty_przycisk[kol[1]][kol[0]].y]):
                                        rozgrywka.przenies_jedna_karte(2, b, y, 0)
                                        zegar.start()
                                        muzyka.odtworz("opuszczenie.wav")
                                        break
                                    # Dla kolumn roboczych posiadajacych karty
                                    elif i > 0:
                                        if ekran.karty_przycisk[rozgrywka.robocze[y][i - 1][1]][rozgrywka.robocze[y][i - 1][0]].najechany([ekran.karty_przycisk[kol[1]][kol[0]].x,ekran.karty_przycisk[kol[1]][kol[0]].y]):
                                            rozgrywka.przenies_jedna_karte(2, b, y)
                                            zegar.start()
                                            muzyka.odtworz("opuszczenie.wav")
                                            break
                                break
                            #Zmienia wspolrzedzne karty, by podazala za kursorem
                            elif zdarzenie.type == pygame.MOUSEMOTION:
                                ekran.karty_przycisk[kol[1]][kol[0]].x = zdarzenie.pos[0] - int(ekran.karty_x * 0.5)
                                ekran.karty_przycisk[kol[1]][kol[0]].y = zdarzenie.pos[1] - int(ekran.karty_y * 0.5)
                                ekran.wyswietl_tlo()
                                ekran.wyswietl_menu_rozgrywki(rozgrywka, zegar)
                                ekran.wyswietl_rozgrywke(rozgrywka)
                                pygame.display.flip()
                            nacisniety = False
                #Klikniecie lewym klawiszem myszy na karte ze stosu kart roboczych
                if nacisniety:
                    #robocza [kolumna, indeks pierwszej karty, ilosc kart]
                    robocza = None
                    for y in range(len(rozgrywka.robocze)):
                        for i in range(len(rozgrywka.robocze[y])):
                            #Zostala nacisnieta ostatnia karta z stosu kart roboczych
                            if i == len(rozgrywka.robocze[y]) - 1 and ekran.karty_przycisk[rozgrywka.robocze[y][i][1]][rozgrywka.robocze[y][i][0]].zaznaczony(zdarzenie.pos):
                                robocza = [y, i, 1]
                                break
                            #Zaznaczonych zostalo kilka kart z stosu kart roboczych
                            elif rozgrywka.robocze[y][i][2] == 1 and ekran.karty_przycisk[rozgrywka.robocze[y][i][1]][rozgrywka.robocze[y][i][0]].zaznaczona_karta(zdarzenie.pos):
                                robocza = [y, i, len(rozgrywka.robocze[y]) - i]
                                #Sprawdza, czy zachowana zostala starszenstwo w wybranych kartach, jesli nie czysci liste
                                for i in range (i, len(rozgrywka.robocze[y]) - 1):
                                    if not rozgrywka.porownaj_robocze(rozgrywka.robocze[y][i + 1], rozgrywka.robocze[y][i]):
                                        robocza = None
                                        break
                                break
                    if robocza is not None:
                        muzyka.odtworz("podniesienie.wav")
                        kol = rozgrywka.robocze[robocza[0]][robocza[1]]
                        #Dopoki myszka jest wcisnieta
                        while True:
                            # Czekaj na zdarzenia
                            pygame.event.pump()
                            zdarzenie = pygame.event.wait()
                            # W przypadku podniesienia lewego przycisku myszy, sprawdza, czy karta/karty nie zostala upuszczona na, którejś z kolumn,
                            # jeśli tak wywołuje funkcje przeniesiena_jednej_karty, która przenosi karty jesli jest to zgodne z zasadami gry
                            if zdarzenie.type == pygame.MOUSEBUTTONUP and zdarzenie.button == 1:
                                #Dla kolumny bazowej
                                if robocza[2] == 1 and ekran.baza_przycisk[kol[1]].najechany([ekran.karty_przycisk[kol[1]][kol[0]].x,ekran.karty_przycisk[kol[1]][kol[0]].y]):
                                    rozgrywka.przenies_jedna_karte(1, robocza[0])
                                    zegar.start()
                                    muzyka.odtworz("baza.wav")
                                    break
                                #Dla kolumny roboczej
                                for y in range(len(rozgrywka.robocze)):
                                    if y != robocza[0]:
                                        i = len(rozgrywka.robocze[y])
                                        # Dla kolumn roboczych pusty, jeśli zaznaczona przenosi karte bez porownania
                                        if i == 0 and ekran.robocze_przycisk[y].najechany([ekran.karty_przycisk[kol[1]][kol[0]].x, ekran.karty_przycisk[kol[1]][kol[0]].y]):
                                            rozgrywka.przenies_jedna_karte(1, robocza[0], y, robocza[2])
                                            zegar.start()
                                            muzyka.odtworz("opuszczenie.wav")
                                            break
                                        # Dla kolumn roboczych posiadajacych karty
                                        elif i > 0:
                                            if ekran.karty_przycisk[rozgrywka.robocze[y][i - 1][1]][rozgrywka.robocze[y][i - 1][0]].najechany([ekran.karty_przycisk[kol[1]][kol[0]].x, ekran.karty_przycisk[kol[1]][kol[0]].y]):
                                                rozgrywka.przenies_jedna_karte(1, robocza[0], y, robocza[2])
                                                zegar.start()
                                                muzyka.odtworz("opuszczenie.wav")
                                                break
                                break
                            #Zmienia wspolrzedzne karty/kart, by podazaly za kursorem
                            elif zdarzenie.type == pygame.MOUSEMOTION:
                                ekran.karty_przycisk[kol[1]][kol[0]].x = zdarzenie.pos[0] - int(ekran.karty_x * 0.5)
                                ekran.karty_przycisk[kol[1]][kol[0]].y = zdarzenie.pos[1] - int(ekran.karty_y * 0.5)
                                for i in range(robocza[1] + 1, robocza[1] + robocza[2]):
                                    prev = rozgrywka.robocze[robocza[0]][i - 1]
                                    next = rozgrywka.robocze[robocza[0]][i]
                                    ekran.karty_przycisk[next[1]][next[0]].x = ekran.karty_przycisk[prev[1]][prev[0]].x
                                    ekran.karty_przycisk[next[1]][next[0]].y = ekran.karty_przycisk[prev[1]][prev[0]].y + int(ekran.karty_y * 0.2)
                                ekran.wyswietl_tlo()
                                ekran.wyswietl_menu_rozgrywki(rozgrywka, zegar)
                                ekran.wyswietl_rozgrywke(rozgrywka, robocza[0])
                                pygame.display.flip()
            #Obsluguje zdarzenia myszy, dla rozgrywki, prawy przycisk myszy
            elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 3:
                #Klikniecie prawym klawiszem myszy na ostatnia karte z kolumny rezerwowej
                if len(rozgrywka.rezerwowe[rozgrywka.rez_indeks]) > 0:
                    kol = rozgrywka.rezerwowe[rozgrywka.rez_indeks][len(rozgrywka.rezerwowe[rozgrywka.rez_indeks]) - 1]
                    if rozgrywka.rez_indeks > -1 and ekran.karty_przycisk[kol[1]][kol[0]].zaznaczony(zdarzenie.pos):
                        rozgrywka.przenies_jedna_karte(0)
                        zegar.start()
                        muzyka.odtworz("baza.wav")
                #Klikniecie prawym klawiszem myszy na ostatnia karte z kolumny roboczej
                for y in range(len(rozgrywka.robocze)):
                    if len(rozgrywka.robocze[y]) != 0:
                        kol = rozgrywka.robocze[y][len(rozgrywka.robocze[y]) - 1]
                        if ekran.karty_przycisk[kol[1]][kol[0]].zaznaczony(zdarzenie.pos):
                            rozgrywka.przenies_jedna_karte(1, y)
                            muzyka.odtworz("baza.wav")
                            zegar.start()
    #Funkcja obslugujaca zdarzenia przywrocenia rozgrywki do wartosci domyślnych w czasie trwania rozgrywki
    def obsluga_zdarzen_rozgrywka_resetuj(self, ekran, rozgrywka, zegar):
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        zdarzenie = pygame.event.wait()
        #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
        if zdarzenie.type == pygame.QUIT:
            ekran.wylacz_okno()
        #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
        elif zdarzenie.type == pygame.VIDEORESIZE:
            ekran.skaluj_okno(zdarzenie)
            ekran.skaluj_menu_dialogowe()
        #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na opcje z okna dialogowego
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            #Dla opcji 1 resetuje rozgrywke, następnie skaluje rozgrywke i przechodzi do rozgrywki
            if ekran.dialog1.zaznaczony(zdarzenie.pos):
                rozgrywka.wyczysc()
                rozgrywka.resetuj()
                rozgrywka.odslon_karty()
                ekran.skaluj_menu_rozgrywki()
                ekran.skaluj_rozgrywke()
                ekran.karty_wspolrzedne(rozgrywka)
                zegar.uruchom_odnowa()
                muzyka.odtworz("przetasowanie.wav")
                self.typ_zdarzen = 1.2
            #Dla opcji 2 skaluje rozgrywke i powraca do poprzedniej rozgrywki
            elif ekran.dialog2.zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_rozgrywki()
                ekran.skaluj_rozgrywke()
                ekran.karty_wspolrzedne(rozgrywka)
                zegar.start()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 1.2
    #Funkcja obslugujaca zdarzenia zapisu obecnej rozgrywki do pliku rozgrywki w czasie trwania rozgrywki
    def obsluga_zdarzen_rozgrywka_zapisz(self, ekran, rozgrywka, zegar):
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        zdarzenie = pygame.event.wait()
        #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
        if zdarzenie.type == pygame.QUIT:
            ekran.wylacz_okno()
        #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
        elif zdarzenie.type == pygame.VIDEORESIZE:
            ekran.skaluj_okno(zdarzenie)
            ekran.skaluj_menu_dialogowe()
        #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na opcje z okna dialogowego
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            #Dla opcji 1 zapisuje rozgrywke, następnie skaluje rozgrywke i przechodzi do rozgrywki
            if ekran.dialog1.zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_rozgrywki()
                ekran.skaluj_rozgrywke()
                ekran.karty_wspolrzedne(rozgrywka)
                rozgrywka.czas = zegar.sekundy_poprzednie
                rozgrywka.zapisz_rozgrywke()
                zegar.start()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 1.2
            #Dla opcji 2 skaluje rozgrywke i powraca do poprzedniej rozgrywki
            elif ekran.dialog2.zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_rozgrywki()
                ekran.skaluj_rozgrywke()
                ekran.karty_wspolrzedne(rozgrywka)
                zegar.start()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 1.2
    #Funkcja obslugujaca zdarzenia okna dialogowego pytajacego czy powrocic z rozgrywki do menu glownego
    def obsluga_zdarzen_rozgrywka_menu_glowne(self, ekran, zegar, zegar_ai, typ_zdarzen = 1.2):
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        zdarzenie = pygame.event.wait()
        #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
        if zdarzenie.type == pygame.QUIT:
            ekran.wylacz_okno()
        #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
        elif zdarzenie.type == pygame.VIDEORESIZE:
            ekran.skaluj_okno(zdarzenie)
            ekran.skaluj_menu_dialogowe()
        #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na opcje z okna dialogowego
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            #Dla opcji Tak wylacza rozgrywke i powraca do menu glownego
            if ekran.dialog1.zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_glowne()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 0
            #Dla opcji Nie skaluje menu rozgrywki i powraca do poprzedniej rozgrywki
            elif ekran.dialog2.zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_rozgrywki()
                ekran.skaluj_rozgrywke()
                muzyka.odtworz("myszka.wav")
                if typ_zdarzen == 1.2:
                    zegar.start()
                zegar_ai.start()
                self.typ_zdarzen = typ_zdarzen
    #Obsluguje zdarzenie, wygrania gry przez gracza, wyświetla jego wynik, umożlwia mu wpisanie nazwy gracza
    #Po nacisnieciu klawisza enter, zapisuje do rankingu
    def obsluga_zdarzen_rozgrywka_wygrana(self, ekran, rozgrywka):
        #Iteruje przez kolejkę zdarzeń
        for zdarzenie in pygame.event.get():
            #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
            if zdarzenie.type == pygame.QUIT:
                ekran.wylacz_okno()
            #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
            elif zdarzenie.type == pygame.VIDEORESIZE:
                ekran.skaluj_okno(zdarzenie)
                ekran.skaluj_menu_dialogowe()
            #Obsluga klawiatury
            elif zdarzenie.type == pygame.KEYDOWN:
                klawisz = zdarzenie.key
                unicode = zdarzenie.unicode
                mod = zdarzenie.mod
                #Ograniczenie znaków w nazwie użytkownika
                if klawisz > 31 and klawisz != 32 and klawisz < 127 and len(rozgrywka.gracz) < 15:
                    if mod in (1, 2) and klawisz >= 97 and klawisz <= 122:
                        #wymusza małe litery
                        rozgrywka.gracz += chr(klawisz - 32)
                    elif mod == 0 and klawisz >= 97 and klawisz <= 122:
                        rozgrywka.gracz += chr(klawisz)
                    else:
                        #korzysta z znaków unicode
                        rozgrywka.gracz += unicode
                #Dla backspace kasuje litery
                elif klawisz == 8 and len(rozgrywka.gracz) > 0:
                    rozgrywka.gracz = rozgrywka.gracz[0:len(rozgrywka.gracz) - 1]
                #Dla przycisku enter dodaje gracza do rankingu i wraca do menu glownego
                elif klawisz == 13 and len(rozgrywka.gracz) > 0 and rozgrywka.gracz != "Komputer":
                    rozgrywka.zapisz_ranking()
                    ekran.skaluj_menu_glowne()
                    self.typ_zdarzen = 0
            #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na opcje powrotu
            elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
                #Dla opcji Powrot wylacza rozgrywke i powraca do menu glownego
                if ekran.dialog_powrot.zaznaczony(zdarzenie.pos):
                    ekran.skaluj_menu_glowne()
                    muzyka.odtworz("myszka.wav")
                    self.typ_zdarzen = 0
    #Funkcja obslugujaca zdarzenie wczytywania gry
    def obsluga_zdarzen_wczytaj(self, ekran, rozgrywka, zegar):
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        zdarzenie = pygame.event.wait()
        #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
        if zdarzenie.type == pygame.QUIT:
            ekran.wylacz_okno()
        #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
        elif zdarzenie.type == pygame.VIDEORESIZE:
            ekran.skaluj_okno(zdarzenie)
            ekran.skaluj_menu_dialogowe()
        #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na powrot do menu glownego
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            #Dla opcji Tak sprawdza, czy mozna wczytac rozgrywke, jesli tak wczytuje ja i przechodzi do rozgrywki
            if ekran.dialog1.zaznaczony(zdarzenie.pos):
                if rozgrywka.wczytaj_sprawdz():
                    rozgrywka.wczytaj_rozgrywke(zegar)
                    ekran.skaluj_menu_rozgrywki()
                    ekran.skaluj_rozgrywke()
                    zegar.pauza()
                    muzyka.odtworz("przetasowanie.wav")
                    self.typ_zdarzen = 1.2
            #Dla opcji Nie skaluje okno i menu i powraca do menu glownego
            elif ekran.dialog2.zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_glowne()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 0
    #Funkcja obslugujaca zdarzenia rozgrywki, dla ai
    def obsluga_zdarzen_rozgrywka_ai(self, ekran, rozgrywka, zegar, zegar_ai, zdarzenia):
        #Sprwdza, czy komputer wygrał grę, jeśli tak zapisuje wynik i czar oraz oblicza bonus punktow za czas, po czym przechodzi do menu głównego
        #Nazwą gracza w tym przypadku będzie Komputer
        if rozgrywka.zwyciestwo():
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
            rozgrywka.czas = czas
            mnoznik = int(zegar.pobierz_sekundy() / 20)
            if rozgrywka.tryb == True:
                rozgrywka.bonus = 500 - 15 * mnoznik
            else:
                rozgrywka.bonus = 350 - 15 * mnoznik
            rozgrywka.gracz = "Komputer"
            rozgrywka.zapisz_ranking()
            rozgrywka.gracz = "Wygrana"
            rozgrywka.czas = zegar.sekundy
            ekran.skaluj_menu_autora()
            muzyka.odtworz("wygrana.wav")
            self.typ_zdarzen = 2.4
            return
        #Pobiera czas
        zegar.pobierz_czas()
        #Dodaje do zegara_ai roznice czasu spowodowany, wywołaniem funkcji pobierz_czas() przez zegar
        zegar_ai.sekundy += zegar.stoper.get_rawtime() / 1000.0
        #Co 4 sekundy, wywołuje funkcję podejmującą decyzję, którą karte należy przenieść lub, czy przewinąć stos kart rezerwowych
        if zegar_ai.podejmij_decyzje(1):
            if not rozgrywka.sztuczna_inteligencja(zdarzenia):
                rozgrywka.czas = zegar.sekundy
                ekran.skaluj_menu_autora()
                return
        # Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        for zdarzenie in pygame.event.get():
            ekran.wyswietl_tlo()
            ekran.wyswietl_menu_rozgrywki_ai(rozgrywka, zegar)
            ekran.karty_wspolrzedne(rozgrywka)
            ekran.wyswietl_rozgrywke(rozgrywka)
            pygame.display.flip()
            #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
            if zdarzenie.type == pygame.QUIT:
                ekran.wylacz_okno()
                #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
            elif zdarzenie.type == pygame.VIDEORESIZE:
                ekran.skaluj_okno(zdarzenie)
                ekran.skaluj_menu_rozgrywki()
                ekran.skaluj_rozgrywke()
            #Obsluguje zdarzenia myszy, dla rozgrywki ai, lewy klawisz myszy
            elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
                #Dla opcji powrot do menu głownego, skaluj okno dialogowe i przejdz do okna dialogowego
                if ekran.opcje[0].zaznaczony(zdarzenie.pos):
                    ekran.skaluj_menu_dialogowe()
                    zegar.pauza()
                    zegar_ai.pauza()
                    muzyka.odtworz("myszka.wav")
                    self.typ_zdarzen = 2.3
    def obsluga_zdarzen_ranking(self, ekran):
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        zdarzenie = pygame.event.wait()
        #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
        if zdarzenie.type == pygame.QUIT:
            ekran.wylacz_okno()
        #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
        elif zdarzenie.type == pygame.VIDEORESIZE:
            ekran.skaluj_okno(zdarzenie)
            ekran.skaluj_menu_dialogowe()
        #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na powrot do menu glownego
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            #Dla opcji powrot skaluje okno i menu i powraca do menu glownego
            if ekran.dialog_powrot.zaznaczony(zdarzenie.pos):
                ekran.skaluj_menu_glowne()
                muzyka.odtworz("myszka.wav")
                self.typ_zdarzen = 0
    #Funkcja obslugujaca zdarzenie, wyswietlenia autora
    def obsluga_zdarzen_autor(self, ekran):
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        for zdarzenie in pygame.event.get():
            #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
            if zdarzenie.type == pygame.QUIT:
                ekran.wylacz_okno()
            #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
            elif zdarzenie.type == pygame.VIDEORESIZE:
                ekran.skaluj_okno(zdarzenie)
                ekran.skaluj_menu_autora()
            #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na powrot do menu glownego
            elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
                #Dla opcji powrot skaluje okno i menu i powraca do menu glownego
                if ekran.autor_powrot.zaznaczony(zdarzenie.pos):
                    ekran.skaluj_menu_glowne()
                    muzyka.odtworz("myszka.wav")
                    self.typ_zdarzen = 0
    def obsluga_zdarzen_wygrana_ai(self, ekran):
        #Odwoluje sie do kolejki zdarzen
        pygame.event.pump()
        #Oczekuje na zdarzenie, jesli oczekiwanie sie zakonczy przypisuje zdarzenie do zmiennej
        for zdarzenie in pygame.event.get():
            #W przypadku nacisniecia przycisku wylaczenia okna, konczy dzialanie programu
            if zdarzenie.type == pygame.QUIT:
                ekran.wylacz_okno()
            #W przypadku zmiany rozmiaru okna, skaluje rozmiar okna
            elif zdarzenie.type == pygame.VIDEORESIZE:
                ekran.skaluj_okno(zdarzenie)
                ekran.skaluj_menu_autora()
            #Obsluguje zdarzenia, nacisniecia lewym klawiszem myszy, na powrot do menu glownego
            elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
                #Dla opcji powrot skaluje okno i menu i powraca do menu glownego
                if ekran.dialog_powrot.zaznaczony(zdarzenie.pos):
                    ekran.skaluj_menu_glowne()
                    muzyka.odtworz("myszka.wav")
                    self.typ_zdarzen = 0