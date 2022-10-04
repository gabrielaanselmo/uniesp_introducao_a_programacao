# Aluno(a): Maria Gabriela Ansemlmo de Souza Batista

# Atividade Avaliativa - Questão 1

#[FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), 
#sendo que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raizes reais).

import math

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
#[FORBELLONE, 2022] Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano,
#P(x1, y1) e Q(x2, y2), imprima a distância entre eles.#

import math

x1 = float(input("Digite o valor de X1: "))
y1 = float(input("Digite o valor de Y1: "))
x2 = float(input("Digite o valor de X2: "))
y2 = float(input("Digite o valor de Y2: "))

D = math.sqrt((x1-y1)**2 + (x2 - y2)**2)

print(f"A distância destes pontos {x1},{y1},{x2} e {y2} é de: {D}")

# Atividade Avaliativa - Questão 3
#Elabore um algoritmo que leia o valor de dois números inteiros e a operacão aritimética desejada; calcule, então, a resposta adequada. 
#Utilize os símbolos da tabela a seguir para ler qual operacão aritmética escolhida.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um outro número: "))
operacao = input("Qual operação você vai utilizar (+,-,,/ ou *): ")

if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    resultado = n1 / n2
else:
    print("Operação inválida!")
    resultado = 0   
print("Resultado: ", resultado)


# Atividade Avaliativa - Questão 4
#O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar a condição de peso de uma pessoa. 
#  A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de uma adulto e mostre sua condição.

massa = float(input ("Diga seu peso em quilogramas:"))
altura = float(input("Diga a sua altura em metros:"))
imc = (massa/(altura**2))

if imc <18.5:
    print("Seu IMC é de", imc)
    print("Abaixo do peso ideal! Procure um especialista!")
elif 18.5< imc <24.99:
    print("Seu IMC é de", imc)
    print("Seu peso é ideal.")
elif 25< imc <30.00:
    print("Seu IMC é de", imc)
    print("Sobrepeso! Procure um especialista!")
else:
    print("Seu IMC é de", imc)
    print("Obesidade! Procure um especialista!")

# Atividade Avaliativa - Questão 5
#Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos
#: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo.

n = int(input("Quantos números?: "))
i = 0
a = 0
b = 0
c = 0
d = 0

while i < n: 
    numero = int(input("Insira um número: "))
    i = i + 1
    print(i)
    if numero < 0: 
        break
    if numero >= 0 and numero <= 25: 
        a = a + 1
    if numero >= 26 and numero <= 50: 
        b = b + 1
    if numero >= 51 and numero <= 75: 
        c = c + 1
    if numero >= 76 and numero <= 100: 
        d = d + 1
print
("Intervalo1: ",a)
print
("Intervalo2: ",b)
print
("Intervalo3: ",c)
print
("Intervalo4: ",d)

# Atividade Avaliativa - Questão 6
#Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

def main():
    A = int(input("Digite o valor de A: "))
    fat = 1
    i = 2
    while i <= A:
        fat = fat*i
        i = i + 1

    print("O valor de %d! é =" %A, fat)

main()