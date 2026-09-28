#Sistema de controle de estoque de eletrônicos

usuario = input('Digite seu nome: ').upper()
print( '=' * 40)
print('      SISTEMA DE ESTOQUE  DE ELETRÔNICOS      ')
print(f'      SEJA BEM VINDO, {usuario}')
print('=' * 40)

estoque_loja = []
controle_codigo = 1001

def cadastrar_produto(nome, preco, quantidade):
    global controle_codigo
    produto = {
        'codigo':controle_codigo,
        'nome':nome,
        'preco':preco,
        'quantidade':quantidade
    }
    estoque_loja.append(produto)
    controle_codigo += 1

def listar_produtos():
    if not estoque_loja:
        print('\nO Estoque está totalmente vazio! ')
        return
    print('\n=============================================')
    print('          PRODUTOS EM DESTAQUE          ')
    print('=================================================')
    for produto in estoque_loja:
        print(f'Código: {produto["codigo"]}')
        print(f'Nome: {produto["nome"]}')
        print(f'Preço: {produto["preco"]:.2f}')
        print(f'Quantidade: {produto["quantidade"]} unidades.')
        print('==========================================')


def vender_produto(codigo_busca, qtd_venda):
    for produto in estoque_loja:
        if produto['codigo']  == codigo_busca:
            if produto['quantidade'] >= qtd_venda:
                produto['quantidade'] -= qtd_venda
                print(f'Venda realizada com sucesso! Foram vendidas {qtd_venda} unidade de {produto['nome']}')
                return
            else:
                print(f'\n ERRO! Estoque insuficiente. Temos apenas {produto["quantidade"]} unidade de {produto["nome"]}')
                return
    print('Produto não localizado. Tente novamente.')

while True:
    print('=' * 40)
    print('          MENU DE OPÇÕES         ')
    print('=' * 40)
    print('1 - Cadastrar produto   ')
    print('2 - Listar estoque   ')
    print('3 - Realizar venda   ')
    print('4 Sair   ')
    print('=' * 40)

    opcao = input ('Escolha uma opção de 1 a 4 ')
    if opcao == '1':
        nomeproduto = input('Digite o nome do produto: ')
        precoproduto = float(input('Digite aqui o preço do produto:  '))
        qtdproduto = int(input('Digite a quantidade em estoque: '))
        cadastrar_produto(nomeproduto, precoproduto, qtdproduto)

    elif opcao == '2':
        listar_produtos()

    elif opcao == '3':
        codigo = int(input(' Digite o código identificador do produto desejado: '))
        qtd = int(input('Digite a quantidade a ser vendida:'))
        vender_produto(codigo, qtd)
    elif opcao == '4':
        print(f' \n Obrigado por usar o sistema, {usuario}. Programa encerrado!')
        break
    else:
        print('Opção inválida. Tente novamente.')



