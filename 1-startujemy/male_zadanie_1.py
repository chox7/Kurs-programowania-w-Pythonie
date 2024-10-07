"""
Oszacować wartość Pi metodą Monte Carlo.

Użytkownik podaje ilość iteracji (N) i krok (K). Program wypisuje wartość 
przybliżenia dla kolejnych kroków (K, 2K, … < N). Na koniec porównuje wartość 
przybliżenia dla N z wartością math.pi.

Wskazówka. Okręg o środku w 0,0 i promieniu r=1. Losujemy wartości współrzędnych
x i y n razy i sprawdzamy, ile wylosowanych punktów jest w ćwiartce okręgu.
"""

import random

def main():
    N = int(input("Podaj ilość iteracji: "))
    K = int(input("Podaj krok: "))
    inside = 0
    for i in range(N * K, K):
        random.
