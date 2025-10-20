# definição da classe task control block
# armazena as informações das tarefas antes, durante e depois da simulação

class TaskControlBlock:
    def __init__(self, tarefa_id, cor, ingresso, duracao, prioridade):
        self.id = tarefa_id
        self.cor = cor
        self.ingresso = ingresso
        self.duracao = duracao 
        self.prioridade = prioridade

