
# Definição da classe task control block
# Armazena as informações das tarefas antes, durante e depois da simulação

class TaskControlBlock:

    def __init__ (self, t_id, color, start, duration, prio):
        
        self.id = t_id
        self.color = color
        self.start = start
        self.duration = duration
        self.prio = prio

        self.state = 'New'
