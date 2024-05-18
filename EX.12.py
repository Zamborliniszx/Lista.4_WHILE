# Solicita ao usuário que digite os dois números float
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma = n1 + n2

tentativas = 0

while True:
    resultado = float(input("Informe o resultado da soma: "))

    # Incrementa o contador de tentativas
    tentativas += 1

    # Verifica se o resultado informado está correto
    if resultado == soma:
        print("Parabéns! Você acertou o resultado após", tentativas, "tentativas.")
        break
    else:
        print("Resultado incorreto! Tente outra vez.")

