# cast = transformar um tipo de dado em outro
# dados = int = numeros inteiros, str = todos os caracteres do teclado, bool = true ou false, float = numero quebrado

nota = 10.0

if nota <5:
    print("Reprovado!")
elif (nota >=5) and (nota <= 6):
    print("Recuperação!")
elif (nota >=7) and (nota <=10):
    print("Aprovado!")
else:
    print("Nota fora do intervalo!")

#    

nota = int(input("Digite uma nota:"))

if nota <5:
    print("Reprovado!")
elif (nota >=5) and (nota <= 6):
    print("Recuperação!")
elif (nota >=7) and (nota <=10):
    print("Aprovado!")
else:
    print("Nota fora do intervalo!")