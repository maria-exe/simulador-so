# main_rr.py
from scr.simulator import Simulator
from scr.task import TaskControlBlock

def main(): 
    print("Iniciando simulação com escalonador Round Robin...")

    # --- Definição das Tarefas para o Teste ---
    # Prioridade (prio) é irrelevante para RR
    tarefas_teste = [
        {"t_id": "T1", "start": 0, "duration": 7, "prio": 0},
        {"t_id": "T2", "start": 2, "duration": 4, "prio": 0},
        {"t_id": "T3", "start": 4, "duration": 2, "prio": 0}
    ]

    # --- Preparação ---
    tasks_list = []
    for task_data in tarefas_teste:
        tasks_list.append(
            TaskControlBlock(
                t_id=task_data["t_id"],
                color=1, # Cor é irrelevante para este teste
                start=task_data["start"],
                duration=task_data["duration"],
                prio=task_data["prio"]
            )
        )

    # Configurações do simulador
    scheduler = "RR"
    quantum = 3  # Definindo um quantum de 3 ticks
    
    # --- Execução ---
    simulador = Simulator(scheduler, quantum, tasks_list)
    simulador.complete_simulation()

    # --- Coleta e Exibição dos Resultados ---
    total_wait = 0
    total_life = 0
    num_tasks = len(tasks_list)

    print("\n--- Resultados Finais ---")
    print(f"{'ID':<5} | {'Espera':<7} | {'T. Vida':<8}")
    print("-" * 24)

    for task in tasks_list:
        print(f"{task.id:<5} | {task._waiting_time:<7} | {task._life_time:<8}")
        total_wait += task._waiting_time
        total_life += task._life_time

    print("-" * 24)
    if num_tasks > 0:
        print(f"Tempo Médio de Espera: {total_wait / num_tasks:.2f}")
        print(f"Tempo Médio de Vida (Turnaround): {total_life / num_tasks:.2f}")
    else:
        print("Nenhuma tarefa foi executada.")


if __name__ == "__main__":
    main()