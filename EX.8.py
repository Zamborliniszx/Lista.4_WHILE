maior10 = 0
igual10 = 0
menor10 = 0

# Loop para ler os 15 números inteiros
for _ in range(15):
    try:
        n = int(input("Digite um número inteiro: "))

        if n > 10:
            maior10 += 1

        elif n == 10:
            igual10 += 1

        elif n < 10:
            menor10 += 1

    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print("Quantidade de números maiores que 10:", maior10)
print("Quantidade de números iguais a 10:", igual10)
print("Quantidade de números menores que 10:", menor10)
