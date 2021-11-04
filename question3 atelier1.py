# atelier 3 exercice 4

# Fonction determine la somme des nombres 
def sum(n):
    
    if n >= 1:
         
        return n + sum( n - 1 )
    # Retruner le Resultat
    return n

# avoir le resultat
print(sum(int(input("saisir n \n"))))