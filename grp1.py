# 1- 
exibir_relatorio = 'relatorio'
sair_sistema = 'sair'
total_preco = 0
total_quantidade = 0
quantidade = 0
preco = 0

while True:
    nome_produto = input('Digite o nome do produto: (ou "relatorio"/"sair"): ').lower()
    total_quantidade += quantidade
    total_preco += preco

    if nome_produto == exibir_relatorio:
        print('--Parciais do sistema--')
        print(f'Quantidade de produtos no total: {total_quantidade}')
        print(f'O total de preço dos produtos é {total_preco}')
        continue
        
    if nome_produto == sair_sistema:
        print('Saindo do sistema...')
        break
    while True:
        preco = float(input(f'Digite o preço de {nome_produto}: '))
        if preco > 0:
            break
        print('O preço que você inseriu está errado. Por favor, digite novamente.')

    while True:
        quantidade = int(input(f'Digite a quantidade de {nome_produto}: '))
        if quantidade > 0:
            break
        print('A quantidade de produto que você inseriu está incorreta. Por favor, digite novamente.')

# 2- 


# 3-

