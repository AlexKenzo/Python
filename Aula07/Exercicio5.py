alunas = 0
alunos = 0
alturaM = 0
alturaF = 0

while True:
    sexo = str.lower(input('Digite o sexo(M/F) ou digite "S" para sair: '))
    if sexo == 's':
        break
    else:
        if sexo =='m':
            altura = float(input('Digite a altura: '))
            alturaM+=altura
            alunos+=1
        if sexo =='f':
            altura = float(input('Digite a altura: '))
            alturaF+=altura
            alunas+=1

if alunas > 0:
    mediaF = alturaF/alunas
    print('A media de altura de {} alunas é {}'.format(alunas,mediaF))
else:
    print('Não foram digitadas informações de alunas')
if alunos > 0:
    mediaM = alturaM/alunos
    print('A media de altura de {} alunos é de {}'.format(alunos,mediaM))
else:
    print('Não foram digitadas informações de alunos')