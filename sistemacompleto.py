import time      
import random    
lista_produtos = []  
lista_CPF = []        
itens = []            
exibir_relatorio = ['relatorio', 'relatório']
sair_sistema = 'sair'
total_preco = 0
total_quantidade = 0
quantidade_produto = 0
categoria_produto = ''
desconto_produto = 0
nome_produto = ''
preco_produto = 0
desconto_limpeza = 'limpeza'
num = 0
voltar = 0
soma = 0
produto_mais_caro = 0
produto_mais_barato = 0
ticket_medio = 0
estoque_itens = 0
soma_estoque = 0


# Mensagem inicial do sistema
print('BEM VINDO AO SISTEMA SUPERMERCADO INTELIGENTE\n' + '=' * 50 + '\nSelecione o sistema que deseja utilizar...')

# Loop para garantir que o usuário escolha apenas 1 ou 2
while True:
    num = int(input('(1) Sistema Administrativo\n(2) Sistema para Clientes\nEscolha uma opção: '))
    
    if num == 1 or num == 2:
        break
    else:
        print('Opção inválida. Por favor, escolha 1 ou 2.')


# ================= SISTEMA ADMINISTRATIVO =================
while num == 1:

    print('---- SISTEMA ADMINISTRATIVO ----')


    # ================= MONITORAMENTO DE TEMPERATURA =================
    print('---- MONITORAMENTO DE TEMPERATURA ----')

    # Gera uma temperatura aleatória entre -10 e 10 graus
    temperatura = random.randint(-10,10)

    print (f'Temperatura atual:{temperatura} C°')

    # Se passar de 5 graus mostra alerta
    if temperatura > 5:
        print (f'Temperatura acima do recomendado!{temperatura} C°')
    else:
        print (f'Temperatura dentro do recomendado!{temperatura} C°')

    # Pausa de 1 segundo
    time.sleep(1)


    # ================= REPOSIÇÃO DE ESTOQUE =================
    print('---- REPOSIÇÃO DE ESTOQUE ----')

    limite_estoque = 10

    # Loop que simula reposição de estoque
    while soma_estoque < limite_estoque:

        estoque_itens = int(input("Digite quantos itens você quer: "))

        soma_estoque += estoque_itens

        # condição simples que encerra o loop

        if soma_estoque >= limite_estoque:
            print("Limite Atingido")
            break
        else:
            print(f'Você tem {limite_estoque - soma_estoque} itens restantes para atingir o limite de estoque')


    # ================= PRODUTO MAIS CARO / MAIS BARATO =================
    print('---- MOSTRAR PRODUTO MAIS CARO, MAIS BARATO E TICKET MÉDIO ----')
    
    while nome_produto != '0':
        # usuário cadastra um produto
        nome_produto = input('Digite o nome do produto: ')
        preco_produto = int(input('Digite o valor deste produto: '))

        # adiciona o produto dentro da lista
        lista_produtos.append({
            "nome": nome_produto,
            "preço": preco_produto
        })

        # soma quantidade de produtos
        soma += 1

        # soma total de preços
        total_preco += preco_produto

        # pega o produto mais caro da lista
        produto_mais_caro = max(lista_produtos, key=lambda lista_produto: lista_produto["preço"])

        # pega o produto mais barato da lista
        produto_mais_barato = min(lista_produtos, key=lambda lista_produto: lista_produto["preço"])

        # calcula ticket médio
        ticket_medio = total_preco / soma
        

        # mostra resultados
        print(f'A lista de produtos é {lista_produtos}\nO produto mais barato é {produto_mais_barato}\nO produto mais caro é {produto_mais_caro}\nO ticket médio desta compra é de R${ticket_medio:.2f}')

    time.sleep(1.5)


    # ================= RELATÓRIOS =================
    print('---- MOSTRAR RELATÓRIOS ----')

    # usuário digita produto ou comando
    nome_produto = input('Digite o nome do produto: (ou "relatorio"/"sair"): ').lower()

    # soma valores totais
    total_quantidade += quantidade_produto
    total_preco += preco_produto


    # se digitar relatorio mostra dados do sistema
    if nome_produto in exibir_relatorio:

        print('--Parciais do sistema--')
        print(f'Quantidade de produtos no total: {total_quantidade}')
        print(f'O total de preço dos produtos é {total_preco}')
        continue
        

    # se digitar sair encerra sistema
    if nome_produto == sair_sistema:

        print('Saindo do sistema...')
        num = 0


    # validação de preço
    while True:

        preco_produto = float(input(f'Digite o preço de {nome_produto}: '))

        if preco_produto > 0:
            break

        print('O preço que você inseriu está errado. Por favor, digite novamente.')


    # validação de quantidade
    while True:

        quantidade_produto = float(input(f'Digite a quantidade de {nome_produto}: '))

        if quantidade_produto > 0:
            break 

        print('A quantidade de produto que você inseriu está incorreta. Por favor, digite novamente.')

    if num == 0:
        print('Saindo do sistema...')
        break

    elif num == 1:
        num = 1



