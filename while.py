r = 'S' 

while r == 'S':
    n1 = int(input('informe um valor: '))
    n2 = int(input('Informe outro valor: '))
    soma = n1 + n2
    r = str(input('Deseja continuar [S/N]')).upper()
print('A soma de todos os numeros é: {}'.format(soma))