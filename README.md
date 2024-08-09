# Algoritmos y su Implementación en Python

### Algoritmo para decidir si un número natural $(n)$ es un número primo

- Pseudocódigo
```
Algoritmo EsPrimo(n)
    Si n <= 1 Entonces
        Retornar Falso
    FinSi
    Para i desde 2 hasta √n Hacer
        Si n % i == 0 Entonces
            Retornar Falso
        FinSi
    FinPara
    Retornar Verdadero
FinAlgoritmo
```

```python
import math

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Ejemplo de uso
print(es_primo(17))  # True
print(es_primo(18))  # False
```




