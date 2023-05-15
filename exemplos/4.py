aluno = 0 
while aluno <10:
    nota1=float(input('Digite a nota 1: '))
    nota2=float(input('Digite a nota 2: '))
    aluno = aluno + 1
    media = (nota1+nota2)/2
    print('A nota do aluno {} foi {}'.format(aluno,media))