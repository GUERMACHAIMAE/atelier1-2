# atelier 2 exercice 4

def intersection(set1, set2):
    a = set((""))
    for i in set1:
        for j in set2: 
            if i == j: a.add(i)
   
    b = set1.copy()
    for i in set1:
        if i in a: b.remove(i)

    print(" l'intersection => ", a, "le reste de set1", b)


