total = 0
venda = 0

for i in range(1,6):
    venda = float(input(f'Digite o valor de venda do {i}º dia: R$'))
    total += venda
    media = total / 5
    
print(f'O total vendido foi de R${total}')
print(f'A média de vendas por dia é R${media}')


