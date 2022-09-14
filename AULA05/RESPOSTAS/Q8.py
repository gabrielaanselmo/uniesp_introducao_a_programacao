# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

qtd_atual = int(input("Qual a quantidade atual do estoque: "))
qtd_maxima = int(input("Qual a quantidade máxima do estoque: "))
qtd_minima = int(input("Qual a quantidade mínima do estoque: "))

qtd_media = (qtd_maxima + qtd_minima)/2
qtd_compra = (qtd_minima - qtd_atual)

if qtd_atual >= qtd_media:
    print("Não efetuar compra")
else:
    print(f"Efetuar compra de: {qtd_compra} unidades")