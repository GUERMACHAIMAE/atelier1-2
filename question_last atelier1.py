# atelier 1 exercice 9

# fonction qui cherche un élément dans une matrice puis renvoi sa position
def get_position(matrice, element):
    for i in matrice:
        for j in i:
            if j == element:
                return [i, j]
    return None

print(get_position(list(input("saisir 2D array ici or array")), 1))