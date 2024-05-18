while True:
    s1 = int(input("Digite o valor do sensor S1 (0 ou 1): "))

    s2 = int(input("Digite o valor do sensor S2 (0 ou 1): "))

    s3 = int(input("Digite o valor do sensor S3 (0 ou 1): "))

    if s1 == 1 and s2 == 0 and s3 == 1:
        print("Combinação correta! Programa encerrado!")
        break
    else:
        print("Sequência incorreta. Tente novamente.")

