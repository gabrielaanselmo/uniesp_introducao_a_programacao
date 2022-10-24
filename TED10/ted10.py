# Questão 01 -

times = []

while True:
    clubes = input("Digite até 10 nomes de clubes de futebol: ")

    if len(clubes) > 0:
        times.append(clubes)
        print(times)

    if len(times) > 10:
        print("Você já adicionou 10 clubes!")
        break

    for clubes in times:
        selecao = input("Quer que eu ache algum time? [SIM/NÃO]: ")
        if selecao == "SIM":
            part2 = input("Qual time você quer achar?:")
            indice = times.index(part2)
            print("Achei!")
        elif selecao == "NÃO":
            break

