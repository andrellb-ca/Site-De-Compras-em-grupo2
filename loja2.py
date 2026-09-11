import time
produtos = []
while True:

    print('-' * 50)
    print('                Bem-vindo a loja')
    print('-' * 50)
    print('1 - Carne')
    print('2 - Açucar')
    print('3 - Chocolate')
    print('4 - Fone De Ouvido')
    print('5 - PlayStation 5')
    print('6 - Sair')
    print('7 - Adicionar um produto')


    for i, produto in enumerate(produtos, start=8):
        print(f'{i} - {produto[0]}')

    a = int(input('Qual produto você deseja comprar? '))

    if a == 1:
        d = input('Você tem dinheiro para comprar carne? Custa 50 reais: ').lower()
        if d in ['sim', 's', 'ss']:
            print('Beleza, você comprou Carne')
        elif d in ['não', 'nao', 'n', 'nn']:
            print('Ok, vá embora')
        else:
            print('Resposta inválida')

    elif a == 2:
        d = input('Você tem dinheiro para comprar açúcar? Custa 10 reais: ').lower()
        if d in ['sim', 's', 'ss']:
            print('Beleza, você comprou Açúcar')
        elif d in ['não', 'nao', 'n', 'nn']:
            print('Ok, vá embora')
        else:
            print('Resposta inválida')

    elif a == 3:
        d = input('Você tem dinheiro para comprar chocolate? Custa 5 reais: ').lower()
        if d in ['sim', 's', 'ss']:
            print('Beleza, você comprou Chocolate')
        elif d in ['não', 'nao', 'n', 'nn']:
            print('Ok, vá embora')
        else:
            print('Resposta inválida')

    elif a == 4:
        d = input('Você tem dinheiro para comprar o fone de ouvido? Custa 80 reais: ').lower()
        if d in ['sim', 's', 'ss']:
            print('Beleza, você comprou o Fone de Ouvido')
        elif d in ['não', 'nao', 'n', 'nn']:
            print('Ok, vá embora')
        else:
            print('Resposta inválida')

    elif a == 6:
        print('Saindo da loja...')
        break

    elif a == 7:
        p = str(input('Qual Produto deseja adiconar?'))
        print(f'{p} foi adicionado aos produtos')
        p2 = float(input('Qual o preço desse produto?'))
        print(f'o produto {p} foi adiconado com o valor de {p2} Reais ')
        produtos.append((p, p2))
    elif a >= 8 and a < 8 + len(produtos):
        produto = produtos[a - 8]
        d = input(f'Você tem dinheiro para comprar {produto[0]}? Custa {produto[1]} reais: ').lower()
        if d in ['sim', 's', 'ss']:
            print(f'Beleza, você comprou {produto[0]}')
        elif d in ['não', 'nao', 'n', 'nn']:
            print('Ok, vá embora')
    else:
        print('Produto inválido')
 