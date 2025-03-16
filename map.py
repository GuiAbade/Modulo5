# Como podemos criar listas?
# Criar listas usando Loops e Range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Função Map
nomes = ['Larissa', 'Rafael', 'Marcus', 'Jhon']


def aprovar_pessoa(nome):
    return nome + ' APROVADO'


print(list(map(aprovar_pessoa, nomes)))