# ================= SISTEMA DE CLIENTES =================
while num == 2:

    print('---- SISTEMA DE CLIENTES ----')


    # ================= VERIFICAÇÃO DE DESCONTOS =================
    print('---- VERIFICAÇÃO DE DESCONTOS ----')

    # usuário informa categoria e quantidade
    categoria_produto = input('Digite a categoria que seu produto pertence: ').lower()
    quantidade_produto = int(input('Digite a quantidade que você deseja comprar deste produto: '))


    # desconto por quantidade
    if quantidade_produto >= 10:

        desconto_produto = 0.12
        print('Você conseguiu um desconto de 12%. Aproveite!')

    # desconto para produtos de limpeza
    elif categoria_produto == desconto_limpeza:

        desconto_produto = 0.05
        print('Você conseguiu um desconto de 5%. Aproveite!')

    else:

        desconto_produto = 0
        print('Você não possui descontos ativos!')


    # ================= SISTEMA DE INGRESSOS =================
    print('---- SISTEMA DE INGRESSOS ----')

    # lista de marcas parceiras
    marcasparceiras = ["baly", "barrila", "heinz"]

    while True: 

        produtomarca = input("Digite a marca do seu produto: ")

        # digitar 0 encerra cadastro
        if produtomarca == "0":
            break

        quantidadeproduto = int(input("Digite a quantidade desse produto: "))

        # cria dicionário com dados do produto
        produtos = {
        "marca": produtomarca ,
        "quantidade": quantidadeproduto
        }

        # adiciona na lista
        itens.append(produtos)


    contador = 0

    # verifica se produtos são de marcas parceiras
    for produtos in itens:

        if produtos["marca"] in marcasparceiras:
            contador += produtos["quantidade"]


    # se comprar mais de 5 ganha ingresso
    if contador > 5:

        print("Parabens, voce conseguiu um ingresso para um jogo de um de nossos times parceiros!!")


    # ================= CADASTRO DE USUÁRIO =================
    print('---- CADASTRO DE USUÁRIO ----')

    novo_CPF = input('Digite seu CPF:')

    # verifica se CPF já existe
    if novo_CPF in lista_CPF:

        print(f'CPF ja cadastrado, tente novamente')

    # valida CPF simples (11 números)
    elif len(novo_CPF) == 11 and novo_CPF.isdigit() :

        lista_CPF.append(novo_CPF)
        print(f'{lista_CPF}')

    else :

        print (f'CPF inválido, tente novamente: ')


    # ================= MÉTODO DE PAGAMENTO =================
    print('---- MÉTODO DE PAGAMENTO ----')

    valor = float(input('valor da compra:'))

    forma = input('Qual a forma do pagamento (debito/dinheiro/pix):' ).lower()


    # débito tem acréscimo de 5%
    if forma == 'debito':

        total = (valor * 1.05) 
        print (f'Total de um acréscimo de 5%: R${total:.2f}')

    # dinheiro tem desconto
    elif forma == 'dinheiro':

        total = (valor * 0.92) 
        print (f'Total de desconto é de 8%: R${total:.2f}')

    # pix sem alteração
    elif forma == 'pix':

        print(f'Pagamento via pix, sem acréscimo ou desconto: R${valor:.2f}')


    time.sleep(1.5)


    # pergunta se deseja sair
    print('Você deseja sair do sistema?')

    time.sleep(1)

    print('Digite 0 para sair')
    print('Digite 1 para continuar')

    num = int(input())

    if num == 0:

        print('Saindo do sistema...')
        break
    elif num == 1:
        num = 2