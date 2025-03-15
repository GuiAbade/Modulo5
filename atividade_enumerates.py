frutas = ['Maçã', 'Laranja', 'Morango', 'Limão']

for indice, fruta in enumerate(frutas, 0):
    print(indice, fruta)
    if indice == 3:
        print(f'{indice} {fruta} está em promoção')
