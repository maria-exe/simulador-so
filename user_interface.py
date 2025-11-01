from scr.simulator import Simulator
from scr.config_reader import read_config
from ui.gantt_chart import GanttChart

def system_simulation():

    #arquivo = input("Envie um arquivo de configuração. Ex: fifo.txt")
    arquivo = "/home/poplu/so-projeto/simulador-so/config/fifo.txt"
    scheduler, quantum, tasks_list = read_config(arquivo)

    simulacao1 = Simulator(scheduler, quantum, tasks_list)
    simulacao1.complete_simulation()

    total_wait = 0
    total_life = 0

    print("--- RESULTADO ---")
    for task in tasks_list:
        total_wait += task._waiting_time
        total_life += task._life_time

    total_task = len(tasks_list)
    print(f"Tempo medio de espera: {total_life/total_task:.2f}")
    print(f"Tempo medio de vida: {total_wait/total_task:.2f}")

    grafico = GanttChart(simulacao1, scheduler)
    grafico.create_chart()

system_simulation()