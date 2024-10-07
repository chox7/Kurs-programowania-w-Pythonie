def tekstPowitania(jezyk):
    """
    Funkcja generuje tekst powitania w odpowiednim jezyku podanym jako parametr.
    """
    slownik_powitan = {
        'en': "Hello",    # angielski
        'it': "Ciao",     # wloski
        'de': "Hallo",    # niemiecki
        'fr': "Bonjour"   # francuski
    }

    if jezyk in slownik_powitan.keys():
        return slownik_powitan[jezyk] + "!"
    else:
        return "Nie znam jezyka: " + jezyk + "."


def powitanie():
    """
    Funkcja odpowiedzialna za dialog z uzytkownikiem i wypisanie powitania.
    """
    jezyk = input("Podaj jezyk: ")
    tekst = tekstPowitania(jezyk)
    print(tekst)

powitanie()