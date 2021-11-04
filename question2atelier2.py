# atelier 2 exercice 2

def divise_inverse(tab):
    i = 0
    export = []
    for i in range(0, 9, 3):
        export.append(tab[i:i + 3])
    return export


print(divise_inverse([9, 2, 7, 9, 5, 6, 7, 5, 9]))