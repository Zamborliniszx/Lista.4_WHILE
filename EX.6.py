soma = 0
contador = 0

while soma < 100:
    try:
        n = int(input("Digite um número inteiro: "))

        soma += n

        contador += 1

    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print("Foram digitados", contador, "números.")
