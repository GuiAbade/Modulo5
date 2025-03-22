import os

frutas = ['Banana', 'Maçã', 'Morango', 'Pera', 'Goiaba']
linguagens = ['python', 'JS', 'Java', 'C#', 'C++']
cores = ['vermelho', 'amarelo', 'azul', 'rosa', 'roxo']

with open('frutas.txt', 'w', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

with open('frutas.txt', 'a', newline='') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + cor)

with open('top 5 linguagens.txt', 'w', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)

# Como criar varios arquivos vazios usando laço

arquivos = ['musica.mp3', 'foto.jpg', 'senhas.txt', 'relaroio.pdf']
for arquivo in arquivos:
    with open(arquivo, 'w') as criarArquivo:
        pass
