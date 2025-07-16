# main_generator.py
import random
# TODO 3: Importiere die Funktionen 'find_max' und 'remove_duplicates'
# aus deinem eigenen Modul 'list_utils'.
from list_utils import find_max
from list_utils import remove_duplicates

def generate_random_numbers(count, min_val, max_val):
    """
    Generiert eine Liste von Zufallszahlen.
    """
    numbers = []
    # TODO 4: Generiere 'count' viele Zufallszahlen zwischen 'min_val' und 'max_val'
    # und füge sie der Liste 'numbers' hinzu. Nutze random.randint().
    for zahl in range(count):
        numbers.append(random.randint(min_val, max_val))
    return numbers
    pass

if __name__ == "__main__":
    print("Willkommen zum Zufallszahlen-Generator und Listen-Helfer!")

    # TODO 5: Generiere eine Liste mit 10 Zufallszahlen zwischen 1 und 50.
    random_list = generate_random_numbers(10, 1, 50)
    print(f"Generierte Zahlen in Liste: {random_list}")

    # TODO 6: Finde die größte Zahl in der generierten Liste und gib sie aus.
    print(f"Die groesste Zahl ist:{find_max(random_list)}")


    # TODO 7: Erstelle eine Liste mit Duplikaten zum Testen.
    duplicates_in_list = [1, 1, 3, 2, 2, 6, 8, 4, 3, 5, 9]
    print(f"Liste mit Duplikaten:{duplicates_in_list}")

    # TODO 8: Entferne Duplikate aus der Liste und gib die bereinigte Liste aus.
    list_without_duplicates = remove_duplicates(duplicates_in_list)
    print(f"Duplikate entfernt:{list_without_duplicates}")

    #print("Bitte implementieren Sie die TODOs, um die App zu starten!")