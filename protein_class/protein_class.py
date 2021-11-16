
import numpy as np
import plotly
import plotly.graph_objs as go
from collections import deque
import pandas as pd
import plotly.express as px

aa_df = pd.read_csv("/Users/anafink/OneDrive - bwedu/Bachelor MoBi/5. Fachsemester/Python Praktikum/advanced_python_2021-22_HD/data/amino_acid_properties.csv")

metrics = {}
hydropathy_aa = {}
pI_aa = {}
hp_type_aa = {}
hydropathy_aa = aa_df.groupby('1-letter code')['hydropathy index (Kyte-Doolittle method)'].apply(float).to_dict()
pI_aa = aa_df.groupby('1-letter code')['pI'].apply(float).to_dict()
metrics = {
    "hydropathy" : hydropathy_aa,
    "pI" : pI_aa,
}


class Protein:

    def __init__(self, name, id, sequence):
        self.name = name
        self.id = id
        self.sequence = sequence
        

    def define_metrics(self, metric_aa = "hydropathy"):
        metric_values = []
        for pos, aa in enumerate(self.sequence):
            metric_values.append(metrics[metric_aa][aa])
        return metric_values

    def get_aa_pos(self):
        aa_pos = []
        aa_pos = list(range(1,len(self.sequence)+1))
        return aa_pos

    def get_y_values(self, metric_aa = "hydropathy", window_size = 5 ):

        metric_values = self.define_metrics(metric_aa)
        window = deque([], maxlen = window_size)

        mean_values = []

        for value in metric_values:
            window.append(value)
            mean_values.append(np.mean(window))

        return mean_values
        
    def plot(self, metric="hydropathy", window_size = 5):
        
        x_values = self.get_aa_pos()
        y_values = self.get_y_values(metric, window_size)    
        
        data = [
            go.Bar(
                x = x_values, 
                y = y_values, 
            )
        ]
        
        fig = go.Figure(data=data)
        fig.update_layout(template="plotly_white", title="Protein: " + self.name)
        return fig
