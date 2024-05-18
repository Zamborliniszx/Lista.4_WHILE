saldo = 0.0

while True:
    print("\nOpções:")
    print("1. Consultar saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        print(f"Seu saldo é R$ {saldo:.2f}")
    elif escolha == '2':
        saque = float(input("Digite o valor que deseja sacar: R$ "))
        if saque > saldo:
            print("Saldo insuficiente! Não é possível realizar o saque.")
        else:
            saldo -= saque
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
            print(f"Saldo atualizado: R$ {saldo:.2f}")
    elif escolha == '3':
        deposito = float(input("Digite o valor que deseja depositar: R$ "))
        if deposito < 0:
            print("Valor de depósito inválido! Não é possível depositar um valor negativo.")
        else:
            saldo += deposito
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
            print(f"Saldo atualizado: R$ {saldo:.2f}")
    elif escolha == '4':
        print("Obrigado por utilizar nossos serviços. Volte sempre!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
