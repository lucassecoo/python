tarefas = []
desfeitas = []

while True:
    def comandos():
        print('')
        print('Comandos: listar, desfazer, refazer')
        comando = input('Digite uma tarefa ou um comando: ')
        match comando:
            case 'listar':
                print(f'Tarefas:')
                for i in range(len(tarefas)):
                    print(tarefas[i])
            case "desfazer":
                if tarefas:
                    desfeitas.append(tarefas[-1])
                    tarefas.pop()
                else:
                    print('nenhuma tarefa para excluir')
            case 'refazer':
                if desfeitas:
                    tarefa_refazer = desfeitas[-1]
                    tarefas.append(tarefa_refazer)
                    desfeitas.pop()
                else:
                    print('nao tem oq refazer')
            case _:
                tarefas.append(comando)

    
    comandos()
                
        