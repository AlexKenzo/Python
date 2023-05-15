from random import*
num = randint(1,10)
parar = 0
tentativa = 0

while parar==0:
    tentativa = tentativa+1
    opcao = int(input('Digite um numero: '))
    if opcao == num:
        print('Voce acertou em {} tentativas'.format(tentativa))
        parar = 1
    elif opcao > num:
        print('Opção maior')
    else:
        print('Opção menor')