from .enums import TaskState
from .clock import SystemClock
from .scheduler import schedulers

# cada posicao da lista de um struct que armazena as informacoes de cada tick
class Simulator():
    def __init__(self, scheduler, quantum, tasks_list):
        self.clock = SystemClock()
        
        valid_scheduler = schedulers.get(scheduler) # verifica que o scheduler esta no dicionario
        if not valid_scheduler:
            raise ValueError(f"Escalonador '{scheduler}' inválido")
        self.scheduler = valid_scheduler()

        self.quantum = quantum
        self.tasks_list = tasks_list
        self.ready_tasks = []
        self.running_task = None
        
    def tasks(self):
        for task in self.tasks_list:
           print(str(task))

    def add_ready_tasks(self):
        for task in self.tasks_list:
            if task.start == self.clock.current_time and task.state == TaskState.NEW:
                task.state = TaskState.READY
                self.ready_tasks.append(task)
   
    # Método para execução passo a passo
    def step (self):
        pass

    def complete_simulation (self): 
        simulation_data = []

        # a cada tick verificar se uma tarefa nova chegou no sistema  }

        return simulation_data
    
    # Método para execução completa
    
