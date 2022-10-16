# Funkciji se predaju dva parametra. Provjera se jesu li parametri istog tipa,
# ako ne error. Provjeri se jesu li parametri liste ili dictionary, ako ne error.
# Vraća se spojena lista ili dictionary.
# Ispis : [1,2,1,2],[3,2] -> [1,2,1,2,3,2]
# Ispis : {1:2,3:2},{5:2,4:1} -> {1: 2, 3: 2, 5: 2, 4: 1}

def check(lista1,lista2):
    if type(lista1) == type(lista2):
        if isinstance(lista1, list) and isinstance(lista2, list):
            return lista1 + lista2
        elif isinstance(lista1, dict) and isinstance(lista2, dict):
            return lista1 | lista2
    return "error"



lista1 = [1,2,1,2]
lista2 = [3,2]

dict1 = {1:2,3:2}
dict2 = {5:2,4:1}

print(check(lista1,lista2))
print(check(dict1,dict2))