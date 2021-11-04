# atelier 1 exercice 8

# Function  determine la  fréquence d’un caractère dans une chaîne

def avoir_occurence(struct, i):
    count = 0
    for n in struct:
        if n == i:
            count = count + 1
    return count

# avoir le Resultat

# exemple de numero 6 qui se repete deux fois

print(avoir_occurence([1, 6, 6, 1, 1], 6))