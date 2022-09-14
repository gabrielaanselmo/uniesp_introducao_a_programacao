# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

conta = 83964
saldo = 30000

total_debitos = int(input("Olá, quanto você gastou esse mês: "))
total_creditos = int(input("Olá, quanto você recebeu esse mês: "))

saldo_atual = (saldo - total_debitos + total_creditos)

if saldo_atual > 0:
    print(f"Saldo positivo, seu saldo atual é: {saldo_atual}")
else:
    print(f"Saldo negativo, seu saldo atual é: {saldo_atual}")