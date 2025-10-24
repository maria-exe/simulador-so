from src.config_reader import tasks_config
from src.tcb import TaskControlBlock 

def main():
    #Só testando :P
    arquivo = "config/fifo.txt"
  
    scheduler, quantum, tasks_list = tasks_config(arquivo)

    print(f"Escalonador: {scheduler}, Quantum: {quantum}")

    for task in tasks_list:
        print(task.id, task.color, task.start, task.duration, task.prio)

if __name__ == "__main__":
    main()


