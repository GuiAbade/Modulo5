"""
COMO CRIAR E MODIFICAR ARQUIVOS:
'r'  -> Usado somete para ler algo
'w'  -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a'  -> Usado para acescentar algo
"""

import os

with open('celulares.txt', 'w') as arquivo:
    arquivo.write('Celular 2')

nomes = ['Lucas', 'Carol', 'Jef', 'Douglas']
with open('nomes.txt', 'a', newline='') as arquivo:
    for nome in nomes:
        arquivo.write(nome + os.linesep)

numeros = range(6)
with open('numeros.txt', 'a', newline='') as arquivo:
    for numero in numeros:
        arquivo.write(str(numero) + os.linesep)


# Ler os arquivos
with open('nomes.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)


# Ler todos os nueros e acrescentar um ao final do arquivo
with open('numeros.txt', 'r+') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('9999')
