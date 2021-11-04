
# atelier 1 exercice 4
def fib(n):

    
    if n <=1: 
       return n 
    else:
       return(fib(n - 1) + fib(n - 2))

 
n=(fib(int(input("saisir le nombre \n"))))
for i in range (n):
 print(fib(i))
