# As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

preco1 = 1
preco2 = 1.30

qtd_macas = int(input("Quantas maças você irá comprar? "))
custo1 = preco1 * qtd_macas
custo2 = preco2 * qtd_macas

if qtd_macas < 12:
    print(f" O seu custo total é: {custo2}")
else:
    print(f"O seu custo total é: {custo1}")