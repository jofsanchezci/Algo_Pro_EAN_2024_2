def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Ejemplo de uso
print(mcd(54, 24))  # 6
