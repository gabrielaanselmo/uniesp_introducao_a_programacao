# Questão 01 - # Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). 
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, 
# se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário

# Primeiro jeito de se fazer
times = []
times.append(input("Digite o primeiro clube: "))
times.append(input("Digite o segundo clube: "))
times.append(input("Digite o terceiro clube: "))
times.append(input("Digite o quarto clube: "))
times.append(input("Digite o quinto clube: "))
times.append(input("Digite o sexto clube: "))
times.append(input("Digite o sétimo clube: "))
times.append(input("Digite o oitavo clube: "))
times.append(input("Digite o nono clube: "))
times.append(input("Digite o décimo clube: "))

buscar = str(input("Digite o clube que deseja buscar na lista: "))

if buscar in times:
    print(f"ACHEI! {buscar} está na lista!")
else:
    print(f"NÃO ACHEI! {buscar} não está na lista")

# Segundo jeito de se fazer
times = []

while True:
    clubes = input("Digite o nome de um Clube de futebol: ")

    if len(clubes) > 0:
        times.append(clubes)
        print(times)

    if len(times) > 10:
        print("Você já adicionou 10 clubes!")
        break

    for clubes in times:
        selecao = input("Quer que eu ache algum time?[S/N]: ")
        if selecao == "S":
            part2 = input("Qual time?:")
            indice = times.index(part2)
            print("Achei!")
        else:
            print("Não achei")
            if selecao == "N":
                break

# Questão 02 - # Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, 
# calcular e escrever quantas vezes esse número aparece no vetor.

from random import randint

v1 = []

for n in range(30):
    v1.append(randint(0, 31))

print(v1)

b1 = int(input("Digite o número que deseja buscar na lista: "))

if b1 in v1:
    print(f"O número {b1} aparece {v1.count(b1)} vezes na lista")
else:
    print(f"O número {b1} não está na lista.")