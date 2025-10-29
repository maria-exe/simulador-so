from .task import TaskControlBlock, TaskState
from .scheduler import schedulers

class SystemClock: 
    def __init__(self):
        self._current_tick = 0

    def tick(self): 
        self._current_tick += 1 

    @property
    def current_time(self):
        return self._current_tick

class Simulator():
    def __init__(self, scheduler, quantum, tasks_list):
        self.clock = SystemClock()
        
        valid_scheduler = scheduler.get(scheduler) # verifica que o scheduler esta no dicionario
        if not valid_scheduler:
            raise ValueError(f"Escalonador '{scheduler}' inválido")
        self.scheduler = valid_scheduler()

        self.quantum = quantum
        self.tasks_list = tasks_list
        self.ready_tasks = []
        self.running_task = None
    
    def add_ready_tasks(self):
        for task in self.tasks_list:
            if task.start == self.tick and task.state == TaskState.NEW:
                task.state = TaskState.READY
                self.ready_tasks.append(task)
   
    # Método para execução passo a passo
    def step (self): 
        pass
    
    # Método para execução completa
    
