# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"{numero1},{numero2}")
elif numero1 < numero2:
    print(f"{numero2},{numero1}")
#else:
    #print("Os números são iguais")