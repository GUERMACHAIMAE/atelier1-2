
# atelier 1 exercice 2

# Fonction convertir Nombre au Binaire 
def binary(nbr):
    
    result = ""
    if nbr >= 1:
       
        result = result + str(nbr % 2)
        return result + binary(nbr // 2)
    
    
    return result


def reverse(string):
    return string[::-1]

# Main fonction
def main(nbr):
    return (reverse(binary(nbr)))

# avoir le resultat 
print(main(int(input("enterez le nombre ici \n"))))