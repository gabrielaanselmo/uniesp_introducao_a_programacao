# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O maior número digitado foi: {numero1}")
elif numero1 < numero2:
    print(f"O maior número digitado foi: {numero2}")
else:
    print("Os números são iguais")