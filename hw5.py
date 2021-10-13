import itertools
import numpy as np
import plotly.graph_objs as go
import plotly.express as px


def question_two():

    n = 10
    k = 2
    n_str = ''.join([str(i) for i in range(n)])
    groups_str_pos = list(itertools.combinations(n_str*2, n + k))
    groups_str_neg = list(itertools.combinations(n_str*2, n - k))

    groups_pos_int = []
    for group in groups_str_pos:
        groups_pos_int += [[int(i) for i in group]]

    groups_neg_int = []
    for group in groups_str_neg:
        groups_neg_int += [[int(i) for i in group]]


    data_pos = [np.mean(list(group)).round(3) for group in groups_pos_int][::10]
    data_neg = [np.mean(list(group)) for group in groups_neg_int][::10]



    fig = px.histogram(data_pos)
    fig.show()

    fig = px.histogram(data_neg)
    fig.show()

    gauss = np.random.normal()


if __name__ == '__main__':
    question_two()
