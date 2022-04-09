import Generator
import pandas as pd
import numpy as np


class Interfejs:
    def __init__(self):
        print('Witaj w zadaniu nr 5. W czym mogę pomóc?')
        self.opcje = ['sinusoidalny', 'prostokątny', 'piłokształtny', 'trójkątny', 'biały szum', 'koniec']
        self.dzialania = ['narysuj wykres przebiegu', 'narysuj transformatę Fourierra',
                          'zapisz przebieg jako plik wav', 'wróć']
        self.wyboruzytkownika = 0
        self.wybordzialania = 0
        self.generator = Generator.Generator(0, 10, 100000)
        self.f = 0
        self.amp = -1
        self.wysw_opcje()

    def wysw_opcje(self):

        for i in range(1, len(self.opcje)+1):
            print(i, ":", 'przebieg', self.opcje[i-1], '-->', i)
        self.menu_opcji()

    def menu_opcji(self):
        self.wyboruzytkownika = input()
        for i in range(1, len(self.opcje)+1):
            if int(self.wyboruzytkownika) == i:
                self.switch_opcji(i)
        print('nieznana opcja:', self.wyboruzytkownika, 'spróbuj jeszcze raz')
        self.menu_opcji()

    def switch_opcji(self, i):
        a = 1
        amp = 0
        if i == 6:
            exit(0)
        print('podaj potrzebne parametry:')
        if i < 5:
            boolf = True
            boolamp = True
            while a == 1:
                try:
                    while boolf:
                        self.f = float(input('częstotliwość(w przedziale 20-15000): '))
                        if self.f < 20 or self.f > 15000:
                            print('podaj liczbę z przedziału 20-15 000!')
                        else:
                            boolf = False
                    a = 0
                except ValueError:
                    print('podaj liczbę dodatnią')
            while a == 0:
                try:
                    while boolamp:
                        self.amp = float(input('amplituda(w przedziale 0-1): '))
                        if self.amp <= 0 or self.amp > 1:
                            print('podaj liczbę z przedziału 0-1')
                        else:
                            boolamp = False
                    a = 1
                except ValueError:
                    print('podaj liczbę z zakresu 0-1')
            if i == 1:
                self.generator.sine(self.f, self.amp)
            elif i == 2:
                self.generator.square(self.f, self.amp)
            elif i == 3:
                self.generator.sawtooth(self.f, self.amp)
            elif i == 4:
                self.generator.triangle(self.f, self.amp)
        elif i == 5:
            boolamp = True
            while a == 0:
                try:
                    while boolamp:
                        self.amp = float(input('amplituda(w przedziale 0-1): '))
                        if self.amp <= 0 or self.amp > 1:
                            print('podaj liczbę z przedziału 0-1')
                        else:
                            boolamp = False
                    a = 1
                except ValueError:
                    print('podaj liczbę z zakresu 0-1')
            self.f = 440
            self.generator.white_noise(amp)
        self.wysw_dzialania()

    def wysw_dzialania(self):
        for i in range(1, len(self.dzialania) + 1):
            print(i, ":", self.dzialania[i - 1], '-->', i)
        self.menu_dzialania()

    def menu_dzialania(self):
        self.wybordzialania = input()
        for i in range(1, len(self.dzialania) + 1):
            if int(self.wybordzialania) == i:
                self.switch_dzialania(i)
        print('nieznana opcja:', self.wybordzialania, 'spróbuj jeszcze raz')
        self.menu_dzialania()

    def switch_dzialania(self, i):
        if i == 1:
            self.generator.show_plot(self.f)
        if i == 2:
            dane = pd.read_csv(r"function.csv", sep="\t")
            y = np.int16(dane['y'])
            self.generator.save_ttf(y)
            self.generator.show_ttf()
        if i == 3:
            self.generator.save_function_to_wav(input('podaj nazwę pliku wraz z rozszerzeniem: '))
        if i == 4:
            self.wysw_opcje()
        self.wysw_dzialania()


menu = Interfejs()
