menu = """ 
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido. O valor do depósito deve ser positivo.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        if valor <= 0:
            print("Valor inválido. O valor do saque deve ser positivo.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("O valor do saque excede o limite por operação (R$ 500).")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo em conta: R$ {saldo:.2f}")
        print("=============================\n")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
