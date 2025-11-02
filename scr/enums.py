from enum import Enum, auto
# Estados das tarefas
class TaskState(Enum):
    NEW = auto(),
    READY = auto(),
    RUNNING = auto(), 
    TERMINATED = auto(),
    SUSPENDED = auto()

class Scheduler(Enum):
    FCFS   = 1
    SRTF   = 2
    PRIOP  = 3

