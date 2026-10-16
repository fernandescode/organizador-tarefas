tarefas = []
opcao = ""

while opcao != "3":
    print("== ORGANIZADOR DE TAREFAS ==")
    print("1 - Adicionar tarefas")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Escolha a opção: ")

    if opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada!")
        else:
            for tarefa in tarefas:
                print(tarefa)
                
    elif opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa cadastrada:", tarefa)
        
    elif opcao == "3":
        print("Saindo do organizador de tarefas...")
        
    else:
        print("Opção inválida. Tente novamente.")
    