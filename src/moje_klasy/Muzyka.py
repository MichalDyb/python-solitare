#Zaimportowanie bliblioteki pygame i funkcji path z biblioteki os
import pygame
from os import path
#Klasa przechowujaca dzwieki gry i umozliwiajaca ich odtwarzaniec
class Muzyka:
    sciezka = path.join(path.split(path.dirname(__file__))[0], "moje_dzwieki")
    #Funkcja pobierajaca nazwe pliku dzwiekowego i odtworzenie go jeden raz
    def odtworz(self, nazwa):
        dzwiek = pygame.mixer.Sound(path.join(self.sciezka, nazwa))
        dzwiek.play()