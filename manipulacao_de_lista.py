valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2050]
valores.append(11)  # Adicionar valores no fim da lista
print(valores)
# Unir listas
valores.extend(anos)
print(valores)
# Adicionar listas
nova_lista = valores + anos
print(nova_lista)
# Inserir novo valor em uma lista
print(anos[1])
anos.insert(2, 2031)
print(anos)
# Extrair com base no indice
anos_2020 = anos.pop(0)
print(anos_2020)
# Remover item da lista
anos.remove(2050)
print(anos)
# a função 'del' podemos remover uma faixa de indides
# ex: Remover do indice 2 até o 5 [1:7] -> del anos[1:7]

# Para contar a ocorrencia de um valor:
"print(valores.count(2))"

# Resetar itens de uma lista
valores.clear()
