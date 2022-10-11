# Funkcija uzima listu dictionary-a o artiklima. Provjerava je li parametar
# lista, ak ne error. Provjerava jesu li svi elementi dictionary, ako ne error.
# Provjerava imaju li svi dictionary odgovarajuća 3 ključeva, ako ne error.
# (“cijena”,“naziv”,“kolicina”) (Moze i u dvije linije) Vraća novi nested
# dictionary s ključem “ukupno” i dictionary sa ključem “artikli” i listom
# svih odabranih artikala te “cijena” s ukupnom cijenom računa. (Ne treba
# biti One-liner)
# Ispis: [{“cijena”:8,“naziv”:“Kruh”,“kolicina”:1}, {“cijena”:13,“naziv”:“Sok”,“kolicina”:2},
# {“cijena”:7,“naziv”:“Upaljac”,“kolicina”:1}] -> {‘ukupno’: {‘artikli’:
# [‘Kruh’, ‘Sok’, ‘Upaljac’], ‘cijena’: 57}}

def check(lista):
    lis = ['cijena', 'naziv', 'kolicina']
    rez = {"ukupno": {"artikli":[], "cijena":0}}
    if isinstance(lista, list):
        if all([isinstance(x, dict) for x in lista]):
            if all([list(x.keys()) == lis for x in lista]):
                for x in lista:
                    rez["ukupno"]['artikli'].append(x['naziv'])
                    rez['ukupno']['cijena'] +=  x['kolicina'] * x['cijena']
                return rez




lista = [{"cijena":8,"naziv":"Kruh","kolicina":1},
         {"cijena":13,"naziv":"Sok","kolicina":2},
         {"cijena":7,"naziv":"Upaljac","kolicina":1}]

print(check(lista))