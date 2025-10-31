# Implementação dos Escalonadores 
# Escalonadores implementados: FIFO, PRIOP e SRTF
from abc import ABC, abstractmethod

# Classe abstrata 
class Scheduler(ABC):
    @abstractmethod
    def select_next_task(self, ready_tasks):
        pass

class FCFS(Scheduler):
    def select_next_task(self, ready_tasks):
        if not ready_tasks:                    # verifica se a lista esta vazia
            return None
        return ready_tasks[0]                  # retorna a primeira tarefa da lista de prontos

class SRTF(Scheduler):
    def select_next_task(self, ready_tasks):
        if not ready_tasks:
            return None
        return min(ready_tasks, key=lambda task: task._remaining_time) # retorna a com menor tempo restante 

class PRIOP(Scheduler):
    def select_next_task(self, ready_tasks):
        if not ready_tasks:
            return None
        return max(ready_tasks, key=lambda task: task.prio)            # retorna a com maior prioridade

# Mapeia as strings dos algoritmos de escalonamento para sua funcao
schedulers = {
        "FCFS": FCFS,
        "SRTF": SRTF,
        "PRIOP": PRIOP
}