while True:
    try:
        numero = int(input("Digite um número inteiro: "))

        if 20 <= numero <= 30:
            print("Você acertou! O número", numero, "está no intervalo de 20 a 30.")
            break
        else:
            print("O número não está no intervalo de 20 a 30. Tente novamente.")
    except ValueError:
        print("Por favor, digite apenas números inteiros.")