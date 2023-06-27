#Função - Cadastro do produto
def cadastrar(lista_produtos):
    nome = input("Digite o nome do produto: ")
    codigo = input("Digite o código do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))

    produto = {"nome": nome, "codigo": codigo, "quantidade": quantidade}
    lista_produtos.append(produto)
    print("Produto cadastrado com sucesso!") 
#Função - Consultar estoque
def fazer_consulta(lista_produtos):
    codigo = input("Digite o código do produto a ser consultado: ")

    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            print("Informações do produto:")
            print(f"Produto: {produto['nome']}")
            print(f"Código: {produto['codigo']}")
            print(f"Quantidade: {produto['quantidade']}")
            return
    print("Produto não foi encontrado.")

#Função - Atualizar o produto do estoque
def atualização(lista_produtos):
    codigo = input("Digite o código do produto a ser atualizado: ")

    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            opcao = input("Deseja atualizar o nome, quantidade ou ambos?(nome/quantidade/ambos): ")
            if opcao == "nome" or opcao == "ambos":
                novo_nome = input("Digite o novo nome do produto: ")
                produto["nome"] = novo_nome
            if opcao == "quantidade" or opcao == "ambos":
                nova_quantidade = int(input("Digite o novo estoque  do produto: "))
                produto["quantidade"] = nova_quantidade
            print("Produto atualizado!")
            return
    print("Produto não foi encontrado.")

#Função - retirar o produto do estoque
def exclusão_do_produto(lista_produtos):
    codigo = input("Digite o código do produto a ser excluído: ")

    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            lista_produtos.remove(produto)
            print("Produto excluído!")
            return

    print("Produto não foi encontrado.")

#Função - relatório do produto
def relatorio(lista_produtos):
    print("Relatório de Produtos:")
    for produto in lista_produtos:
        print(f"Produto: {produto['nome']}")
        print(f"Código: {produto['codigo']}")
        print(f"Quantidade: {produto['quantidade']}")
        print("------------------")

#Função - Volta menu
def menu_do_estoque():
    print("+++++++ Menu - Controle de estoque +++++++")
    print("1 - Cadastrar Produto")
    print("2 - Consultar Produto")
    print("3 - Atualizar Produto")
    print("4 - Excluir Produto")
    print("5 - Exibir Relatório de Produtos")
    print("6 - Encerrar")

# Lista - armazenar os produtos
produtos = []

while True:
    menu_do_estoque()
    opcao = input("Opção desejada: ")
    if opcao == "1":
        cadastrar(produtos)
    elif opcao == "2":
        fazer_consulta(produtos)
    elif opcao == "3":
        atualização(produtos)
    elif opcao == "4":
        exclusão_do_produto(produtos)
    elif opcao == "5":
        relatorio(produtos)
    elif opcao == "6":
        print("Terminando o programa")
        break
    else:
        print("Inválido. Digite novamente.")