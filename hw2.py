import numpy as np
import pandas as pd
from scipy import stats
import plotly.graph_objs as go
import plotly.express as px


df = pd.read_csv('planets.csv')

t = df['p']
r = df['r']

fig = go.Figure()
fig.update_layout(template='plotly')
fig.add_trace(go.Scatter(x=np.log10(t), y=np.log10(r), mode='lines'))
fig.update_layout(font_size=14, title=f"log period vs log radius for planets in solar system")
fig.update_xaxes(title='Log10 period (T)')
fig.update_yaxes(title='Log10 radius (r)')
fig.show()

regress = stats.linregress(np.log10(r), np.log10(t))
print(regress.slope)