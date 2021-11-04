# atelier 2 exercice 5

def get(list1, dict1):
    keys = list(dict1.keys())
    result = []
    for i in keys:
        for j in list1:
            if dict1[str(i)] == j: 
                result.append(j)
    return result

print(get([47, 64, 69, 37, 76, 83, 95, 97], {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}))