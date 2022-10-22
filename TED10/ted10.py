#Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, 
# se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário

# Lista
lista_futebol = []

while True:
    op = int(input("1 - Adicionar time de futebol\n \
                2 - Ler lista dos times \n \
                3 - Sair \n \
                Digite a opção: \n \
                "))
    
    if op == 1:
        # Adicionar objetos a lista
        time = (input("Adicione um time de futebol: "))
        lista_futebol.append(time)

    elif op == 2:
        # Lendo lista dos times
        for lista in lista_futebol:
            print(lista)
            
    elif op == 3:
        break

