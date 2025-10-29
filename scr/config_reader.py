from .task import TaskControlBlock

def tasks_config(file): # leitura de arquivos
    try:
        with open(file, 'r', encoding='utf-8') as config_file:
            tasks_list = []

            f_line = config_file.readline().strip('\n').split(';') 
            scheduler = f_line[0]
            quantum = int(f_line[1])
           
            for line in config_file:                # itera pelas linhas do arquivo
                line = line.strip().split(';')

                t_id = line[0]
                color = int(line[1])
                start = int(line[2])
                duration = int(line[3])
                prio = int(line[4])
                # events -- ver dps

                new_task = TaskControlBlock(
                t_id = t_id,
                color = color,
                start = start, 
                duration = duration, 
                prio = prio
                )   

                tasks_list.append(new_task)

    except FileNotFoundError:
        print(f"\nArquivo {file} não encontrado!\n")
        return None, 0, []
    
    return scheduler, quantum, tasks_list
            
def create_file(filepath, scheduler, quantum, temp_tasks_list):  # criacao de arquivos
    try: 
        with open(filepath, 'w', encoding='utf-8') as file:
            f_line = f"{scheduler};{quantum}\n"                      
            file.write(f_line)                          # escreve a primeira linha do arquivo

            for task in temp_tasks_list:                # escreve uma tarefa por linha no arquivo
                t_line = [
                    str(task["t_id"]), 
                    str(task["color"]), 
                    str(task["start"]), 
                    str(task["duration"]), 
                    str(task["prio"])  
                ]
                t_line = ";".join(t_line) + "\n"        # junta cada info da tarefa, separadas apenas por ; 
                file.write(t_line)                      # escreve a linha no arquivo

            print(f"\nArquivo '{filepath}' gerado.\n")
            return True
   
    except IOError:                                     # captura de erro de escirta
        print(f"\nErro de escrita no arquivo: {IOError}\n")
        return False