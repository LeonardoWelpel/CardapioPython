t1 = ('Doce', 2.3, 'Bala', 0.15, 'Pizza', 28.9, 'Arroz', 4.5, 'Paçoca', 0.5, 'Pamonha', 5.4)

print('-'*40)
print(f'{"Cardápio":^40}')
print('-'*40)
cardapio = {}
for i in range(0, len(t1), 2):
    cardapio[t1[i]] = t1[i+1]

for item, preco in cardapio.items():
    print("{:.<25} : R$ {:>7.2f}".format(item, preco))

print('-'*40)

soma = 0
ped = input('Deseja Selecionar suas comidas (s/n): ')
while ped == 's':
    comida = input('Digite a comida desejada: ')
    if comida in cardapio:
        soma += cardapio[comida]
        print('Valor adicionado: R$ {:.2f}'.format(cardapio[comida]))
    else:
        print('Item não encontrado no cardápio.')
    ped = input('Mais algum pedido? (s/n) ')
    if ped == "n":
        break
print('Fim do pedido')
print()
print('Valor total da conta: R$ {:.2f}'.format(soma))
print('-'*40)
