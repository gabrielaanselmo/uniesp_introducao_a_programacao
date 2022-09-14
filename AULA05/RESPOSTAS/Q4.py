# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

avaliacao1 = int(input("Qual foi a sua nota 1a? "))
avaliacao2 = int(input("Qual foi a sua nota 2a? "))

resultado = (avaliacao1 + avaliacao2) / 2
if resultado >=6:
    print(f"Parabéns, você foi aprovado/a! A sua média é: {resultado}")
else:
    print(f"Infelizmente você foi reprovado. Ano que vem nos vemos de novo! A sua média é: {resultado}")