import os, sys, tty, termios
from scr.config_reader import read_config, create_config
from scr.simulator import Simulator
from scr.enums import Scheduler
from ui.ui_aux import colors, color_state

class SystemInterface:
    def __init__(self):
        
        self.default_file = "config/fifo.txt"                                        # configuracao padrao do sistema que pode ser sobreescrito pelo usuario
        self.scheduler, self.quantum, self.tasks = read_config(self.default_file)
        self.simulator1 = Simulator(self.scheduler, self.quantum, self.tasks)
        
        self.tasks_map = {}

    def user_click(self):                       # captura click do teclado
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try: 
            tty.setcbreak(fd)
            click = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        return click

    def clear_terminal(self):                   # limpa terminal
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def edit_task_aux(self):                    # metodo para receber as configuracoes das tarefas do usuario
        try:
            self.clear_terminal()
            id = input("Digite o id: ")
            
            print("Selecione uma cor: (0. Roxo, 1. Rosa, 2. Vermelho, 3. Laranja, 4. Amarelo, 5. Verde, 6. Ciano, 7. Azul)")
            valid_colors = [0, 1, 2, 3, 4, 5, 6, 7]
            color = int(input("Digite o valor correspondente: "))
            if color not in valid_colors:
                raise ValueError
            
            start = int(input("Digite o ingresso: "))
            if start < 0:
                raise ValueError
            
            duration = int(input("Digite a duracao: "))
            if duration <= 0: 
                raise ValueError
            
            prio  = int(input("Digite a prioridade: "))
            if prio < 0: 
                raise ValueError
            
            # Adiciona essas info em um dicionario temporario
            task = {
                "t_id": id, 
                "color": color,
                "start": start,
                "duration": duration,
                "prio": prio
            }
            return task
        
        except ValueError:
            print(f"ERRO: Entrada {ValueError} invalida.")
            return None

    def create_tasks(self):                     # metodo principal para parametrizacao do sistema do usuario
        try:
            self.clear_terminal()
            print("Escolha o escalonador entre as opcoes: (1. FCFS, 2. SRTF e 3. PRIOP)\n")
            
            valid_scheduler = [1, 2, 3]
            entry = int(input("Digite o valor correspondente: "))
            if entry not in valid_scheduler:
                raise ValueError(f"Entrada {entry} invalida.")
            
            sch_string = Scheduler(entry)   
            scheduler = sch_string.name
                
            quantum = int(input("Digite o valor do quantum: "))
            if quantum <= 0:
                raise ValueError(f"Entrada {quantum} invalida.")
            
            print("\n ----- Configuracao de tarefas ----- \n")
            created_tasks = []
            
            is_adding = True
            while(is_adding):
                print("\n--- Quer criar adicionar uma nova tarefa? (1. Sim, 2. Não) ---\n")
                command = int(input("Digite o valor correspondente: "))

                if command == 1:
                    task = self.edit_task_aux()
                    created_tasks.append(task)  
                elif command == 2:
                    is_adding = False
                    break
                else: 
                    raise ValueError(f"Entrada {command} invalida.")
        
        except Exception as e:
            print(f"ERRO: {e}")
            return None, 0, []
        return scheduler, quantum, created_tasks

    def by_step(self):
        current_tick = self.simulator1.clock.current_time 
        self.simulator1.tick()

        if not self.tasks_map:
            self.tasks_map = {task.id: task for task in self.simulator1.tasks_list}

        tick_history = self.simulator1.tick_data
        tick_data = {} 

        max_time = self.simulator1.clock.current_time 
        
        for task_id in self.tasks_map.keys():
            tick_data[task_id] = ['IDLE'] * max_time 
            
        for entry in tick_history:
            tick_time = entry['tick']
            task_id = entry['id']
            
            if task_id not in tick_data:
                continue

            state = entry['state'].upper()
            
            if state == 'RUNNING' or tick_data[task_id][tick_time] == 'IDLE':
                tick_data[task_id][tick_time] = state

        clean = "\033[H\033[J"
        reset = "\033[0m"
        print(clean, end="")

        display_ids = sorted(tick_data.keys(), reverse=True)
        
        if not display_ids: 
            print(f"\ntick:\t{current_tick}")
            return

        for task_id in display_ids:
            history = tick_data[task_id]
            task = self.tasks_map[task_id]
            column = f"{task.id}  | "

            for state in history: 
                color_code = "\033[40m"
                
                if state == 'RUNNING':
                    color_code = colors.get(task.color, "\033[47m") 
                
                elif state == 'READY' or state == 'SUSPENDED':
                    color_code = color_state.get(state, "\033[100m")

                column = column + f"{color_code}    {reset}" 
            
            print(column)
        
        padding = "      " 
        axis_x = padding

        for tick in range(max_time):
            axis_x = axis_x + f"{tick:<4}"
        
        print(axis_x)
        print(f"\nTick:\t{current_tick}")

        for task in self.simulator1.tasks_list:
            print(task)

    def by_step_simulation(self):
        while(self.simulator1.existing_tasks()):
            print("Clique espaço para avançar a simulação\n")
            click = self.user_click()
            if click == " " or click == "c":
                self.by_step()

    def complete_simulation(self):
        while(self.simulator1.existing_tasks()):
                self.by_step()

    # Metodo principal da classe, responsavel pelo interacao com o usuario no terminal
    def main_menu(self):
        try: 
            self.clear_terminal()
            print("--- SimuladorOS ---\n")
            print("Digite o numero da opcao desejada:\n" \
            "      1. INICIAR\n" \
            "      2. CARREGAR ARQUIVO\n" \
            "      3. CONFIGURACAO\n" \
            "      4. SAIR\n")

            command = int(input("Digite: "))
            
            match command:
                case 1: 
                    print("Selecione o modo de simulacao: (1. Passo-a-passo, 2. Completa)")
                    mode = int(input("Digite: "))
                    if mode == 1:
                       self.by_step_simulation()
                    elif mode == 2:
                        self.complete_simulation()

                    print("\nQuer salvar o resultado da simulacao como imagem? (1. Sim, 2. Não)")
                    mode = int(input("Digite: "))
                    if mode == 1:
                        # chama o matplot
                        pass
                    elif mode == 2:
                        print("Adeus!")
                        self.clear_terminal()
                        sys.exit(0)
                case 2:
                    print("Digite o arquivo. Exemplo: 'SRTF.txt': ")
                    caminho = input()
                    read_config(caminho) # precisa arrumar os caminhos para serem absolutos no standalone
                    self.main_menu()
                case 3:
                    self.scheduler, self.quantum, self.tasks_list = self.create_tasks()
                    create_config(self.default_file, self.scheduler, self.quantum, self.tasks_list) # sobreescreve arquivo default com as config do usuario
                    self.main_menu()
                case 4:
                    sys.exit(0)
                case _:
                    raise ValueError(f"Entrada invalida")

        except Exception as e:
            print(f"ERRO: {e}")
    

teste1 = SystemInterface()
SystemInterface.main_menu(teste1)


