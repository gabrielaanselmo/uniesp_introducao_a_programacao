# Use um dicionário para armazenar informações sobre uma pessoa que você conheça. 
# Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive.
# Você deverá ter chaves como primeiro_nome, sobrenome, idade e cidade.
# Por fim, mostre cada informação armazenada em seu dicionário.

dados = {"primeiro_nome": "Gabriela", "sobrenome": "Anselmo", "idade": 19, "cidade": "Cabedelo"}
print(dados.keys())
print(dados.values())
print(dados.items())

for k,v in dados.items():
    print(f"A chave e o valor deste item são: {k} e {v}.")

# Use um dicionário para armazenar os números favoritos de algumas pessoas.
# Escolha cinco colegas, e pergunte quais seus números favoritos.
# Use seus nomes para serem as chaves de cada número favorito. 
# Ao final, exiba o nome de cada pessoa e seu número favorito.

nprefer = {"Gabriela": 7, "Leticia": 19, "Yasmin": 13, "Suely": 25, "Amanda": 26}

for k,v in nprefer.items():
    print(f'O número preferido de {k} é {v}.')