convidados = [
    "taeyeon", "tiffany", "irene", "seulgi", "baekhyung"
]

#convite
for nome in convidados:
    mensagem = f"e ai {nome}, bora pra ph?"
    print(mensagem)

#quem não vai poder ir
print("taeyeon: não poderei ir porque o baekhyung vai!")

print("tiffany: se a taeyeon não vai, não irei também!")

convidados[0] = "joy"
convidados[1] = "yeri"

#novo convite
for nome in convidados:
    mensagem = f"e ai {nome}, bora pra ph?"
    print(mensagem)