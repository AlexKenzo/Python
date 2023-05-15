email = str(input('Digite o seu email: '))
dominio = email.split('@')[1]
print(f'O dominio do seu e-mail é: http://{dominio}')