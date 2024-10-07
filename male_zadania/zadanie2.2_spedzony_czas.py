# Slownik do przechowywania danych o aktywnosciach i czasie
aktywnosci = {}

def dodaj_aktywnosc(nazwa_aktywnosci, czas):
    """
    Funkcja dodaje czas do istniejącej aktywności lub tworzy nową.
    Argumenty:
    nazwa_aktywnosci - nazwa aktywności do dodania/aktualizacji
    czas - czas spędzony na aktywności (w minutach)
    """
    if nazwa_aktywnosci in aktywnosci.keys():
        aktywnosci[nazwa_aktywnosci].append(czas)
    else:
        aktywnosci[nazwa_aktywnosci] = [czas]
    
    print(f"Dodano {czas} minut do aktywności '{nazwa_aktywnosci}'.")

def pokaz_czas(nazwa_aktywnosci): 
    """
    Wyświetla całkowity czas spędzony na wybranej aktywności.
    Argument:
    nazwa_aktywnosci - nazwa aktywności do sprawdzenia
    """
    if nazwa_aktywnosci in aktywnosci:
        laczny_czas = sum(aktywnosci[nazwa_aktywnosci])
        print(f"Całkowity czas spędzony na '{nazwa_aktywnosci}': {laczny_czas} minut.")
    else:
        print(f"Aktywność '{nazwa_aktywnosci}' nie została jeszcze dodana.")

def pokaz_top_aktywnosci():
    """
    Wyświetla top 3 aktywności, na które użytkownik spędził najwięcej czasu.
    """
    if len(aktywnosci) == 0:
        print("Nie dodano żadnych aktywności.")
        return
    sumy_czasu = {nazwa: sum(czasy) for nazwa, czasy in aktywnosci.items()}    
    top_3 = sorted(sumy_czasu.items(), key=lambda item: item[1], reverse=True)[:3]
    print("Top 3 aktywnosci, na ktorych uzytkownik spedzil najwiecej czasu:")
    
    for i, (nazwa, czas) in enumerate(top_3):
        print(f"{i+1}. Aktywnosc: {nazwa}, Czas: {czas} minut")