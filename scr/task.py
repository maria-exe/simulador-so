from enum import Enum, auto

# Estados das tarefas
class TaskState(Enum):
    NEW = auto(),
    READY = auto(),
    RUNNING = auto(), 
    TERMINATED = auto(),
    SUSPENDED = auto()

# Armazena as informações das tarefas antes, durante e depois da simulação
class TaskControlBlock:
    def __init__ (self, t_id, color, start, duration, prio):
        
        self.id = t_id
        self.color = color
        self.start = start
        self.duration = duration
        self.prio = prio

        self._state = TaskState.NEW
        self._waiting_time = 0           # Tempo de espera
        self._life_time = 0              # Tempo de vida da tarefa
        self._remaining_time = duration  # Tempo restante de execução
    
    # adicionar método str ou repr