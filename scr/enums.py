from enum import Enum, auto

# Estados das tarefas
class TaskState(Enum):
    NEW = auto(),
    READY = auto(),
    RUNNING = auto(), 
    TERMINATED = auto(),
    SUSPENDED = auto()