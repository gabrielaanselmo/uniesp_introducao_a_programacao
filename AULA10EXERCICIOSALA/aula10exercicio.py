# Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). 
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, 
# se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

clubes = []

for clube in range(10):
    clubes.append(str(input(f"Digite o nome do clube: ")))

busca = (str(input("Digite o nome do clube que deseja buscar: ")))

if busca in clubes:
    print(f"ACHEI! {busca} está na lista de clubes!")
else:
    print(f"NÃO ACHEI! {busca} não está na lista de clubes!")

# Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. 
# Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. 
# Escrever a média da turma e o resultado da contagem.

notas = []

for nota in range(20):
    notas.append(int(input(f"Digite a nota do aluno: ")))

qtd_lista = len(notas)

soma = 0
for nota in notas:
    soma = soma + nota

media = soma / qtd_lista

qtd_alunos_media = 0
for nota_aluno in notas:
    if nota_aluno > media:
        qtd_alunos_media += 1

print(f"Média da turma: {media} com {qtd_alunos_media} alunos acima da média")

# Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
# o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
# o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

from random import randint

RAND_MIN = 1
RAND_MAX = 100

vetor = []

n = 0
while n < 20:
    numero = randint(RAND_MIN, RAND_MAX)
    vetor.append(numero)
    n += 1

menor = vetor[0]
maior = vetor[0]

for i in vetor:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

print(f"Lista: {vetor}")
print(f"Menor número {menor} posicionado em: {vetor.index(menor)} e Maior número {maior} posicionado em: {vetor.index(maior)}")

# Ler um vetor A de 10 números. 
# Após, ler mais um número e guardar em uma variável X. 
# Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. 
# Logo após, imprimir o vetor M.

from random import randint

vetor_a = []

for n in range(10):
    n = vetor_a.append(randint(0,100))

print(vetor_a)

x = randint(0,100)

print(x)

vetor_m = []

for c,v in enumerate(vetor_a):
    vetor_m.append(v * x)
    
print(vetor_m)

# Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B. 
# Exemplo: A[0] + B[0] deverá ser salva em N[0].

from random import randint

vetor_a = []
vetor_b = []
vetor_n = []

for i in range(10):
    a = vetor_a.append(randint(0,10))
    b = vetor_b.append(randint(0,10))

print(vetor_a)
print(vetor_b)

for c,v in enumerate(vetor_a):
    vetor_n.append(v + (vetor_b[c]))

print(vetor_n)

# Faça um algoritmo para ler um vetor de 20 números. 
# Após isto, deverá ser lido mais um número qualquer e verificar se esse número existe no vetor ou não. 
# Se existir, o algoritmo deve gerar um novo vetor sem esse número. (Considere que não haverão números repetidos no vetor).

from random import randint

lista = []

for l in range(20):
    lista.append(randint(0,100))

print(lista)

busca = (int(input("Digite o número para buscar na lista: ")))

if busca in lista:
    b = lista.index(busca)
    del lista[b]
print(lista)

# Faça um algoritmo para ler dois vetores V1 e V2 de 10 números cada. 
# Calcular e escrever a quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.

from random import randint

v1 = []
v2 = []

for v in range(10):
    v1.append(randint(0,10))
    v2.append(randint(0,10))

print(v1)
print(v2)

for n in range(len(v1)):
    if v1[n] == v2[n]:
        print(f"Os itens {v1[n]} e {v2[n]}, na posição {n} são iguais nas duas listas.")

# Faça um algoritmo para ler um vetor de 30 números. 
# Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

from random import randint

vetor = []

for v in range(30):
    vetor. append(randint(0,30))

print(vetor)

busca = (int(input("Qual número deseja buscar no vetor? ")))

if busca in vetor:
    print(f"O número {busca} aparece {vetor.count(busca)} vezes na lista.")
else:
    print(f"O número {busca} não aparece na lista.")