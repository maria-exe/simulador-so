from tcb import TaskControlBlock

# Função para ler as configurações de um arquivo texto (.txt)
def ler_arquivo(caminho):
   
    lista_tarefas = []
    with open(caminho, 'r', encoding='utf-8') as txt: 
    
        p_linha = txt.readline().strip('\n').split(';') # Lê primeira linha para definir o Escalonador e o Quantum
        algoritimo = p_linha[0]
        quantum = int(p_linha[1])
   
        next(txt) # Pula a primeira linha
    
        for linha in txt: # Loop para as configurações das tarefas
            
            parte = linha.strip().split(';')
                 
            tarefa_id = parte[0]
            cor = parte[1] 
            ingresso = int(parte[2])
            duracao = int(parte[3])
            prioridade = int(parte[4])
            # eventos = parte[5] precisa ver como fazer essa parte
        
            nova_tarefa = TaskControlBlock(    # Instancia as tarefas
                tarefa_id = tarefa_id,
                cor = cor,
                ingresso = ingresso,
                duracao = duracao,
                prioridade = prioridade,
                # lista_eventos = eventos
            )
            
            lista_tarefas.append(nova_tarefa)   # Adiciona na lista de tarefas

    return algoritimo, quantum, lista_tarefas

