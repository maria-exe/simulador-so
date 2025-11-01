from .enums import TaskState
from .clock import SystemClock
from .scheduler import schedulers

# cada posicao da lista de um struct que armazena as informacoes de cada tick
class Simulator():
    def __init__(self, scheduler, quantum, tasks_list):
        self.clock = SystemClock()
        
        valid_scheduler = schedulers.get(scheduler)                          # verifica que o scheduler esta no dicionario
        if not valid_scheduler:
            raise ValueError(f"Escalonador '{scheduler}' inválido")
        self.scheduler = valid_scheduler()

        self._quantum = quantum
        self._quantum_tick = 0

        self.tasks_list = tasks_list
        
        self._current_task = None            # apenas uma tarefa pode estar no estado RUNNING
        self.ready_tasks = []         
        
    def tasks(self):
        for task in self.tasks_list:
           print(str(task))

    def add_ready_tasks(self):
        for task in self.tasks_list:
            if task.start == self.clock.current_time and task._state == TaskState.NEW:
                task._state = TaskState.READY
                self.ready_tasks.append(task)
                print(task)
   
    def increment_waiting_time(self):
        for task in self.ready_tasks:
            task._waiting_time += 1

    def select_task(self):
        if not self.ready_tasks:
            return None
        
        return self.scheduler.select_next_task(self.ready_tasks)
    
    def existing_tasks(self):
        for task in self.tasks_list:
            if task._state != TaskState.TERMINATED:
                return True
        return False 
    
    # Método para execução passo a passo
    def step(self):

        self.increment_waiting_time()   # Incrementa tempo de espera das tarefas prontas
        self.add_ready_tasks()

        if self._current_task is not None:                  # CPU/ocupada
            self._current_task._remaining_time -= 1
            self._quantum_tick += 1
            
            if self._current_task._remaining_time == 0:             # verifica se a tarefa terminou 
                self._current_task._state = TaskState.TERMINATED 
                self._current_task = None
                self._quantum_tick = 0                         # reseta quantum

            elif self._quantum_tick == self._quantum:          # esgotou o quantum
                new_task = self.select_task()
                self._current_task._state = TaskState.READY
                self.ready_tasks.append(self._current_task)
                
                self.ready_tasks.remove(new_task)
                
                self._current_task = new_task
                self._current_task._state = TaskState.RUNNING
                
                self._quantum_tick = 0

            else: 
                new_task = self.select_task()
                if new_task is not None and new_task != self._current_task:  # verifica se a tarefa escolhida pelo escalonador e diferente da executando                                         
                    self._current_task._state = TaskState.READY   # muda seu estado  
                    self.ready_tasks.append(self._current_task)   # EXEC. -> PRONTA -- preempta a tarefa 
                    self.ready_tasks.remove(new_task)            # remove a nova da lista de prontos -- PRONTA -> EXEC.

                    self._current_task = new_task                # nova ocupa a CPU do sistema
                    self._current_task._state = TaskState.RUNNING
                    self._quantum_tick = 0
        
        elif self._current_task is None and self.ready_tasks:
            
            new_task = self.select_task()
            
            self.ready_tasks.remove(new_task)                   # PRONTA -> EXECUTANDO
            self._current_task = new_task
            self._current_task._state = TaskState.RUNNING
            self._quantum_tick = 0                               # reseta o quantum 

        self.clock.tick()
    

    def complete_simulation(self):
        while(self.existing_tasks()):
            self.step()

    # return simulation_data
    # Método para execução completa
    
    # TA - running -- acabou o tempinho dela -- sisteminha vai olhar e tentar e preemptar --- se tiver outra prio maior ela preempt
    # se nao continua com ela --- quantum ainda acontece com base na regra do escalonador