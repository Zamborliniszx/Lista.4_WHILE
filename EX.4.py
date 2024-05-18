while True:
    try:
        numero = int(input("Digite um número inteiro (4 ou 9): "))

        if numero == 4 or numero == 9:
            print("Você acertou! O número", numero, "foi digitado.")
            break
        else:
            print("O número digitado não é 4 nem 9. Tente novamente.")
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

