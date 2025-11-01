from .enums import TaskState
from .clock import SystemClock
from .scheduler import schedulers

# cada posicao da lista de um struct que armazena as informacoes de cada tick
class Simulator():
    def __init__(self, scheduler, quantum, tasks_list):
        self.clock = SystemClock()
        
        # mover para a interface 
        valid_scheduler = schedulers.get(scheduler)                          # verifica que o scheduler esta no dicionario
        if not valid_scheduler:
            raise ValueError(f"Escalonador '{scheduler}' inválido")
        self.scheduler = valid_scheduler()

        self._quantum = quantum
        self._quantum_tick = 0

        self.tasks_list = tasks_list
        
        self.current_task = None            # apenas uma tarefa pode estar no estado RUNNING
        self.ready_tasks = []         
        
    def check_new_tasks(self):
        for task in self.tasks_list:
            if task.start == self.clock.current_time and task._state == TaskState.NEW:
                task.set_ready()
                self.ready_tasks.append(task)
   
    def increment_waiting_time(self):
        for task in self.ready_tasks:
            task._waiting_time += 1

    def select_task(self):        
        return self.scheduler.select_next_task(self.ready_tasks, self.current_task)
    
    def existing_tasks(self):
        for task in self.tasks_list:
            if task._state != TaskState.TERMINATED:
                return True
        return False 
    
    def is_running(self):
        if self.current_task == None:
            return False
        return True
    
    def is_terminated(self):
        if self.current_task._remaining_time == 0:
            return True
        return False
    
    def tick(self):
        self.increment_waiting_time()
        self.check_new_tasks()

        if not self.is_running():
            if self.ready_tasks:
                chosen_task = self.select_task()
                self.ready_tasks.remove(chosen_task)    # PRONTA -> EXECUTANDO
                self.current_task = chosen_task
                self.current_task.set_running()

                self._quantum_tick = 0

        else:
            chosen_task = self.select_task()
            if chosen_task != self.current_task:
                self.current_task.set_ready()
                self.ready_tasks.append(self.current_task)

                self.current_task = chosen_task             # a outra tarefa recebe o processamento
                self.ready_tasks.remove(self.current_task)
                self.current_task.set_running()
                self._quantum_tick = 0                 

            elif self._quantum_tick == self._quantum:
                self.current_task.set_ready()                   # muda seu estado para pronto e adiciona de volta para lista de prontos
                self.ready_tasks.append(self.current_task)
                
                self.current_task = None
                chosen_task = self.select_task()                # seleciona a proxima tarefa
                self.current_task = chosen_task
                self.ready_tasks.remove(self.current_task)
                self.current_task.set_running()
                
                self._quantum_tick = 0    

        if self.is_running():
            self.current_task._remaining_time -= 1
            self._quantum_tick += 1

            if self.is_terminated():
                self.current_task.set_terminated()
                self.current_task._life_time = (self.clock.current_time + 1) - self.current_task.start
                self.current_task = None
                self._quantum_tick = 0
                
        self.clock.tick()                                       # avança o tick
    

    def complete_simulation(self):
        while(self.existing_tasks()):
            self.tick()

