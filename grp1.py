# # 1- 
# exibir_relatorio = 'relatorio'
# sair_sistema = 'sair'
# total_preco = 0
# total_quantidade = 0
# quantidade = 0
# preco = 0

# while True:
#     nome_produto = input('Digite o nome do produto: (ou "relatorio"/"sair"): ').lower()
#     total_quantidade += quantidade
#     total_preco += preco

#     if nome_produto == exibir_relatorio:
#         print('--Parciais do sistema--')
#         print(f'Quantidade de produtos no total: {total_quantidade}')
#         print(f'O total de preço dos produtos é {total_preco}')
#         continue
        
#     if nome_produto == sair_sistema:
#         print('Saindo do sistema...')
#         break
#     while True:
#         preco = float(input(f'Digite o preço de {nome_produto}: '))
#         if preco > 0:
#             break
#        print('O preço que você inseriu está errado. Por favor, digite novamente.')

#     while True:
#         quantidade = int(input(f'Digite a quantidade de {nome_produto}: '))
#         if quantidade > 0:
#             break
#         print('A quantidade de produto que você inseriu está incorreta. Por favor, digite novamente.')

# # 2- 

# import time

# categoria_produto = 0
# desconto_produto = 0
# num = -1


# while num != 0:
#     print('')
#     categoria_produto = input('Digite a categoria que seu produto pertence: ').lower()
#     quantidade_produto = int(input('Digite a quantidade que você deseja comprar deste produto: '))
#     time.sleep(1)
#     print('Você deseja sair do sistema?')
#     time.sleep(1)
#     print('Digite 0 para sair')
#     print('Digite 1 para continuar')
#     num = int(input())

#     if quantidade_produto >= 10:
#         desconto_produto = 0.12
#         print('Você conseguiu um desconto de 12%. Aproveite!')
#         break
#     elif categoria_produto == 'limpeza':
#         desconto_produto = 0.05
#         print('Você conseguiu um desconto de 5%. Aproveite!')
#         break
#     else:
#         desconto_produto = 0
#         print('Você não possui descontos ativos!')


# 3-

import time
nome_produto = ''
preco_produto = 0
num = 1
lista_produtos = []
soma = 0
total_preco = 0

while num != 0:

    nome_produto = input('Digite o nome do produto: ')
    preco_produto = int(input('Digite o valor deste produto: '))
    lista_produtos.append({
        "nome": nome_produto,
        "preço": preco_produto
    })
    soma += 1
    total_preco += preco_produto

    print('Você deseja sair do sistema?')
    print('Digite 0 para sair')
    print('Digite 1 para continuar')
    num = int(input())

    produto_mais_caro = max(lista_produtos, key=lambda lista_produto: lista_produto["preço"])
    produto_mais_barato = min(lista_produtos, key=lambda lista_produto: lista_produto["preço"])
    ticket_medio = total_preco / soma
    

print(f'A lista de produtos é {lista_produtos}')
print(f'O produto mais barato é {produto_mais_barato}')
print(f'O produto mais caro é {produto_mais_caro}')
print(f'O ticket médio desta compra é de R${ticket_medio:.2f}')
