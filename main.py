print("== ORGANIZADOR DE TAREFAS ==")
print("1 - Adicionar tarefas")
print("2 - Listar tarefas")
print("3 - Sair")

opcao = input("Escolha a opção: ")

if opcao == "2":
    print("Você escolheu listar tarefas!")
elif opcao == "1":
    print("Você escolheu adicionar tarefas!")
elif opcao == "3":
    print("Saindo do organizador de tarefas...")
else:
    print("Opção inválida. Tente novamente.")
    