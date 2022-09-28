# Atividade Avaliativa - Questão 1

'''[FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), 
sendo que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raizes reais).'''

#import math

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

delta = math.pow(b, 2) - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"X1 -> {x1:.2f}")
    print(f"X2 -> {x2:.2f}")
    print(f"Delta -> {delta}")
else:
    print("Reduza os valores de A e C!")

# Atividade Avaliativa - Questão 2
'''[FORBELLONE, 2022] Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano,
P(x1, y1) e Q(x2, y2), imprima a distância entre eles.'''



# Atividade Avaliativa - Questão 3
'''Elabore um algoritmo que leia o valor de dois números inteiros e a operacão aritimética desejada; calcule, então, a resposta adequada. 
Utilize os símbolos da tabela a seguir para ler qual operacão aritmética escolhida.
'''




# Atividade Avaliativa - Questão 4
'''O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar a condição de peso de uma pessoa. 
A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de uma adulto e mostre sua condição.
'''

massa = float (input ("Diga seu peso em quilogramas:"))
altura = float (input("Diga a sua altura em metros:"))
imc = (massa/(altura**2))

if imc <18.5:
    print ("Seu IMC é de", imc)
    print ("Abaixo do peso ideal! Procure um especialista!")
elif 18.5< imc <24.99:
    print ("Seu IMC é de", imc)
    print ("Seu peso é ideal.")
elif 25< imc <30.00:
    print ("Seu IMC é de", imc)
    print ("Sobrepeso! Procure um especialista!")
else:
    print ("Seu IMC é de", imc)
    print ("Obesidade! Procure um especialista!")

# Atividade Avaliativa - Questão 5
'''Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos
: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo.
'''
n = 1
c1 = 0
c2 = 0
c3 = 0
c4 = 0

while n > 0:
    n = int(input("Digite um número: "))
    if n >= 0 and n <= 25: 
        c1 = c1 + 1
    elif n >= 26 and n <= 50:
        c2 = c2 + 1
    elif n >= 51 and n <= 75:
        c3 = c3 + 1
    elif n >= 76 and n <= 100:
        c4 = c4 + 1
    print("A quantidade de números entre 0 e 25 é: ", c1 "entre votos 26-50 é: ", c2 "entre votos 51-75 é: ", c3, "e entre votos 76-100 é: " c3)

# Atividade Avaliativa - Questão 6
'''Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 '''