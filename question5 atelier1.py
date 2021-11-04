# atelier 1 exercice 5

#  Fonction compte les chiffres d'un nombre
def chiffre_number(nbr):
    
    if len(nbr) > 1:
       
        return chiffre_number(nbr[0:len(nbr) - 1]) + 1
    return 1

# avoir le Resultat
print(chiffre_number(str(input("saisir le nombre ici "))))