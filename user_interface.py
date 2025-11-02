# teste de uma possivel interacao com o usuario
import os, sys
from scr.config_reader import read_config, create_config
from scr.simulator import Simulator
from scr.enums import Scheduler



class SystemInterface:
    def __init__(self):
        self.default_file = "config/priop.txt"

    def clear_terminal():
        os.system('clear')

    def edit_task_aux(self):
        try:
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

    def create_tasks(self):
        # clean terminal dps
        try:
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
            
            print("\n -- Configuracao de tarefas -- \n")
            created_tasks = []
            
            is_adding = True
            while(is_adding):
                print("\n-- Quer criar adicionar uma nova tarefa? (1. Sim, 2. Não) --\n")
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
        
    def main_menu(self):
        try: 
            print("--- SimuladorOS ---\n")
            print("Digite o numero da opcao desejada:\n" \
            "      1. INICIAR\n" \
            "      2. CARREGAR\n" \
            "      3. CONFIGURACAO\n" \
            "      4. MODO DE SIMULACAO\n"\
            "      5. SAIR\n")

            command = int(input("Digite: "))
            
            match command:
                case 1: 
                    # chamada funcao
                    pass
                case 2:
                    print("Digite o arquivo. Exemplo: 'SRTF.txt': ")
                    caminho = input()
                    read_config(caminho) # precisa arrumar os caminhos para serem absolutos no standalone
                    self.main_menu()
                case 3:
                    scheduler, quantum, tasks_list = self.create_tasks()
                    create_config(self.default_file, scheduler, quantum, tasks_list) # sobreescreve arquivo default com as config do usuario
                    self.main_menu()
                case 4:
                    # chama funcao
                    #
                    pass
                case 5:
                    sys.exit(0)
                case _:
                    raise ValueError

        except Exception as e:
            print(f"ERRO: {e}")
    

teste1 = SystemInterface()
SystemInterface.main_menu(teste1)


