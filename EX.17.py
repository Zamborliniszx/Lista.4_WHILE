meta = float(input("Digite a meta de arrecadação da campanha: R$"))

total = 0
pessoas = 0

while total < meta:
    try:
        doacao = float(input(f"Digite o valor da doação: R$"))

        if doacao <= 0:
            print("Valor de doação inválido!")
            continue

        total += doacao

        pessoas += 1

        restante = meta - total

        print(f"Faltam apenas R${restante:.2f}!! para atingir o total de R${meta:.2f}.")

    except ValueError:
        print("Por favor, digite um valor válido.")

if pessoas > 0:
    media = total / pessoas
else:
    media = 0

print("\nResultados da campanha:")
print("a) Meta estabelecida: R$", meta)
print("b) Total arrecadado: R$", total)
print("c) Quantidade de pessoas que participaram da campanha:", pessoas)
print("d) Valor médio doado por pessoa: R$", media)
