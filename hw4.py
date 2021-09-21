import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from scipy import stats
import itertools


df = pd.read_csv('vocab_cs_mod.txt', delim_whitespace=True)
# number of words, amount of times words appeared


def question_1():
    df['pdf'] = df['n_sub_k'] / df['n_sub_k'].sum()
    df['cdf'] = df['pdf'][::-1].cumsum()
    df['ccdf'] = np.ones(len(df['cdf'])) - df['cdf']

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=np.log10(df['k']), y=np.log10(df['cdf']), name='CDF'))
    fig.add_trace(go.Scatter(x=np.log10(df['k']), y=np.log10(df['ccdf']), name='CCDF'))
    fig.update_layout(title='CDF/CCDF for Google Vocab Dataset')
    fig.update_xaxes(title='log k')
    fig.update_yaxes(title='log distribution function')
    # fig.show()



def question_2():
    x = np.log10(df['k'])
    y = np.log10(df['ccdf'])

    x_cleaned = x[~np.isnan(y)]
    y_cleaned = y[~np.isnan(y)]

    xrange_one = x_cleaned[x_cleaned < 7]
    yrange_one = y_cleaned[x_cleaned < 7]

    model = stats.linregress(xrange_one, yrange_one)

    t = 1.96
    ci = (model.slope - (t * model.stderr), model.slope + (t * model.stderr))
    print(ci)


    xrange_two = x_cleaned[(x_cleaned > 7.5) & (x_cleaned < 10)]
    yrange_two = y_cleaned[(x_cleaned > 7.5) & (x_cleaned < 10)]

    model = stats.linregress(xrange_two, yrange_two)

    t = 1.96
    ci = (model.slope - (t * model.stderr), model.slope + (t * model.stderr))
    print(ci)


def question_3():
    raw_df = pd.read_csv('rawwordfreqs.txt', names=['count'])
    raw_df['sorted'] = raw_df['count'].sort_values(ascending=False)
    raw_df['index'] = [i + 1 for i in range(len(raw_df))]

    # x axis
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=np.log10(raw_df['index']), y=np.log10(raw_df['sorted']), name='ZipfsF', mode='lines'))
    fig.update_layout(title='Zipfs Law')
    fig.update_xaxes(title='log occurence')
    fig.update_yaxes(title='log rank')
    fig.show()


def question_4():
    raw_df = pd.read_csv('rawwordfreqs.txt', names=['count'])
    raw_df['sorted'] = raw_df['count'].sort_values(ascending=False)
    raw_df['index'] = [i + 1 for i in range(len(raw_df))]

    x = np.log10(raw_df['index'])
    y = np.log10(raw_df['sorted'])

    x_cleaned = x[~np.isnan(x)]
    y_cleaned = y[~np.isnan(x)]

    xrange_one = x_cleaned[(x_cleaned > 7.5) & (x_cleaned < 10)]
    yrange_one = y_cleaned[(x_cleaned > 7.5) & (x_cleaned < 10)]

    model = stats.linregress(xrange_one, yrange_one)

    t = 1.96
    ci = (model.slope - (t * model.stderr), model.slope + (t * model.stderr))
    print(ci)


    xrange_two = x_cleaned[x_cleaned < 7.5]
    yrange_two = y_cleaned[x_cleaned < 7.5]

    model = stats.linregress(xrange_two, yrange_two)

    t = 1.96
    ci = (model.slope - (t * model.stderr), model.slope + (t * model.stderr))
    print(ci)

if __name__ == '__main__':
    question_1()
    question_2()
    # question_3()
    question_4()
