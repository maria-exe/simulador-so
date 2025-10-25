from enum import Enum, auto

# Estados das tarefas

class TaskState(Enum):
    NEW = auto(),
    READY = auto(),
    RUNNING = auto(), 
    TERMINATED = auto(),
    SUSPENDED = auto()


# Definição da classe task control block
# Armazena as informações das tarefas antes, durante e depois da simulação

class TaskControlBlock:

    def __init__ (self, t_id, color, start, duration, prio):
        
        self.id = t_id
        self.color = color
        self.start = start
        self.duration = duration
        self.prio = prio

        self._state = TaskState.NEW

        self._waiting_time = 0
        self._life_time = 0

        self._remaining_time = duration
        

 