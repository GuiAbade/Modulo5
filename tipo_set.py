# SET

numeros = [2, 2, 5, 8]
frutas = {'maça', 'uva', 'banana', 'maça', 'morango'}
# Convertendo para set
set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)
# Adicionando novos valores
set_numeros.add(10)
print(set_numeros)

# Conjuntos

numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]

a = set(numeros1)
b = set(numeros2)

# Imprimindo que não estão nas duas listas(exceto numeros repetidos)
print(a.symmetric_difference(b))
# Imprimindo valores presentes nas duas variáveis(exceto numeros repetidos)
print(a.intersection(b))
# Imprimindo os valores presentes em A e B(exceto numeros repetidos)
print(a.union(b))
