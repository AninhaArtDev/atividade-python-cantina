quantidade_motos = 0
quantidade_carros = 0
quantidade_caminhonetes = 0
valor_arrecadado = 0

opcao = 0

while opcao != 6:
    print("ESTACIONAMENTO")
    print("1 - Registrar Moto")
    print("2 - Registrar Carro")
    print("3 - Registrar Caminhonete")
    print("4 - Mostrar quantidade de veículos")
    print("5 - Mostrar valor arrecadado")
    print("6 - Encerrar programa")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        quantidade_motos = quantidade_motos + 1
        valor_arrecadado = valor_arrecadado + 5
    elif opcao == 2:
        quantidade_carros = quantidade_carros + 1
        valor_arrecadado = valor_arrecadado + 10
    elif opcao == 3:
        quantidade_caminhonetes = quantidade_caminhonetes + 1
        valor_arrecadado = valor_arrecadado + 15
    elif opcao == 4:
        total_veiculos = quantidade_motos + quantidade_carros + quantidade_caminhonetes
        print("Total de veículos:", total_veiculos)
    elif opcao == 5:
        print("Valor arrecadado: R$", valor_arrecadado)
    elif opcao == 6:
        print("Programa encerrado.")
    else:
        print("Opção inválida")