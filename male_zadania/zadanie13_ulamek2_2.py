import math
import random
import time

class Ułamek:
    __slots__ = ('licznik', 'mianownik')

    def __init__(self, licznik, mianownik):
        assert mianownik != 0, "Mianownik nie może być zerem."
        self.licznik = int(licznik)
        self.mianownik = int(mianownik)
        self.przekształć()

    def przekształć(self):
        if self.licznik == 0:
            self.mianownik = 1
        else:
            gcd = math.gcd(self.licznik, self.mianownik)
            self.licznik //= gcd
            self.mianownik //= gcd

            if self.mianownik < 0:
                self.licznik = -self.licznik
                self.mianownik = -self.mianownik

    def __add__(self, other):
        licznik = self.licznik * other.mianownik + other.licznik * self.mianownik
        mianownik = self.mianownik * other.mianownik
        return Ułamek(licznik, mianownik)

    def __str__(self):
        if self.mianownik == 1:
            return f"{self.licznik}"
        return f"{self.licznik}/{self.mianownik}"

    __repr__ = __str__


def main():
    # Wczytywanie danych
    n = int(input("Podaj liczbę ułamków (n): "))
    k = int(input("Podaj liczbę operacji (k): "))

    # Generowanie n ułamków
    ułamki = [Ułamek(random.randint(1, 100), random.randint(1, 100)) for _ in range(n)]

    # Wykonanie k operacji
    for _ in range(k):
        for i in range(n):
            ułamki[i] += ułamki[(i + 1) % n]  # Cykliczne dodawanie

if __name__ == "__main__":
    main()