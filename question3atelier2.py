
# atelier 2 exercice 3
def occurence(list):
    c = {}
    for i in list:
        if str(i) in c:
            c[str(i)] = c.get(str(i)) + 1
        else:
            c[str(i)] = 1
    return c

print(occurence([1, 2, 3, 2, 5,]))