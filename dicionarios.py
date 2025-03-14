# Dicionários

'''
Pessoa
  nome
  idade
  altura
'''
# Dicionário
dicionario_pessoa = {'Nome': 'Gaby', 'idade': 18, 'altura': 1.60}
pessoa_2 = dict(nome='Gaby', idade=18, altura=1.60)
# print(pessoa_2['idade']) -> acessando através da chave
print(dicionario_pessoa.keys())    # Acessando as chaves do dicionário
print(dicionario_pessoa.values())  # Acessando os valores do dicionário
print(dicionario_pessoa.items())   # Acessando chaves e valores do dicionário

# Iterar sobre um dicionário:

for item in dicionario_pessoa.items():
    print(item)
    print(item[1])
