
# atelier 1 exercice 1

# fonction somme factoriel 
def factorial(nb):
    if nb == 1: return nb
    return nb * factorial(nb - 1)

# fonction main 
def determinate(n):
     
    resultat = 0
    for i in range(1, n + 1):
        resultat = (factorial(i)/i) + resultat
    # Final result 
    return resultat

# affichage de la resultat final
print(determinate(int(input("entrez le nombre de terme \n"))))
