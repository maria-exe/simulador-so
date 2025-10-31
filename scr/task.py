from enum import Enum, auto
from scr.enums import TaskState

# Armazena as informações das tarefas antes, durante e depois da simulação
class TaskControlBlock:
    def __init__(self, t_id, color, start, duration, prio):
        
        self.id = t_id
        self.color = color
        self.start = start
        self.duration = duration
        self.prio = prio
        
        self._remaining_time = duration  # Tempo restante de execução
        self._waiting_time = 0           # Tempo de espera
        self._life_time = 0              # Tempo de vida da tarefa
        
        self._state = TaskState.NEW      # Estado da tarefa 
    
    # Metodos para visualizacao de informacoes das tarefas
    def __repr__(self):
        return (f"Task(id={self.id}, start={self.start}, state={self._state.name} "
                f"remaining={self._remaining_time}, waiting time={self._waiting_time})")
    
    def __str__(self):
        return (f"Tarefa {self.id}, inicio em: {self.start}, estado atual: {self._state.name}, " 
                f"tempo de espera: {self._waiting_time}, tempo restante de execucao: {self._remaining_time}")