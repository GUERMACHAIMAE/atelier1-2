# atelier 1 exercice 6

# Function trier par insertion 

def trier_par_insertion(tab):
    i =  0
    while( i < len(tab) - 1):
        if tab[i] > tab[i + 1]:
            j = tab[i + 1]
            tab[i + 1] = tab[i]
            tab[i] = j
        i = i + 1
    return tab

# Function trier à Bull

def trier_a_bull(tab, a):
    if tab == []:
        return a
    num = min(tab)
    a.append(num)
    tab.remove(num)
    return trier_a_bull(tab, list(a))


# Function trier par Selection

def trier_par_selection(tab):
    n = len(tab)
    for i in range(0, n - 2):
        min = i
        for j in range(i + 1, n - 1):
            if tab[j] < tab[min]:
                min = j
        if min != i:
            temp = tab[min]
            tab[min] = tab[i]
            tab[i] = temp
    return tab


# affichage Finale
print(trier_par_selection([9, 5, 7, 2, 8]))
print(trier_par_selection([1, 5, 3, 2, 2]))
print(trier_a_bull([9, 5, 7, 2, 8], []))