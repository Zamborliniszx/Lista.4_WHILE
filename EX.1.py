npar = 0

while True:
    try:
        n = int(input("Digite um número inteiro: "))

        if n % 2 == 0:
            npar += 1

        if n % 2 != 0:
            break
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print("Quantidade de números pares digitados:", npar)
