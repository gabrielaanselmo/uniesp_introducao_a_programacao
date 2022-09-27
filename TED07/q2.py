# Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano_atual = int(input("Digite o ano atual: "))
idade = int(input("Entre com seu ano de nascimento: "))

if idade < 2006:
    print("Este ano você poderá votar.: ")
elif idade >= 2006:
    print("Este ano você não poderá votar: ")