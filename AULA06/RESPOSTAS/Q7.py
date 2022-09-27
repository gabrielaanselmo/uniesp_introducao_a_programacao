cadastros = []

botao=1000
while botao != 0:
    print("Digite 1 para cadastrar um novo usuário")
    print("Diigite 2 para imprimir todos os usuários")
    print("Digite 0 para sair")
    botao = int(input("Digite a opção desejada: "))

    if botao == 1:
        #entrada dos dados
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite sua idade: "))
        email = input("Digite o seu e-mail: ")

        #folha de cadastro
        dados = [nome, idade, email]
        #guardando folha na pasta
        cadastros.append(dados)

    elif botao == 2:
        for p in cadastros:
            print(p)
    elif botao == 0:
        print("Obrigado por acessar este software!")
    else:
        print("Digite um número válido!")