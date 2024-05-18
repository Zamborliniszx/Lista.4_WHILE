soma = 0
contador = 0

while True:
    try:
        numero = float(input("Digite um número real: "))

        soma += numero

        contador += 1

        continuar = input("Digite 's' para continuar informando números ou qualquer outra tecla para encerrar: ")

        if continuar.lower() != 's':
            break

    except ValueError:
        print("Por favor, digite um número real válido.")

if contador > 0:
    media = soma / contador
    print("A média dos valores digitados é:", media)
else:
    print("Nenhum número foi digitado.")
