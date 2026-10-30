
total = 0
quantidade = 0

while True:
    print("\nCANTINA ESCOLAR")
    print("1 - Suco       R$ 5,00")
    print("2 - Salgado    R$ 7,00")
    print("3 - Sanduíche  R$ 10,00")
    print("4 - Finalizar compra")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        total += 5
        quantidade += 1
        print("Suco adicionado na sacola")

    elif opcao == 2:
        total += 7
        quantidade += 1
        print("Salgado adicionado na sacola")

    elif opcao == 3:
        total += 10
        quantidade += 1
        print("Sanduíche adicionado na sacola")

    elif opcao == 4:
        print("\n Notinha da compra")
        print(f"Quantidade de produtos: {quantidade}")
        print(f"Total da compra: R$ {total:.2f}")
        print("Compra finalizada. Obrigada por comprar!")
        break

    else:
        print("Opção inválida, Tente novamente.")
