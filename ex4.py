num = -1 
soma = 0
num_informados = -1

while num != 0:
    num = float(input('Digite um número. (0 para sair): '))
    soma += num
    num_informados += 1

print(f'Você informou {num_informados} numeros e a soma deles foi de {soma}')