def calcular_precio_final(precio_inicial):
    iva = 0.19
    precio_final = precio_inicial * (1 + iva)
    return precio_final

# Ejemplo de uso
print(calcular_precio_final(100))  # 119.0
