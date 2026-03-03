import time
senha_correta = '123123'
senha = 0

while senha != senha_correta:
    senha = input('Confirme a sua senha: ')
    if senha != senha_correta:
        print('A senha está incorreta, digite-a novamente.')
    else:
        print('A senha foi digitada corretamente')
        time.sleep(1)
        print('Estaremos liberando o acesso ao usuario em breve...')
        break