'''nomes = ['Larissa', 'Rafael', 'Marcus', 'Jhon']


def pessoa_aprovada(pessoa):
    if pessoa == 'Marcus':
        return True
    else:
        return False


# Imprime apenas o nome informado na função
print(list(filter(pessoa_aprovada, nomes)))
# Mostra se a condição aplicada na função é verdadeira ou falsa
print(list(map(pessoa_aprovada, nomes)))
'''

pinturas = [
    ['Pintura Classica', 'Azul',    1857],
    ['Pintura Medieval', 'Verelha', 1867],
    ['Pintura Moderna',  'Verde',   1897],
]


def eh_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False


print(list(filter(eh_antiguidade, pinturas)))
print(list(map(eh_antiguidade, pinturas)))
