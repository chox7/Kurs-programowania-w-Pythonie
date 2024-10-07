import random
import math

def estimate_pi(N, K):
    """
    Funkcja oszacowuje wartość Pi metodą Monte Carlo. 
    Argumenty:
    N - liczba iteracji
    K - krok
    """
    if K > N:
        print("Krok nie może być większy niż liczba iteracji.")
        return

    inside_circle = 0

    for i in range(1, N + 1):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Sprawdzenie, czy punkt jest w ćwiartce koła
        if x**2 + y**2 <= 1:
            inside_circle += 1

        # Wyświetlenie przybliżonej wartości pi co K iteracji
        if i % K == 0:
            pi_estimate = (inside_circle / i) * 4
            print(f"Po {i} iteracjach: przybliżona wartość pi = {pi_estimate}") 
        
    # Ostateczne przybliżenie po N iteracjach
    final_estimate = (inside_circle / N) * 4
    comparison = final_estimate - math.pi
    print(f"\nOstateczne przybliżenie dla N={N}: {final_estimate}")
    print(f"Różnica względem math.pi: {comparison}")

# Wczytywanie danych od użytkownika
N = int(input("Podaj liczbę iteracji: "))
K = int(input("Podaj krok: "))
estimate_pi(N, K)