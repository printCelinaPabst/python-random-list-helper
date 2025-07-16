# list_utils.py
def find_max(numbers):
    """Findet die größte Zahl in einer Liste."""
    # TODO 1: Implementiere die Logik, um die größte Zahl zu finden.
    # Tipp: Du kannst die eingebaute Funktion max() verwenden.
    max_number = max(numbers)
    return max_number
    pass

def remove_duplicates(items):
    """Entfernt Duplikate aus einer Liste und gibt eine neue Liste zurück."""
    # TODO 2: Implementiere die Logik zum Entfernen von Duplikaten.
    # Tipp: Ein Set kann verwendet werden, um Duplikate zu entfernen.
    removed_duplicates = list(set(items))
    return removed_duplicates

    pass