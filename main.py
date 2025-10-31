from scr.config_reader import read_config, create_config
from scr.simulator import Simulator
from scr.task import TaskControlBlock, TaskState

def main(): 
    tarefas_de_teste = [
        {"t_id": "t01", "color": 1, "start": 0, "duration": 8, "prio": 3},
        {"t_id": "t02", "color": 2, "start": 2, "duration": 4, "prio": 1},
        {"t_id": "t03", "color": 3, "start": 4, "duration": 5, "prio": 2},
        {"t_id": "t04", "color": 4, "start": 6, "duration": 2, "prio": 10}
    ]
    
    arquivo = "config/fifo.txt"
    create_config(arquivo, "SRTF", 7, tarefas_de_teste)
    
    scheduler, quantum, tasks_list = read_config(arquivo)
    print(f"Escalonador: {scheduler}, Quantum: {quantum}")


    # for task in tasks_list:
    #     task._state = TaskState.SUSPENDED
        

    # for task in tasks_list:
    #     print(str(task))

    simulacao1 = Simulator(scheduler, quantum, tasks_list)
    simulacao1.tasks()
    #print(simulacao1.scheduler, simulacao1.quantum)
    #print(simulacao1.scheduler, simulacao1.quantum)

if __name__ == "__main__":
    main()

