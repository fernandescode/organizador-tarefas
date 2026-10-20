from pathlib import Path

tarefas = []
arquivo_tarefas = Path("tarefas.txt")

if arquivo_tarefas.exists():
    with open(arquivo_tarefas, "r") as arquivo:
        for linha in arquivo:
            tarefa = linha.strip()
            tarefas.append(tarefa)
            
opcao = ""

while opcao != "5":
    print("== ORGANIZADOR DE TAREFAS ==")
    print("1 - Adicionar tarefas")
    print("2 - Listar tarefas")
    print("3 - Excluir tarefa")
    print("4 - Editar tarefa")
    print("5 - Sair")

    opcao = input("Escolha a opção: ")

    if opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada!")
        else:
            for indice, tarefa in enumerate(tarefas, start=1):
                print(indice, "-", tarefa)
                
    elif opcao == "1":
        tarefa = input("Digite a tarefa: ").strip()
        if not tarefa:
            print("A tarefa não pode ficar vazia!")
            continue

        tarefas.append(tarefa)

        with open(arquivo_tarefas, "a") as arquivo:
            arquivo.write(tarefa + "\n")
        print("Tarefa cadastrada:", tarefa)
        
    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada!")
        else:
            for indice, tarefa in enumerate(tarefas, start=1):
                print(indice, "-", tarefa)
            escolha = input("Digite o número da tarefa que deseja excluir: ")
            try:
                escolha = int(escolha)
            except ValueError:
                print("Digite um número válido!")
                continue
            if 1 <= escolha <= len(tarefas):
                tarefa_removida = tarefas.pop(escolha - 1)
                print("Tarefa removida:", tarefa_removida)
                with open(arquivo_tarefas, "w") as arquivo:
                    for tarefa in tarefas:
                        arquivo.write(tarefa + "\n")
            else:
                print("Número de tarefa inválido!")

    elif opcao == "4":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada!")
        else:
            for indice, tarefa in enumerate(tarefas, start=1):
                print(indice, "-", tarefa)

            escolha = input("Digite o número da tarefa que deseja editar: ")

            try:
                escolha = int(escolha)
            except ValueError:
                print("Digite um número válido!")
                continue

            if 1 <= escolha <= len(tarefas):
                tarefa_atual = tarefas[escolha - 1]
                print("Tarefa atual:", tarefa_atual)

                nova_tarefa = input("Digite o novo texto da tarefa: ").strip()

                if not nova_tarefa:
                    print("A tarefa não pode ficar vazia!")
                    continue

                tarefas[escolha - 1] = nova_tarefa
                print("Tarefa atualizada:", nova_tarefa)

                with open(arquivo_tarefas, "w") as arquivo:
                    for tarefa in tarefas:
                        arquivo.write(tarefa + "\n")
            else:
                print("Número de tarefa inválido!")

    elif opcao == "5":
        print("Saindo do organizador de tarefas...")
        
    else:
        print("Opção inválida. Tente novamente.")
    