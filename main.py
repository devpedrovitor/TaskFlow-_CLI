tarefas = [ 
        {
            "id": 0,
            "name_task": "Leitura",
            "tipo_task": "Leitura",
            "data_inicio": "20/12/25",
            "data_vencimento": "22/01/26",
            "Complete": True
        },
        {
            "id": 1,
            "name_task": "Passear com o cachorro",
            "tipo_task": "tarefas Pessoal",
            "data_inicio": "20/12/25",
            "data_vencimento": "22/01/26",
            "Complete": True
        }
]

def Add_Task():
    while True:
        print("--- Criar nova tarefas ---")
        # tarefas.append({
        #     "id": 0,
        #     "name_task": input("Digite o nome da tarefas: "),
        #     "tipo_task": input("Digite o tipo da tarefas: "),
        #     "data_inicio": input("Digite a data de inicio da tarefas ( dd/mm/yyyy): "),
        #     "data_fim": input("Digite a data de vencimento da tarefas ( dd/mm/yyyy): "),
        #     "is_complete": False
        # })
        tarefas.append()
        print("tarefas adicionada com sucesso...")
        menu()
        break;
    

def viewTaks():
    print("--- Lista de tarefass ---")
    count = 0
    while count < len(tarefas):
        dic = tarefas[count]
        name_task = dic.get("name_task")
        print(f"{count + 1}. {name_task}")
        count += 1

    print("Toda as tarefass foram exibidas..")

def editTask():
    print("--- Edit Task ---")
    count =  0
    while count < len(tarefas):
        dic = tarefas[count]
        name_task = dic.get("name_task")
        print(f"{count + 1}. {name_task}")
        count += 1

    answer = input("Digite o nome da tarefas que você vai editar: ")
    task_encontrada = None

    for editTask in tarefas:
        if editTask["name_task"] == answer:
            task_encontrada = editTask
            break;

    if task_encontrada:
        novo_nome = input(f"Digite o novo nome da task {task_encontrada['name_task']}: ")
        novo_tipo = input(f"Digite o novo tipo da task {task_encontrada['name_task']}: ")
        nova_data = input(f"Digite a nova data de inicio da task {task_encontrada['name_task']}: ")
        nova_data_vencimento = input(f"Digite a nova data de vencimento da task  {task_encontrada['name_task']}: ")
        novo_stats = bool(input(f"Essa tarefas foi completada?: "))

        task_encontrada['name_task'] = novo_nome
        task_encontrada['tipo_task'] = novo_tipo
        task_encontrada['data_inicio'] = nova_data
        task_encontrada['data_vencimento'] = nova_data_vencimento
        task_encontrada['Complete'] = novo_stats
    else:
        print("Task não encontrada")
    


def vertarefassCompletas():
    print("--- Task Sucess ---")
    count =  0
    while count < len(tarefas):
        dic = tarefas[count]
        if dic['Complete']:
            name_task = dic.get("name_task")
            print(f"{count + 1}. {name_task}")
            count += 1
        
    
def deleteTask():
    for tarefa in tarefas[:]:
        if tarefa['Complete']:
            tarefas.remove(tarefa)

    print("tarefass concluidas deletadas")
    menu()


def menu():
    while True:
        print("---- Gerenciador de tarefass ----")
        print("1. Adicionar  tarefas.")
        print("2. Ver tarefass.")
        print("3. Editar tarefass.")
        print("4. Ver tarefass Completas.")
        print("5. Deletar tarefass completas.")
        print("6. Sair")

        answer = int(input("Digite sua escolha: "))
        if answer == 1:
            Add_Task()
            break;
            
        if answer == 2:
            viewTaks()
            break;

        if answer == 3:
            editTask()
            break;

        if answer == 4:
            vertarefassCompletas()
            break;

        if answer == 5:
            deleteTask()
            break;

        if answer == 6:
            break;

menu()