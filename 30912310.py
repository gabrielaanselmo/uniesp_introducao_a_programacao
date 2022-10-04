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