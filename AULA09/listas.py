# Lista
frutas = ["pêra", "uva", "maça", "kiwi"]

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

print(f"juliana gosta de {frutas[3]}")

# Trocando de lugar
print(frutas)
frutas.insert(2, "Morango")
print(frutas)

# Substituindo 
frutas[0] ="Melancia"
print(frutas)

# Deletando
print(frutas)
del frutas[3]
print(frutas)

# Procurando o índice
indice_fruta = frutas.index("Melancia")
print(f"O índice da fruta é {indice_fruta}")
del frutas[indice_fruta]
print(frutas)

