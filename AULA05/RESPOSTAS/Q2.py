# Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo (considere o valor zero como positivo).

numero = int(input("Digite um número: "))

if numero >= 0:
    print("O seu número é positivo")
else:
    print("Seu número é negativo")