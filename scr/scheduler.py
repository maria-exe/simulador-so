# Implementação dos Escalonadores 
# Escalonadores implementados: FIFO, PRIOP e SRTF
from abc import ABC, abstractmethod

# Classe abstrata 
class Scheduler(ABC):
    @abstractmethod
    def select_next_task(self, ready_tasks, current_task):
        pass

class FCFS(Scheduler):
    def select_next_task(self, ready_tasks, current_task):
        if not ready_tasks:                    # verifica se a lista esta vazia
            return current_task
        return ready_tasks[0]                  # retorna a primeira tarefa da lista de prontos

class SRTF(Scheduler):
    def select_next_task(self, ready_tasks, current_task):
        if not ready_tasks:
            return current_task
        
        chosen = min(ready_tasks, key=lambda task: task._remaining_time) # retorna a com menor tempo restante 

        if current_task is None:    # nao tem tarefa executando no sistema 
            return chosen
        
        if chosen._remaining_time < current_task._remaining_time:
            return chosen

        return current_task

class PRIOP(Scheduler):
    def select_next_task(self, ready_tasks, current_task):
        if not ready_tasks:
            return current_task
        
        chosen = max(ready_tasks, key=lambda task: task.prio)
        
        if current_task is None:    # nao tem tarefa executando no sistema 
            return chosen

        if chosen.prio > current_task.prio: 
            return chosen
        
        return current_task

# Mapeia as strings dos algoritmos de escalonamento para sua funcao
schedulers = {
        "FCFS": FCFS,
        "SRTF": SRTF,
        "PRIOP": PRIOP,
        "RR": FCFS
}