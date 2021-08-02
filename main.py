from utils import soma, subtracao, multiplicacao, divisao

opcao = 100
while opcao != 0:
    print('########### MENU ###########')
    print('1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n0- Finalizar programa')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print('\n')
        print('----- SOMA -----')
        numero1 = float(input('Digite o número 1: '))
        numero2 = float(input('Digite o número 2: '))
        resultado = soma(numero1, numero2)
        print('Resultado: ', resultado)
        print('---------------------')
    if opcao == 2:
        print('\n')
        print('----- SUBTRAÇÃO -----')
        numero1 = float(input('Digite o número 1: '))
        numero2 = float(input('Digite o número 2: '))
        resultado = subtracao(numero1, numero2)
        print('Resultado: ', resultado)
        print('---------------------')
    if opcao == 3:
        print('\n')
        print('----- MULTIPLICAÇÃO -----')
        numero1 = float(input('Digite o número 1: '))
        numero2 = float(input('Digite o número 2: '))
        resultado = multiplicacao(numero1, numero2)
        print('Resultado: ', resultado)
        print('---------------------')
    if opcao == 4:
        print('\n')
        print('----- DIVISÃO -----')
        numero1 = float(input('Digite o número 1: '))
        numero2 = float(input('Digite o número 2: '))
        resultado = divisao(numero1, numero2)
        print('Resultado: ', resultado)
        print('---------------------')
