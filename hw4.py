import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from scipy import stats
import itertools
import os


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
    fig.show()


def question_2():
    x = np.log10(df['k'])
    y = np.log10(df['ccdf'])

    x_cleaned = x[~np.isnan(y)]
    y_cleaned = y[~np.isnan(y)]

    xrange_one = x_cleaned[x_cleaned < 7]
    yrange_one = y_cleaned[x_cleaned < 7]

    model = stats.linregress(xrange_one, yrange_one)
    print('ccdf')
    z = 1.96
    ci = (model.slope - (z * model.stderr), model.slope + (z * model.stderr))
    print(ci)


    xrange_two = x_cleaned[(x_cleaned > 7.5) & (x_cleaned < 10)]
    yrange_two = y_cleaned[(x_cleaned > 7.5) & (x_cleaned < 10)]

    model = stats.linregress(xrange_two, yrange_two)

    z = 1.96
    ci = (model.slope - (z * model.stderr), model.slope + (z * model.stderr))
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
    # fig.show()
    # fig.write_image('test.png', format='png')


def question_4():
    raw_df = pd.read_csv('rawwordfreqs.txt', names=['count'])
    raw_df['sorted'] = raw_df['count'].sort_values(ascending=False)
    raw_df['index'] = [i + 1 for i in range(len(raw_df))]

    x = np.log10(raw_df['index'])
    y = np.log10(raw_df['sorted'])

    x_cleaned = x[~np.isnan(x)]
    y_cleaned = y[~np.isnan(x)]

    xrange_one = x_cleaned[y_cleaned < 7.5]
    yrange_one = y_cleaned[y_cleaned < 7.5]

    model = stats.linregress(xrange_one, yrange_one)

    print('zipfs')
    z = 1.96
    ci = (model.slope - (z * model.stderr), model.slope + (z * model.stderr))
    print(ci)


    xrange_two = x_cleaned[(y_cleaned > 7.5) & (y_cleaned < 10)]
    yrange_two = y_cleaned[(y_cleaned > 7.5) & (y_cleaned < 10)]

    model = stats.linregress(xrange_two, yrange_two)

    z = 1.96
    ci = (model.slope - (z * model.stderr), model.slope + (z * model.stderr))
    print(ci)


def question_5():


    def alpha_from_gamma(gamma: float):
        return 1/(gamma - 1)

    def gamma_from_alpha(alpha: float):
        return 1 + (1/alpha)

    # get gamma from slope
    ccdf1 = -0.66
    ccdf2 = -1.11
    gamma_1 = -ccdf1 + 1
    gamma_2 = -ccdf2 + 1

    alpha_1 = 1.42
    alpha_2 = 0.911

    print('slope 1')
    print(f'gamma: {gamma_1}, calculated alpha: {alpha_from_gamma(gamma_1):.3f}')
    print(f'alpha: {alpha_1}, calculated gamma: {gamma_from_alpha(alpha_1):.3f}')
    print(gamma_1, alpha_1)
    print('slope 2')
    print(f'gamma: {gamma_2}, calculated alpha: {alpha_from_gamma(gamma_2):.3f}')
    print(f'alpha: {alpha_2}, calculated gamma: {gamma_from_alpha(alpha_2):.3f}')


def question_6():
    babygirls_1952 = pd.read_csv(os.path.join('data', 'names-girls1952.txt'), names=['name', 'gender', 'count'])
    babyboys_1952 = pd.read_csv(os.path.join('data', 'names-boys1952.txt'), names=['name', 'gender', 'count'])
    babygirls_2002 = pd.read_csv(os.path.join('data', 'names-girls2002.txt'), names=['name', 'gender', 'count'])
    babyboys_2002 = pd.read_csv(os.path.join('data', 'names-boys2002.txt'), names=['name', 'gender', 'count'])

    to_process = [babygirls_1952, babyboys_1952, babygirls_2002, babyboys_2002]
    titles = ['babygirls_1952', 'babyboys_1952', 'babygirls_2002', 'babyboys_2002']

    for i, df in enumerate(to_process):
        # ccdf
        data = df['count'].value_counts().to_frame()
        k = np.asarray(data.index.values)
        n_sub_k = np.asarray(data['count'].values)
        out = pd.DataFrame()
        out['k'] = k
        out['pdf'] = n_sub_k / n_sub_k.sum()
        out['cdf'] = out['pdf'].sort_values()[::-1].cumsum()
        out['ccdf'] = np.ones(len(out['cdf'])) - out['cdf']

        # zipfs
        zipf = pd.DataFrame()
        zipf['y'] = df['count'].sort_values(ascending=False).to_numpy()
        zipf['x'] = np.asarray([i + 1 for i in range(len(df))])

        filtered_ccdf = out[np.log10(out['k']) < 2]
        regr = stats.linregress(np.log10(filtered_ccdf['k']), np.log10(filtered_ccdf['ccdf']))
        gamma = -regr.slope + 1

        filtered_zipf = zipf[np.log10(zipf['x']) > 2]
        regr = stats.linregress(np.log10(filtered_zipf['x']), np.log10(filtered_zipf['y']))
        alpha = -regr.slope


        fig = make_subplots(rows=1, cols=2,
                            subplot_titles=(f'CCDF {titles[i]}, gamma: {gamma:.3f}', f'Zipfs {titles[i]}, alpha: {alpha:.3f}'),
                            specs=[[{"type": "scatter"}, {"type": "scatter"}]],
                            shared_yaxes=False)

        fig.add_trace(go.Scatter(x=np.log10(out['k']), y=np.log10(out['ccdf']), name='CCDF', mode='markers'), row=1, col=1)
        fig.add_trace(go.Scatter(x=np.log10(zipf['x']), y=np.log10(zipf['y']), name='Zipfs', mode='markers'), row=1, col=2)

        fig.show()


if __name__ == '__main__':
    # question_1()
    # question_2()
    # question_3()
    # question_4()
    # question_5()
    question_6()
