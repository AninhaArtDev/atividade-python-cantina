quantidade_alunos = 0
quantidade_aprovados = 0
quantidade_recuperacao = 0
quantidade_reprovados = 0

opcao = 0

while opcao != 6:
    print("CONTROLE DE NOTAS")
    print("1 - Cadastrar notas de um aluno")
    print("2 - Mostrar quantidade de alunos cadastrados")
    print("3 - Mostrar quantidade de aprovados")
    print("4 - Mostrar quantidade de recuperação")
    print("5 - Mostrar quantidade de reprovados")
    print("6 - Encerrar")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("CADASTRO")
        primeira_nota = float(input("Digite a primeira nota: "))
        segunda_nota = float(input("Digite a segunda nota: "))
        media = (primeira_nota + segunda_nota) / 2
        print("Média:", media)

        quantidade_alunos = quantidade_alunos + 1

        if media >= 7:
            print("Situação: Aprovado")
            quantidade_aprovados = quantidade_aprovados + 1
        elif media >= 5:
            print("Situação: Recuperação")
            quantidade_recuperacao = quantidade_recuperacao + 1
        else:
            print("Situação: Reprovado")
            quantidade_reprovados = quantidade_reprovados + 1
    elif opcao == 2:
        print("Total de alunos cadastrados:", quantidade_alunos)
    elif opcao == 3:
        print("Total de aprovados:", quantidade_aprovados)
    elif opcao == 4:
        print("Total em recuperação:", quantidade_recuperacao)
    elif opcao == 5:
        print("Total de reprovados:", quantidade_reprovados)
    elif opcao == 6:
        print("Programa encerrado.")
    else:
        print("Opção inválida")