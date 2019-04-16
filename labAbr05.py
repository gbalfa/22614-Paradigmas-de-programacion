def factorial (n):
    return 1 if n <= 0 else n*factorial(n-1)

def potencia (n,m):
    return 1 if m <= 0 else n*potencia(n,m-1)

def qsort(L):
    if L == []: return []
    return  qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + \
            qsort([x for x in L[1:] if x>=L[0]])

def fibonacci(n):
    E=[]
    for i in range(n):
        if i < 8:
            E+=[N_Fib(i+1)]
        else:
            E+=[E[len(E)-2]+E[-1]]
    return E

def N_Fib(n):
    if n <= 1: return 0
    if n == 2: return 1
    if n > 2:
        return N_Fib(n-1)+N_Fib(n-2)

def maximo(L):
    m = None
    for e in L:
         if m is None or m < e:
             m = e
    return m

def minimo(L):
    m = None
    for e in L:
         if m is None or m > e:
             m = e
    return m

def impares(L):
    for e in L:
        if not e%2:
            L.remove(e)
    return L

def pares(L):
    for e in L:
        if e%2:
            L.remove(e)
    return L