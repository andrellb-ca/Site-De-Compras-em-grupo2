import time

produtos = []
carrinho = []

catalogo = [
    ('Tênis', 130),
    ('Microfone', 100),
    ('Mouse', 50),
    ('Fone De Ouvido', 80),
    ('PlayStation 5', 4299)
]

while True:
    print('-' * 50)
    print('                Bem-vindo a loja')
    print('-' * 50)

    for i, produto in enumerate(catalogo, start=1):
        print(f'{i} - {produto[0]} - R$ {produto[1]:.2f}')

    print('6 - Sair')
    print('7 - Adicionar um produto')
    print('8 - Ver carrinho')
    print('9 - Finalizar compra')
    print('10 - Remover item do carrinho')

    for i, produto in enumerate(produtos, start=10):
        print(f'{i} - {produto[0]} - R$ {produto[1]:.2f}')

    try:
        a = int(input('Qual produto ou opção você deseja escolher? '))
    except ValueError:
        print('Digite apenas números.')
        continue

    if a in [1, 2, 3, 4]:
        produto = catalogo[a - 1]
        carrinho.append(produto)
        print(f'{produto[0]} foi adicionado ao carrinho!')

    elif a == 5:
        print('Você não vai comprar um PS5 em 2026.')
        print('O PS5 não pode ser adicionado ao carrinho.')

    elif a == 6:
        print('Saindo da loja...')
        break

    elif a == 7:
        p = input('Qual produto deseja adicionar? ')

        try:
            p2 = float(input('Qual o preço desse produto? '))
        except ValueError:
            print('Preço inválido.')
            continue

        produtos.append((p, p2))
        print(f'O produto {p} foi adicionado com o valor de R$ {p2:.2f}!')

    elif a == 8:
        print('\n' + '-' * 50)
        print('                 SEU CARRINHO')
        print('-' * 50)

        if not carrinho:
            print('Seu carrinho está vazio.')
        else:
            total = 0

            for i, produto in enumerate(carrinho, start=1):
                print(f'{i} - {produto[0]} - R$ {produto[1]:.2f}')
                total += produto[1]

            print('-' * 50)
            print(f'TOTAL: R$ {total:.2f}')

        input('Pressione Enter para voltar à loja...')

    elif a == 9:
        print('\n' + '-' * 50)
        print('              FINALIZAR COMPRA')
        print('-' * 50)

        if not carrinho:
            print('Seu carrinho está vazio.')
        else:
            total = sum(produto[1] for produto in carrinho)

            for produto in carrinho:
                print(f'{produto[0]} - R$ {produto[1]:.2f}')

            print('-' * 50)
            print(f'TOTAL DA COMPRA: R$ {total:.2f}')

            confirmar = input('Deseja finalizar a compra? ').lower()

            if confirmar in ['sim', 's', 'ss']:
                pagamento = input(
                    'Deseja pagar à vista ou parcelado? '
                    '(1 - À vista / 2 - Parcelado): '
                )

                if pagamento == '1':
                    print(f'Você pagou R$ {total:.2f} à vista!')

                elif pagamento == '2':
                    try:
                        parcelas = int(input('Em quantas vezes deseja pagar? (2 até 10): '))
                    except ValueError:
                        print('Número de parcelas inválido.')
                        input('Pressione Enter para voltar à loja...')
                        continue

                    if 2 <= parcelas <= 10:
                        valor_parcela = total / parcelas
                        print(f'Você pagará {parcelas}x de R$ {valor_parcela:.2f}')
                    else:
                        print('Você só pode parcelar de 2x até 10x.')
                        input('Pressione Enter para voltar à loja...')
                        continue

                else:
                    print('Forma de pagamento inválida.')
                    input('Pressione Enter para voltar à loja...')
                    continue

                print('Compra finalizada com sucesso!')
                carrinho.clear()
            else:
                print('Compra cancelada.')

        input('Pressione Enter para voltar à loja...')

    elif a >= 10 and a < 10 + len(produtos):
        produto = produtos[a - 10]
        carrinho.append(produto)
        print(f'{produto[0]} foi adicionado ao carrinho!')


    elif a == 10:
        print('\n' + '-' * 50)
        print('             REMOVER DO CARRINHO')
        print('-' * 50)

        if not carrinho:
            print('Seu carrinho está vazio.')
        else:
            for i, produto in enumerate(carrinho, start=1):
                print(f'{i} - {produto[0]} - R$ {produto[1]:.2f}')

            try:
                remover = int(input('Digite o número do item que deseja remover: '))

                if 1 <= remover <= len(carrinho):
                    produto_removido = carrinho.pop(remover - 1)
                    print(f'{produto_removido[0]} foi removido do carrinho!')
                else:
                    print('Número de item inválido.')

            except ValueError:
                print('Digite apenas números.')

        input('Pressione Enter para voltar à loja...')

    else:
        print('Produto inválido.')
