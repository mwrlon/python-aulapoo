maior_de_idade = 0
menor_de_idade = 0

for i in range (1,11):
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    if idade >= 18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1

print(f'Existem {maior_de_idade} pessoas maiores de idade e {menor_de_idade} pessoas menores de idade')