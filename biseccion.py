def biseccion(f, a, b, tol):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")
    
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Ejemplo de uso
def f(x):
    return x**3 - x - 2

raiz = biseccion(f, 1, 2, 0.01)
print(raiz)  # Aproximadamente 1.521
