maior = float('-inf')  # Inicializa com o menor valor possível
menor = float('inf')  # Inicializa com o maior valor possível

contador = 1

while contador <= 7:
    try:
        n = int(input(f"Digite o {contador}º número inteiro: "))

        if n > maior:
            maior = n
        if n < menor:
            menor = n

        contador += 1
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print("O maior número lido é:", maior)
print("O menor número lido é:", menor)
