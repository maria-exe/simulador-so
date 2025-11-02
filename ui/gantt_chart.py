import pandas as pd
import matplotlib.pyplot as plt
#from .ui_aux import colors

class GanttChart:
    def __init__(self, simulation, scheduler):
        self.simulation = simulation
        self.scheduler = scheduler

    def clean_data(self):
        df = pd.DataFrame(self.simulation.tick_data)

        df = df.sort_values(by=['id', 'tick'])

        df['block'] = ((df['id'] != df ['id'].shift()) | (df['state'] != df['state'].shift())).cumsum()
        
        df_gantt = df.groupby(['id', 'state', 'block']).agg (
            start = ('tick', 'min'),
            end = ('tick', 'max')
        ).reset_index()

        df_gantt['duration'] = df_gantt['end'] - df_gantt['start'] + 1
        df_gantt = df_gantt[df_gantt['state'] != 'empty']
        
        return df_gantt

    def create_chart(self):
        df = self.clean_data()
        ids = sorted(df['id'].unique())

        fig, ax = plt.subplots(figsize=(15, len(ids) * 0.5 + 2))

        ax.barh (
            y = df['id'],
            width = df['duration'],
            height = 0.6,
            left = df['start'],
            #color = colors.get(self.task.id),
            edgecolor = 'black'
        )

        ax.set_xlabel("Tempo")
        ax.set_ylabel("Tarefas")
        ax.set_title(f"Escalonamento do {self.scheduler}")

        ax.set_yticks(ids)
        ax.set_yticklabels(ids)
        
        if not df.empty:
            max_time = (df['start'] + df['duration']).max()
            ticks = range(int(max_time) + 1)
            
            ax.set_xticks(ticks)

            ax.set_xlim(0, max_time)

        ax.grid(axis='x', color='gray', linewidth=1, alpha=0.7)
  
        plt.show()