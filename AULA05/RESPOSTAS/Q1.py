# Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.

numero = int(input("Digite um número: "))

if numero > 10:
    print(f"Seu número é maior que 10, o seu valor digitado foi: {numero}")

elif numero <10:
   print(f"Seu número é menor que 10, o seu valor digitado foi: {numero}")

else:
    print(f"Seu número é igual a 10, o seu valor digitado foi: {numero}")