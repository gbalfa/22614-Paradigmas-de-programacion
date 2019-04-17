#   Implementar en Python, sin usar funciones de Python:
#
#   1) min(A)   : Devuelve el mínimo de A.
#   2) min(A,f) : Devuelve el elemento de A que minimiza f.
#   3) Usando min(A,f) implemente max(A,f).
#   4) Implemente un algoritmo de ordenamiento: ordenar(A), que ordene a A.
#   5) ordenar(A,comp) donde comp es una función de comparación.
####


def minimo(A, f=lambda x: x):
    """ 1) y 2): Funcion que retorna elemento de A que minimiza la función f.

    :param A: Lista floats.
    :param f: Función.
    :returns: elemento de A que minimiza la función.
    :rtype: float

    """
    m = None
    for e in A:
        if m is None or f(m) > f(e):
            m = e
    return m

def maximo(A, f=lambda x: x):
    """ 3): Máximo usando min(A,f). 
    Función que retorna elemento de A que maximiza la función f.

    :param A: Lista floats.
    :param f: Función.
    :returns: elemento de A que maximiza la función.
    :rtype: float
 
    """
    return minimo(A, lambda x: -f(x))


def qsort(A):
    """ 4) Función que ordena una lista usando Quicksort.

    :param A: Lista.
    :returns: Lista ordenada.
    :rtype: Lista.

    """
    if A == []:
        return []
    return qsort([x for x in A[1:] if x < A[0]]) + A[0:1] + \
        qsort([x for x in A[1:] if x >= A[0]])



def qsortf(A, comp):
    """ 5) Sort usando función de comparación.

    :param A: Lista.
    :param comp: Operación binaria de comparación.
    :returns: Lista ordenada según criterio comparación.
    :rtype: Lista.

    """
    if A == []:
        return []
    return qsortf([x for x in A[1:] if comp(x, A[0])], comp) + A[0:1] + \
        qsortf([x for x in A[1:] if not comp(x, A[0])], comp)
