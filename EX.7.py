vogais = 0
consoantes = 0
numeros = 0

while True:
    caractere = input("Digite um caractere (ou '#' para sair): ")

    if caractere == '#':
        break

    if caractere.isalpha():
        if caractere.lower() in 'aeiou':
            vogais += 1
        else:
            consoantes += 1

    elif caractere.isdigit():
        numeros += 1

print("Quantidade de vogais:", vogais)
print("Quantidade de consoantes:", consoantes)
print("Quantidade de números:", numeros)
