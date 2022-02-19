import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class metodos:
    def prepararDatos(): 
        data = pd.read_csv("datos.csv")
        #data = data.astype(str)
        return data