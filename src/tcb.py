
# Definição da classe task control block
# Armazena as informações das tarefas antes, durante e depois da simulação

class TaskControlBlock:
    # Método Construtor
    def __init__(self, tarefa_id, cor, ingresso, duracao, prioridade, lista_eventos):
        
        self.id = tarefa_id
        self.cor = cor
        self.ingresso = ingresso
        self.duracao = duracao 
        self.prioridade = prioridade
        self.eventos = lista_eventos

        self.estado = 'Novo' # Estados da tarefa