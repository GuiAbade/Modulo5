# Revisão
# 1
idade = input('Digite sua idade')
print(int(idade) > 17)
# 2
ano_publicacao = 2020
print('Este livro foi criado em' + str(ano_publicacao))
# 3
altura = input('Altura da parede?')
print(float(altura) > 2.50)

# Conversões entre coleções
saudacao = 'Hello!'
print(list(list(saudacao)))
print(list(set(saudacao)))
print(list(tuple(saudacao)))
print(list(range(30)))

numeros = [10, 20, 20, 50]
print(set(numeros))
print(tuple(numeros))
print(type(numeros))
