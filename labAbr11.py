#   Implementar en Python, sin usar funciones de Python:
#
#   1) min(A)   : Devuelve el mínimo de A.
#   2) min(A,f) : Devuelve el elemento de A que minimiza f.
#   3) Usando min(A,f) implemente max(A,f).
#   4) Implemente un algoritmo de ordenamiento: ordenar(A), que ordene a A.
#   5) ordenar(A,comp) donde comp es una función de comparación.
####


# 2 minimo(A, f)
def minimo(A, f=lambda x: x):
    m = None
    for e in A:
        if m is None or f(m) > f(e):
            m = e
    return m

# 1 minimo(A)
def minim(A):
    return minimo(A)

# 3 maximo usando min(A,f)
def maximo(A, f=lambda x : x):
    return minimo(A, lambda x: -f(x))

# 4 quicksort
def qsort(A):
    if A == []: return []
    return  qsort([x for x in A[1:] if x< A[0]]) + A[0:1] + \
            qsort([x for x in A[1:] if x>=A[0]])

# 5 sort usando función de comparación
def qsortf(A, comp):
    if A == []: return []
    return  qsortf([x for x in A[1:] if comp(x,A[0])],comp) + A[0:1] + \
            qsortf([x for x in A[1:] if not comp(x,A[0])],comp)