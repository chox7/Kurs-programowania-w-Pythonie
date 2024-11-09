import math

class Ułamek:
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
        mianownik =  self.mianownik * other.mianownik
        return Ułamek(licznik, mianownik)
    
    def __sub__(self, other):
        licznik = self.licznik * other.mianownik - other.licznik * self.mianownik
        mianownik =  self.mianownik * other.mianownik
        return Ułamek(licznik, mianownik)
    
    def __mul__(self, other):
        licznik = self.licznik * other.licznik 
        mianownik =  self.mianownik * other.mianownik
        return Ułamek(licznik, mianownik)

    def __truediv__(self, other):
        assert other.licznik != 0, "Nie można dzielić przez zero."
        licznik = self.licznik * other.mianownik 
        mianownik =  self.mianownik * other.licznik
        return Ułamek(licznik, mianownik)
    
    def __eq__(self, other):
        return self.licznik * other.mianownik == other.licznik * self.mianownik

    def __lt__(self, other):
        return self.licznik * other.mianownik < other.licznik * self.mianownik

    def __le__(self, other):
        return self.licznik * other.mianownik <= other.licznik * self.mianownik

    def __gt__(self, other):
        return self.licznik * other.mianownik > other.licznik * self.mianownik

    def __ge__(self, other):
        return self.licznik * other.mianownik >= other.licznik * self.mianownik

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        if self.mianownik == 1:
            return f"{self.licznik}"
        return f"{self.licznik}/{self.mianownik}"

    __repr__ = __str__

if __name__ == '__main__':
    u1 = Ułamek(2, 3)  
    u2 = Ułamek(4, 6)  

    # Dodawanie
    assert (u1 + u2) == Ułamek(4, 3) 

    # Odejmowanie
    assert (u1 - u2) == Ułamek(0, 1)  

    # Mnożenie
    assert (u1 * u2) == Ułamek(4, 9) 

    # Dzielenie
    assert (u1 / u2) == Ułamek(1, 1) 

    # Porównania
    assert u1 == u2  
    assert u1 != Ułamek(1, 3)  
    assert u1 < Ułamek(5, 6)  
    assert u2 > Ułamek(1, 3)  
    assert u1 <= Ułamek(5, 6)  
    assert u1 >= Ułamek(1, 3)  

    print("Wszystkie testy przeszły pomyślnie.")