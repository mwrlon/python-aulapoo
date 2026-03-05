import time
import random
lista_produtos = []
lista_CPF = []
exibir_relatorio = 'relatorio'
sair_sistema = 'sair'
total_preco = ''
total_quantidade = ''
quantidade_produto = ''
categoria_produto = ''
desconto_produto = ''
nome_produto = ''
preco_produto = ''
desconto_limpeza = 'limpeza'
num = 0
voltar = 0
soma = ''
produto_mais_caro = ''
produto_mais_barato = ''
ticket_medio = 0


print('BEM VINDO AO SISTEMA SUPERMERCADO INTELIGENTE')
print('-' * 50)
print('Selecione o setor que deseja utilizar...')
print('(1) Criação de relatórios\n(2) Verificação de descontos\n(3) Mostrar produto mais caro, mais barato e ticket médio\n(4) Reposição de estoque \n(5) Sistema de ingressos\n(6)\n(7) Monitoramento de temperatura \n(8) Cadastro de usuário\n(9) Método de pagamento')
while num == voltar:
    num = int(input(''))


# /////////////////////// MOSTRAR RELATÓRIOS //////////////////////////////

while num == 1:
    print('---- MOSTRAR RELATÓRIOS ----')
    nome_produto = input('Digite o nome do produto: (ou "relatorio"/"sair"): ').lower()
    total_quantidade += quantidade_produto
    total_preco += preco_produto

    if nome_produto == exibir_relatorio:
        print('--Parciais do sistema--')
        print(f'Quantidade de produtos no total: {total_quantidade}')
        print(f'O total de preço dos produtos é {total_preco}')
        continue
        
    if nome_produto == sair_sistema:
        print('Saindo do sistema...')
        num = 0

    while True:
        preco = float(input(f'Digite o preço de {nome_produto}: '))
        if preco > 0:
            break
        print('O preço que você inseriu está errado. Por favor, digite novamente.')

    while True:
        quantidade_produto = int(input(f'Digite a quantidade de {nome_produto}: '))
        if quantidade_produto > 0:
            break
        print('A quantidade de produto que você inseriu está incorreta. Por favor, digite novamente.')

# //////////////////// VERIFICAÇÃO DE DESCONTOS //////////////////////////


while num == 2:
    print('---- VERIFICAÇÃO DE DESCONTOS ----')

    categoria_produto = input('Digite a categoria que seu produto pertence: ').lower()
    quantidade_produto = int(input('Digite a quantidade que você deseja comprar deste produto: '))
    time.sleep(1)
    print('Você deseja sair do sistema?')
    time.sleep(1)
    print('Digite 0 para sair')
    print('Digite 1 para continuar')
    num = int(input())


    if quantidade_produto >= 10:
        desconto_produto = 0.12
        print('Você conseguiu um desconto de 12%. Aproveite!')

    elif categoria_produto == desconto_produto:
        desconto_produto = 0.05
        print('Você conseguiu um desconto de 5%. Aproveite!')
    else:
        desconto_produto = 0
        print('Você não possui descontos ativos!')

# /////////////////////// MOSTRAR PRODUTO MAIS CARO & MAIS BARATO ////////////////////////////////


while num == 3:
    print('---- MOSTRAR PRODUTO MAIS CARO, MAIS BARATO E TICKET MÉDIO ----')

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

# /////////////////////// REPOSIÇÃO DE ESTOQUE ////////////////////////////////

while num == 4:
    print('---- REPOSIÇÃO DE ESTOQUE ----')
    limite = 10
    for i in range (0, limite):
        limite = int(input("Digite quanto voce quer: "))
        if limite == limite:
            print("Limite Atingido")
            break


# /////////////////////// SISTEMA DE INGRESSOS ////////////////////////////////

while num == 5:
    print('---- SISTEMA DE INGRESSOS ----')
    marcasparceiras = ["baly", "barrila", "heinz"]

    itens = []
    while True: 
        produtomarca = input("Digite a marca do seu produto: ")

        if produtomarca == "0":
            break

        quantidadeproduto = int(input("Digite a quantidade desse produto: "))

        produtos = {
        "marca": produtomarca ,
        "quantidade": quantidadeproduto
        }
        itens.append(produtos)

    contador = 0

    for produto in itens:
        if produto["marca"] in marcasparceiras:
            contador += produto["quantidade"]

    if contador > 5:
        print("Parabens, voce conseguiu um ingresso para um jogo de um de nossos times parceiros!!")
    


# /////////////////////// MONITORAMENTO DE TEMPERATURA //////////////////////////////

while num == 7:
    print('---- MONITORAMENTO DE TEMPERATURA ----')
    temperatura = random.randint(-10,10)
    print (f'Temperatura atual:{temperatura} C­°')

    if temperatura > 5:
        print (f'Temperatura acima do recomendado!{temperatura} C­°')
    time.sleep(1)


# /////////////////////// CADASTRO DE USUÁRIO //////////////////////////////

while num == 8:
    print('---- CADASTRO DE USUÁRIO ----')
    novo_CPF = input('Digite seu CPF:')
    if novo_CPF in lista_CPF:
        print(f'CPF ja cadastrado, tente novamente')
    elif len(novo_CPF) == 11 and novo_CPF.isdigit() :
        lista_CPF.append(novo_CPF)
        print(f'{lista_CPF}')
    else :
        print (f'CPF inválido, tente novamente: ')


# /////////////////////// MÉTODO DE PAGAMENTO //////////////////////////////

while num == 9:
    print('---- MÉTODO DE PAGAMENTO ----')
    valor = float(input('valor da compra:'))
    forma = input('Qual a forma do pagamento (debito/dinheiro):' ).lower()

    if forma == 'debito':
        total = valor * 1.05
        print (f'Total de um acréscimo de 5%: R${total:.2f}')

    elif forma == 'dinheiro':
        total = valor * 0.92
        print (f'Total de desconto é de 8%: R${total:.2f}')

    else:
        print(f'Pagamento inválido, tente novamente:')
