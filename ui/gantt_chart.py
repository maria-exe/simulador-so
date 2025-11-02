import pandas as pd
import matplotlib.pyplot as plt
from .ui_aux import colors_chart

class GanttChart:
    def __init__(self, simulation, scheduler):
        self.simulation = simulation
        self.scheduler = scheduler

    def clean_data(self):
        df = pd.DataFrame(self.simulation.tick_data)    # transforma os dados salvos da simulacao em um DataFrame

        if df.empty:                                    
            return pd.DataFrame(columns=['id', 'state', 'block', 'start', 'end', 'duration'])

        df = df.sort_values(by=['id', 'tick'])
        df['block'] = ((df['id'] != df ['id'].shift()) | (df['state'] != df['state'].shift())).cumsum()

        gantt = df.groupby(['id', 'state', 'block']).agg (
            start = ('tick', 'min'),
            end   = ('tick', 'max')
        ).reset_index()

        gantt['duration'] = gantt['end'] - gantt['start'] + 1

        return gantt
    
    def create_chart(self):
        df = self.clean_data()

        if df.empty:
            print("Sem dados para a simulacao.")
            return

        ids = sorted(df['id'].unique())
  
        colors_task = {
            task.id: task.color
            for task in self.simulation.tasks_list
        }

        df['int_color'] = df['id'].map(colors_task)
        df['hex_color'] = df['int_color'].map(colors_chart)
        
        gray = '#d3d3d3'

        df['plot_color'] = df.apply(
            lambda row: row['hex_color'] 
            if row['state'] == 'running'
            else gray,
            axis=1
        )

        fig, ax = plt.subplots(figsize=(15, len(ids) * 0.5 + 2))

        ax.barh (
            y = df['id'],
            width = df['duration'],
            height = 0.6,
            left = df['start'],
            color = df['plot_color'], 
            edgecolor = 'black'
        )

        ax.set_xlabel("Tempo")
        ax.set_ylabel("Tarefas")
        ax.set_title(f"Escalonamento do {self.scheduler}")

        ax.set_yticks(ids)
        ax.set_yticklabels(ids)
        
        max_time = (df['start'] + df['duration']).max()
        ticks = range(int(max_time) + 1)
        
        ax.set_xticks(ticks)
        ax.set_xlim(0, max_time)

        ax.grid(axis='x', color='gray', linewidth=1, alpha=0.7)

        file = f"{self.scheduler}.png"
        print("Grafico salvo com sucesso!")
        plt.savefig(file)
        plt.close(fig)
       