soma = 0
contador = 0

while True:
    try:
        n = int(input("Digite um número inteiro (digite 0 para encerrar): "))

        if n == 0:
            break

        soma += n

        contador += 1

    except ValueError:
        print("Por favor, digite apenas números inteiros.")

if contador > 0:
    media = soma / contador
    print("A média dos valores lidos é:", media)
else:
    print("Nenhum valor foi lido.")
