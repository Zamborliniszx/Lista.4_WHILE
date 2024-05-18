while True:
    try:
        n = int(input("Digite um número inteiro dentro do intervalo de 30 a 40: "))

        if 30 <= n <= 40:
            print("O número", n, "está dentro do intervalo de 30 a 40.")
        else:
            print("O número está fora do intervalo de 30 a 40. Tente novamente.")
            continue
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
        continue

    continuar = input("Deseja continuar? (S/N): ")
    if continuar.upper() != "S":
        break
