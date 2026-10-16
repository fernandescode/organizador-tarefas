from pathlib import Path

tarefas = []
arquivo_tarefas = Path("tarefas.txt")

if arquivo_tarefas.exists():
    with open(arquivo_tarefas, "r") as arquivo:
        for linha in arquivo:
            tarefa = linha.strip()
            tarefas.append(tarefa)
            
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
        with open(arquivo_tarefas, "a") as arquivo:
            arquivo.write(tarefa + "\n")
        print("Tarefa cadastrada:", tarefa)
        
    elif opcao == "3":
        print("Saindo do organizador de tarefas...")
        
    else:
        print("Opção inválida. Tente novamente.")
    