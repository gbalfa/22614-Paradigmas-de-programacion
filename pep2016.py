def common(A, B):
    """Pregunta 1.
    Programe eficientemente en Python la función common(A,B) que recibe dos
    listas A y B, cada una formada por números distintos ordenados de menor a mayor, y nos devuelve
    una lista ordenada con los valores que se repiten en ambas listas. Por ejemplo, common([1, 2, 4,
    5, 6, 8], [2, 3, 4, 5, 7, 8]) => [2, 4, 5, 8].

    :param A: Lista formada por números distintos ordenados de menor a mayor.
    :param B: Lista formada por números distintos ordenados de menor a mayor.
    :returns: Lista ordenada con los valores que se repiten en ambas listas. 
    :rtype: Lista.

    """
    i, j = 0, 0
    largoA, largoB = len(A), len(B)
    lista = []
    while (i < largoA and j < largoB):
        if A[i] == B[j]:
            lista.append(A[i])
            i += 1
        elif A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i += 1
    return lista


def sublists(A, k):
    """Pregunta 2
    Usando las funciones map y filter, programe en Python bajo el paradigma
    funcional la función sublists(A,k) que recibe una lista y un entero positivo k, y devuelve en una
    nueva lista todas las sublistas de A formadas por k elementos consecutivos todos positivos.

    :param A: Lista.
    :param k: Entero positivo.
    :returns: Nueva lista con todas las sublistas de A formadas por k elementos consecutivos todos positivos. 
    :rtype: Lista.

    """
    listaPositivos = list(filter(lambda x: x > 0, A))
    cantidadElementos = int(len(listaPositivos)/k)*k
    return list(map(lambda i: listaPositivos[i:i+k], range(0, cantidadElementos, k)))


A = [1, 2, 4, 5, 6, 8]
B = [-3, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14]

# 1)
print(common(A, B))

# 2)
print(sublists(B, 3))
