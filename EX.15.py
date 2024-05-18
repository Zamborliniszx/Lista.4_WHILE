n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

menor = min(n1, n2)
maior = max(n1, n2)

print("Números no intervalo entre", menor, "e", maior, "são:")
for n in range(menor, maior + 1):
    print(n, end=" ")