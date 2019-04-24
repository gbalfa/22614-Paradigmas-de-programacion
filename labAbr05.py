""" Argumentos en mayúsculas corresponden a listas.
"""


def factorial(n):
    """ Función que retorna el valor de n factorial.
    """
    return 1 if n <= 0 else n*factorial(n-1)


def potencia(n, m):
    """ Función que retorna el valor de n elevado a la m.
    """
    return 1 if m <= 0 else n*potencia(n, m-1)


def qsort(L):
    """Función que ordena una lista de menor a mayor usando el algoritmo Quick Sort.
    """
    if L == []:
        return []
    return qsort([x for x in L[1:] if x < L[0]]) + L[0:1] + \
        qsort([x for x in L[1:] if x >= L[0]])


def fibonacci(n):
    """Función que retorna una lista con los primeros n números de Fibonacci.
    """
    E = []
    for i in range(n):
        if i < 8:
            E += [N_Fib(i+1)]
        else:
            E += [E[len(E)-2]+E[-1]]
    return E


def N_Fib(n):
    """ Función que retorna el número n de la sucesión de Fibonacci.
    """
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return N_Fib(n-1)+N_Fib(n-2)


def maximo(L):
    """ Dada una lista retorna el elemento con el valor máximo.
    """
    max = None
    for elem in L:
        if max is None or max < elem:
            max = elem
    return max


def minimo(L):
    """ Dada una lista retorna el elemento con el valor mínimo.
    """
    min = None
    for elem in L:
        if min is None or min > elem:
            min = elem
    return min


def impares(L):
    """ Dada una lista de números, elimina los pares.
    """
    for elem in L:
        if not elem % 2:
            L.remove(elem)
    return L


def pares(L):
    """ Dada una lista de números, elimina los impares.
    """
    for elem in L:
        if elem % 2:
            L.remove(elem)
    return L
