
# Funkcija uzima listu string-ova. Provjeri dal su sve stringovi, ako ne error.
# Vraća novu listu, gdje su string-ovi duži od 4 znaka. (Funkcija od dvije
# linije)
# Ispis: [“Pas”, “Macka”, “Stol”] -> [“Macka”]


def check(lista):
    return [x for x in lista if isinstance(x, str) and len(x) > 4] if all([isinstance(x, str) for x in lista]) else "error"

lista = ['Pas', 'Macka', 'Stol']

print(check(lista))