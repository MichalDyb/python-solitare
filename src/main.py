#Import wszystkich potrzebnych klas skladowych projektu
from moje_klasy.Okno import Okno
from moje_klasy.Rozgrywka import *
from moje_klasy.Zdarzenia import *
from moje_klasy.Zegar import *


#Utworzenie obiektu klasy ekran, zdarzenia i zegar
ekran = Okno()
zdarzenia = Zdarzenia()
zegar = Zegar()
#Zegar wykorzystywany dla sztucznej inteligencji, w celu zapewnienia, że decyzje będą podejmowane co określony czas
zegar_ai = Zegar()
#Utworzenie zmiennych stanowiacych pozniej referencje do nowo utworzonego obiektu rozgrywki i jego kopi
rozdanie = Rozgrywka()
#Utworzenie nowego okna
ekran.utworz_okno()
#Wyswietlenie okna ładowania i skalowanie grafik kart
ekran.skaluj_menu_dialogowe()
ekran.wyswietl_tlo()
ekran.wyswietl_menu_dialogowe("Uruchamianie", x = 0)
pygame.display.flip()
ekran.skaluj_rozgrywke()
#Petla warunkujaca dzialanie programu, do czasu jego wylaczenia przez uzytkownika
while True:
    #Menu glowne, okno domyslne, wyswietla menu glowne i pozwala wybrac jedna z kilku opcji
    if zdarzenia.typ_zdarzen == 0:
        #Obsluguje zdarzenia dla menu glownego i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_menu_glowne(ekran)
        ekran.wyswietl_tlo()
        ekran.wyswietl_menu_glowne()
        pygame.display.flip()
    #Okno dialogowy, upewniające się, czy na pewno wyłączyć gre
    elif zdarzenia.typ_zdarzen == 0.1:
        #Obsluguje zdarzenia dla okna dialogoweg i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_wylacz(ekran)
        ekran.wyswietl_tlo()
        ekran.wyswietl_menu_dialogowe("Na pewno?", "Tak", "Nie")
        pygame.display.flip()
    #Tworzenie nowej gry
    elif zdarzenia.typ_zdarzen == 1.1:
        #Obsloguje zdarzenia dla okna tworzenia nowej rozgrywki i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_nowa_gra(ekran, rozdanie, zegar, zegar_ai)
        ekran.wyswietl_tlo()
        ekran.wyswietl_menu_dialogowe("Wybierz rozdanie:", "1 Karta", "3 Karty", "Powrot")
        pygame.display.flip()
    #Rozgrywka
    elif zdarzenia.typ_zdarzen == 1.2:
        #Obsloguje zdarzenia dla okna rozgrywki i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_rozgrywka(ekran, rozdanie, zegar)
        ekran.wyswietl_tlo()
        ekran.wyswietl_menu_rozgrywki(rozdanie, zegar)
        ekran.karty_wspolrzedne(rozdanie)
        ekran.wyswietl_rozgrywke(rozdanie)
        pygame.display.flip()
    #Resetowanie rozgrywki
    elif zdarzenia.typ_zdarzen == 1.3:
        #Obsluguje zdarzenia dla okna tworzenia resetowania i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_rozgrywka_resetuj(ekran, rozdanie, zegar)
        ekran.wyswietl_tlo()
        ekran.wyswietl_menu_dialogowe("Na pewno?", "Tak", "Nie")
        pygame.display.flip()
    #Zapisywanie rozgrywki
    elif zdarzenia.typ_zdarzen == 1.4:
        #Obsluguje zdarzenia dla okna tworzenia resetowania i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_rozgrywka_zapisz(ekran, rozdanie, zegar)
        ekran.wyswietl_tlo()
        ekran.wyswietl_wiadomosc((155, 55, 55), ekran.dialog_etykieta, "Uwaga, poprzedni zapis, zostanie nadpisany!", 3, 0, -15)
        ekran.wyswietl_menu_dialogowe("Na pewno?", "Tak", "Nie")
        pygame.display.flip()
    #Okno dialogowy, upewniające się, czy na pewno powrócić do menu głównego
    elif zdarzenia.typ_zdarzen == 1.5:
        #Obsluguje zdarzenia dla okna dialogoweg i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_rozgrywka_menu_glowne(ekran, zegar, zegar_ai)
        ekran.wyswietl_tlo()
        ekran.wyswietl_menu_dialogowe("Na pewno?", "Tak", "Nie")
        pygame.display.flip()
    #Ekran, dla wygranego rozdania, wyświetla wynik, umożlwia wpisanie nazwy gracza i wpisanie jej do rankingu
    elif zdarzenia.typ_zdarzen == 1.6:
        #Obsluguje zdarzenia dla wygranego rozdania
        zdarzenia.obsluga_zdarzen_rozgrywka_wygrana(ekran, rozdanie)
        ekran.wyswietl_tlo()
        ekran.skaluj_menu_dialogowe()
        ekran.wyswietl_menu_wygrana("Wygrana", "Wynik: " + str(rozdanie.wynik), "Bonus za czas: " + str(rozdanie.bonus), "Czas: " + rozdanie.czas, rozdanie.gracz)
        pygame.display.flip()
    #Wyswietlenie wczytywania rozgrywki
    elif zdarzenia.typ_zdarzen == 1.7:
        #Obsluguje zdarzenia dla opcji wczytaj rozgrywke i wyswietla jego zawartosc
        rozdanie.resetuj()
        zdarzenia.obsluga_zdarzen_wczytaj(ekran, rozdanie, zegar)
        ekran.wyswietl_tlo()
        ekran.skaluj_menu_dialogowe()
        if not rozdanie.wczytaj_sprawdz():
            ekran.wyswietl_wiadomosc((155, 55, 55), ekran.dialog_etykieta, "Brak zapisanej gry!", 3, 0, -15)
        ekran.wyswietl_menu_dialogowe("Wczytywanie", "Tak", "Nie")
        pygame.display.flip()
    #Tworzenie nowej gry, dla AI
    elif zdarzenia.typ_zdarzen == 2.1:
        #Obsloguje zdarzenia dla okna tworzenia nowej rozgrywki, dla AI i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_nowa_gra(ekran, rozdanie, zegar, zegar_ai, 2.2)
        ekran.wyswietl_tlo()
        ekran.wyswietl_menu_dialogowe("Wybierz rozdanie:", "1 Karta", "3 Karty", "Powrot")
        pygame.display.flip()
    #Rozgrywka AI
    elif zdarzenia.typ_zdarzen == 2.2:
        #Obslguje zdarzenia dla okna rozgrywki ai i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_rozgrywka_ai(ekran, rozdanie, zegar, zegar_ai, zdarzenia)
        ekran.wyswietl_tlo()
        ekran.wyswietl_menu_rozgrywki_ai(rozdanie, zegar)
        ekran.karty_wspolrzedne(rozdanie)
        ekran.wyswietl_rozgrywke(rozdanie)
        pygame.display.flip()
    #Okno dialogowe, upewniające się, czy na pewno powrócić do menu głównego
    elif zdarzenia.typ_zdarzen == 2.3:
        #Obsluguje zdarzenia dla okna dialogoweg i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_rozgrywka_menu_glowne(ekran, zegar, zegar_ai, 2.2)
        ekran.wyswietl_tlo()
        ekran.wyswietl_menu_dialogowe("Na pewno?", "Tak", "Nie")
        pygame.display.flip()
    #Wyświetlenie okna informującego o wygranej, lub przegranej sztucznej inteligencji
    elif zdarzenia.typ_zdarzen == 2.4:
        zdarzenia.obsluga_zdarzen_wygrana_ai(ekran)
        ekran.skaluj_menu_autora()
        ekran.wyswietl_tlo()
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
        ekran.wyswietl_menu_wygrana_ai("Wynik: " + str(rozdanie.wynik), "Bonus za czas: " + str(rozdanie.bonus), "Czas: " + czas, rozdanie.gracz)
        pygame.display.flip()
    #Wyswietlenie rankingu
    elif zdarzenia.typ_zdarzen == 3:
        #Obsluguje zdarzenia dla opcji autor i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_ranking(ekran)
        ekran.wyswietl_tlo()
        ekran.skaluj_menu_dialogowe()
        ekran.wyswietl_menu_ranking()
        pygame.display.flip()
    #Wyswietlenie autora gry
    elif zdarzenia.typ_zdarzen == 4:
        #Obsluguje zdarzenia dla opcji autor i wyswietla jego zawartosc
        zdarzenia.obsluga_zdarzen_autor(ekran)
        ekran.wyswietl_tlo()
        ekran.wyswietl_menu_autora()
        pygame.display.flip()

while True:
    x = 5