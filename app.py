preco_1 = 10
preco_2 = 20
preco_3 = 30
# listas
precos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
precos[2]  # Imprime o idice 2 (numero 30)
print(precos[0])
print(precos[precos.index(100)])
# Listas no python são dinâmicas(aceitam qualquer tipo de dado)
itens = [1, 3, 6, 'Olá', 'Café', True, 10.6]
print(itens[4])
# Maneiras diferentes de gerar uma lista
# Multiplicação de valores (repetição)
lista_de_noves = [9] * 10
print(lista_de_noves)
# Usando gerador Range (Sequência)
# 1 até 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)
# Gerar a partir de strings
print(list('Bem-vindo ao treinamento'))
# criando lista de lista (matriz)
matriz_de_nomes = [['Carol', 30], ['Marcos', 50]]
print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0])
