from Calculadora import soma
from Calculadora import sub

#Implementação da Calculadora simples

while True:
    #Apresentação
    print('\n\t\t\t --- Calculadora Simples -- \n')

    #Menu
    print('1.Soma')
    print('2.Subtração')
    print('3.Sair')

    #Ler a opção de escolha do usuário
    op = int(input('\n Opção:'))
    if op == 1 :
        print('\nSoma\n')
        #Entrada
        v1= int(input('Informe o valor1:'))
        v2= int(input('Informe o valor2:'))

        #Processamento
        total=soma(v1,v2)

        #Saída
        print(f'\n n{v1} + n {v2} = {total} \n')

    elif op == 2 :
        print('\n Subtração\n')

        #Entrada
        b1=int(input('digite um numero b1:'))
        b2=int(input('digite segundo numero b2:'))

        #Processamento
        total1=sub(b1,b2)

        #Saída
        print('\n n{b1} - {b2} = {total1} \n')

    elif op == 3 :
        #Sair do sistema
        print('Forte Abraço')
        break

    else:
        #Tratamento de exceção
        print(f'\n Opção {op} incorreta\n')
