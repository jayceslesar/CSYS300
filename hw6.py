import numpy as np
from scipy import stats
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import collections


def question_two():

    def simons_model(steps, rho):
        population = np.zeros(steps)
        num_groups = 1
        population[0] = 1

        for i in range(steps - 1):
            if np.random.uniform(0,1) <= rho:
                num_groups += 1
                population[i + 1] = num_groups
            else:
                population[i + 1] = np.random.choice(population[0 : i + 1])

        return population

    rhos = [0.1, 0.01, 0.001]
    for rho in rhos:
        times = 10
        steps = 100000
        res = np.empty([times, steps])

        for i in range(times):
            res[i, :] = simons_model(steps, rho)

        # find counts of each group
        unique, counts = np.unique(res, return_counts=True)
        unique = unique.astype(int)
        counts = sorted(counts)[::-1]

        frequency = np.log10(counts)
        rank = np.log10([i + 1 for i in range(len(counts))])

        regr = stats.linregress(rank[1:], frequency[1:])
        beta = -regr.slope
        alpha = 1 - rho

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=rank, y=frequency, name='Zipf', mode='markers'))
        fig.add_trace(go.Scatter(x=rank, y=regr.intercept + rank*regr.slope, name='Regression Fit', mode='lines'))
        fig.update_xaxes(title='log rank')
        fig.update_yaxes(title='log frequency')
        fig.update_layout(title=f'Zipfian Distribution for Simon Model for {steps} steps and rho={rho}. alpha={alpha:.3f}, beta={beta:.3f}')
        fig.show()


def question_5():
    clean_text('helo')
    df = pd.read_csv('ulysses.txt', delimiter=': ', names=['word', 'count'])

    # 5b
    frac = len(df) / df['count'].sum()
    print(f'5b {frac:.3f}')
    # 0.119

    # 5c
    freq = collections.Counter(df['count'])
    n1 = freq[1] / sum(freq.values())
    n2 = freq[2] / sum(freq.values())
    n3 = freq[3] / sum(freq.values())
    print(f'{n1:.3f}  {n2:.3f}  {n3:.3f}')
    # 0.565  0.156  0.071


def clean_text(filename: str):
    with open(filename) as text:
        words = text.read()
        lower = words.lower()
        splits = lower.split()

    return words


def question_6():
    # a
    data = clean_text('pride.txt')
    print(len(data))


def main():
    question_5()


if __name__ == '__main__':
    main()
