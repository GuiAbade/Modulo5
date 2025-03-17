vagas = [
    ['Vaga 1', 1200],
    ['Vaga 2', 2550],
    ['Vaga 3', 5000]
]


def salario(vaga):
    if vaga[1] > 2500:
        return True
    else:
        return False


print(list(filter(salario, vagas)))
print(list(map(salario, vagas)))
