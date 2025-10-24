from .tcb import TaskControlBlock

def tasks_config(file):
    
    tasks_list = []

    with open(file, 'r', encoding='utf-8') as config_txt:

        # Lê a primeira linha do arq e separa por ; em uma lista
        f_line = config_txt.readline().strip('\n').split(';') 

        # Info do Escalonador e quantum
        scheduler = f_line[0]
        quantum = int(f_line[1])

        for line in config_txt:
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

    return scheduler, quantum, tasks_list
