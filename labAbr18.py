def divisores_tres(n):
    """1) Función que retorna los divisores de tres entre 1 y n.

    :param n: int.
    :returns: int.
    :rtype: int.

    """
    for i in range(1, n+1):
        if i % 3 == 0:
            yield i


def Cond_filter(n, cond=lambda x: x % 3 == 0):
    """2) Similar a filter, la "misma" función de 1) con un parámetro cond. La función, digamos f1 sera llamada como f(n,cond) y genera los números de 1 a n que cumplen cond.

    :param n: int.
    :param cond: condición.
    :returns: números de 1 a n que cumplen condición.
    :rtype: int.

    """
    for i in range(1, n+1):
        if cond(i):
            yield i


def Parentesis(n):
    """3) Función que genera dado un n, todas las formas correctas de escribir n parejas de paréntesis. Ej, n=3
    "()()()","()(())","(())()","(()())","((()))"

    :param n: int. 
    :returns: combinaciones válidas de paréntesis.
    :rtype: string.

    """
    if n == 0:
        yield ""
    else:
        for k in range(0, n):
            for s1 in Parentesis(k):
                for s2 in Parentesis(n-k-1):
                    yield "(" + s1 + ")" + s2


for value in Parentesis(5):
    print(value)