# Ordenar por propriedade
from operator import itemgetter
produtos = [
    ('Celular',   750),
    ('Bicicleta', 1500),
    ('Microfone', 550)
]
# Reverse=True para inverter a ordem finalizando no indice 0
produtos.sort(key=itemgetter(0), reverse=True)
print(produtos)

# Ordenando Matriz
matriz = [[5, 10], [15, 21], [1, 5]]
matriz.sort(key=itemgetter(1))
print(matriz)
