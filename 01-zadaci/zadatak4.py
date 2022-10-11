# Funkcija prima dvije liste, provjerava dal su istih duljina, ako nisu raise-a
# Error. Vraća novu listu uspoređujući elemente na istim indeksima. Ako
# su vrijednosti iste, vraća taj element, ako nisu vraća -1 na toj poziciji.
# (Funkcija mora imati dvije linije)
# Ispis: [1,2,3,4,5],[2,2,4,4,5] -> [-1, 2, -1, 4, 5]


def check(lista1, lista2):
       return [ x if x==lista2[y]  else -1 for y, x in enumerate(lista1)] if len(lista1) == len(lista2) else "error"

lista1 = [1,2,3,4,5]
lista2 = [2,2,4,4,5,5]

print(check(lista1,lista2))