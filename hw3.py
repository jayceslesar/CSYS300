import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from scipy import stats
import itertools


df = pd.read_csv('vocab_cs_mod.txt', delim_whitespace=True)
# number of words, amount of times words appeared


def question_5():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['k'], y=df['n_sub_k']))
    fig.update_layout(title='Frequency Distribution of Google Vocab (Unique)')
    fig.update_xaxes(title='k (frequency)')
    fig.update_yaxes(title='N sub k (number of words that appeared k times)')
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.log10(df['k']), y=np.log10(df['n_sub_k'])))
    fig.update_layout(title='Log10 Frequency Distribution of Google Vocab (Unique)')
    fig.update_xaxes(title='Log10 k (frequency)')
    fig.update_yaxes(title='Log10 N sub k (number of words that appeared k times)')
    fig.show()


def question_6():
    # On the log log scale the scaling seems to be upheld from 2.3 to 4 (fanning is why)
    our_val = 4
    df_filtered = df[np.log10(df['k']) >= our_val]
    ols = stats.linregress(np.log10(df_filtered['k']), np.log10(df_filtered['n_sub_k']))
    print(ols.slope)
    # beta_hat = -0.3585

def question_7():
    mean = sum(df['k']*df['n_sub_k'])/sum(df['n_sub_k'])
    numer = sum((np.array(df['k'], dtype='object')**2)*df['n_sub_k'])
    stdv = np.sqrt(((numer/sum(df['n_sub_k'])) - mean**2))

    print(mean, stdv)

def question_8():
    girlgirl = go.Figure(data=go.Heatmap(
                   z=[[1, 2, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1]],
                   x=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                   y=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],

                   hoverongaps = False, showlegend=False))
    girlgirl.show()

    girlboy = go.Figure(data=go.Heatmap(
                   z=[[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],
                   x=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                   y=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],

                   hoverongaps = False, showlegend=False))
    girlboy.show()

    boygirl = go.Figure(data=go.Heatmap(
                   z=[[1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1]],
                   x=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                   y=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],

                   hoverongaps = False, showlegend=False))
    boygirl.show()

    boyboy = go.Figure(data=go.Heatmap(
                   z=[[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2]],
                   x=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'extra'],
                   y=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'extra'],

                   hoverongaps = False, showlegend=False))
    boyboy.show()


if __name__ == '__main__':
    question_8()

