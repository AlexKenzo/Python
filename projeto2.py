import os
os.system('cls')

while True:
    print('Conversor de Decimal para Binario, Hexadecimal e Octadecimal.')
    print('Opção 0 - Sair')
    print('Opção 1 - Decimal para Binario')
    print('Opção 2 - Decimal para Hexadecimal')
    print('Opção 3 - Decimal para Octadecimal')
    print('Opção 4 - Dados do Projeto')
    print() 

    opcao=int(input('Digite a opção(0, 1, 2, 3, 4): '))
    if opcao in [1,2,3,4,0]:
        if opcao==0:
            print('Ok, Saindo...')
            break

        elif opcao==1:
            decimal=int(input('Digite um numero decimal: '))
            binario = ""
            while decimal > 0:
                binario = str(decimal % 2) + binario
                decimal = decimal // 2
            print("O número binário correspondente é: {}".format(binario))

        elif opcao==2:
            decimal=int(input('Digite aqui o numero decimal: '))
            hexadecimal = ""
            while decimal > 0:
                resto = decimal % 16
                if resto < 10:
                    hexadecimal = str(resto) + hexadecimal
                else:
                    hexadecimal = chr(resto - 10 + ord('a')) + hexadecimal
                    decimal = decimal // 16
            print("O número hexadecimal correspondente é: {}".format(hexadecimal))

        elif opcao==3:
            decimal=int(input('Digite aqui o numero decimal: '))
            octadecimal = ""
            while decimal > 0:
                octadecimal = str(decimal % 8) + octadecimal
                decimal = decimal // 8
            print("O número octal correspondente é: {}".format(octadecimal)) 

        elif opcao==4:
            print('Curso Análise e Desenvolvimento de Sistemas, Noturno, 1° Semestre')
            print('Componentes do Grupo:\nAlex Kenzo - RGM 32521618\nGuilherme Guabiraba Pironti - RGM 32525133')
            print('Disciplinas Envolvidas: Estruturas de Repetição, Entrada e Saída, Decisão Aninhada')
            print('Versão do Aplicativo: Python 3.11')
            print()

    else:
        print('Tipo de Entrada Invalida, tente novamente')
        print()