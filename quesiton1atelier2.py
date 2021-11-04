# atelier 2 exercice 1

def get_liste3(list11, list12):
    a, b = [], [] 
    for i in range(0, len(list11)):
        if i % 2 != 0: a.append(list11[i])
    
    for j in range(0, len(list12)):
        if j % 2 == 0:  b.append(list12[j])
    return a + b

print(get_liste3([1, 6, 8, 4, 7], [2, 5,  3]))