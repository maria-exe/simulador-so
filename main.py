from scr.config_reader import tasks_config, create_file
from scr.simulator import Simulator

def main(): 
    tarefas_de_teste = [
        {"t_id": "t01", "color": 1, "start": 0, "duration": 8, "prio": 3},
        {"t_id": "t02", "color": 2, "start": 2, "duration": 4, "prio": 1},
        {"t_id": "t03", "color": 3, "start": 4, "duration": 5, "prio": 2},
        {"t_id": "t04", "color": 4, "start": 5, "duration": 2, "prio": 4}
    ]
    
    arquivo = "teste.txt"
    create_file(arquivo, "SRFT", 7, tarefas_de_teste)
    
    scheduler, quantum, tasks_list = tasks_config(arquivo)
    print(f"Escalonador: {scheduler}, Quantum: {quantum}")

    for task in tasks_list:
        print(task.id, task.color, task.start, task.duration, task.prio)

    simulacao1 = Simulator(scheduler, quantum, tasks_list)
    print(simulacao1.scheduler, simulacao1.quantum)
    print(simulacao1.scheduler, simulacao1.quantum)

if __name__ == "__main__":
    main()

