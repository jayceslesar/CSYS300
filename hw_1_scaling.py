import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from scipy import stats
import copy

# 1
def one():

    powerlifting = pd.read_csv('hw_1_scaling.csv')

    powerlifting['total_log'] = np.log10(powerlifting['total'])
    powerlifting['body_mass_log'] = np.log10(powerlifting['body_mass'])
    powerlifting['clean_and_jerk_log'] = np.log10(powerlifting['clean_and_jerk'])
    powerlifting['snatch_log'] = np.log10(powerlifting['snatch'])
    powerlifting['scaled'] = powerlifting['body_mass_log']**(3/8)


    powerlifting_m = copy.deepcopy(powerlifting[powerlifting['sex'] == 'm'])
    # x is always body mass
    snatch_m = stats.linregress(powerlifting_m['scaled'], powerlifting_m['snatch_log'])

    clean_and_jerk_m = stats.linregress(powerlifting_m['scaled'], powerlifting_m['clean_and_jerk_log'])
    total_m = stats.linregress(powerlifting_m['scaled'], powerlifting_m['total_log'])

    fig = go.Figure()
    fig.update_layout(template='plotly')
    fig.add_trace(go.Scatter(x=powerlifting_m['body_mass_log'], y=powerlifting_m['snatch_log'], mode='lines', name='snatch m'))
    fig.add_trace(go.Scatter(x=powerlifting_m['body_mass_log'], y=powerlifting_m['clean_and_jerk_log'], mode='lines', name='clean and jerk m'))
    fig.add_trace(go.Scatter(x=powerlifting_m['body_mass_log'], y=powerlifting_m['total_log'], mode='lines', name='snatch m'))

    powerlifting_f = powerlifting[powerlifting['sex'] == 'f']
    # x is always body mass
    snatch_f = stats.linregress(powerlifting_f['scaled'], powerlifting_f['snatch_log'])
    clean_and_jerk_f = stats.linregress(powerlifting_f['scaled'], powerlifting_f['clean_and_jerk_log'])
    total_f = stats.linregress(powerlifting_f['scaled'], powerlifting_f['total_log'])

    fig.add_trace(go.Scatter(x=powerlifting_f['body_mass_log'], y=powerlifting_m['snatch_log'], mode='lines', name='snatch f'))
    fig.add_trace(go.Scatter(x=powerlifting_f['body_mass_log'], y=powerlifting_m['clean_and_jerk_log'], mode='lines', name='clean and jerk f'))
    fig.add_trace(go.Scatter(x=powerlifting_f['body_mass_log'], y=powerlifting_m['total_log'], mode='lines', name='snatch f'))
    fig.update_layout(font_size=14, title=f"Current World Record Powerlifting Slopes for Events Snatch, Clean and Jerk, and Total")
    fig.update_xaxes(title='Log10 Body Mass (kg)')
    fig.update_yaxes(title='Log10 weight (kg)')
    fig.show()



    # a

    scaled_regression = stats.linregress(powerlifting_m['scaled'], powerlifting_m['total'])

    # show differences in R^2 for total, snatch, clean and jerk vs body mass that is scaled and unscaled across men and women

    normalized_snatch = []
    normalized_clean_and_jerk = []
    normalized_total = []
    for index, row in powerlifting_m.iterrows():
        weight_class = row['scaled']

        worldrecord_snatch = row['snatch_log']
        c_snatch = snatch_m.slope
        b_snatch = snatch_m.intercept
        scaled_snatch = 100 * ((worldrecord_snatch / (b_snatch*(weight_class**c_snatch))) - 1)
        normalized_snatch.append(scaled_snatch)

        worldrecord_clean_and_jerk = row['clean_and_jerk_log']
        c_clean_and_jerk = clean_and_jerk_m.slope
        b_clean_and_jerk = clean_and_jerk_m.intercept
        scaled_clean_and_jerk = 100 * ((worldrecord_clean_and_jerk / (b_clean_and_jerk*(weight_class**c_clean_and_jerk))) - 1)
        normalized_clean_and_jerk.append(scaled_clean_and_jerk)

        worldrecord_total = row['total_log']
        c_total = total_m.slope
        b_total = total_m.intercept
        scaled_total = 100 * ((worldrecord_total / (b_total*(weight_class**c_total))) - 1)
        normalized_total.append(scaled_total)

    for index, row in powerlifting_f.iterrows():
        weight_class = row['scaled']

        worldrecord_snatch = row['snatch_log']
        c_snatch = snatch_f.slope
        b_snatch = snatch_f.intercept
        scaled_snatch = 100 * ((worldrecord_snatch / (b_snatch*(weight_class**c_snatch))) - 1)
        normalized_snatch.append(scaled_snatch)

        worldrecord_clean_and_jerk = row['clean_and_jerk_log']
        c_clean_and_jerk = clean_and_jerk_f.slope
        b_clean_and_jerk = clean_and_jerk_f.intercept
        scaled_clean_and_jerk = 100 * ((worldrecord_clean_and_jerk / (b_clean_and_jerk*(weight_class**c_clean_and_jerk))) - 1)
        normalized_clean_and_jerk.append(scaled_clean_and_jerk)

        worldrecord_total = row['total_log']
        c_total = total_f.slope
        b_total = total_f.intercept
        scaled_total = 100 * ((worldrecord_total / (b_total*(weight_class**c_total))) - 1)
        normalized_total.append(scaled_total)

    powerlifting['noramlized_snatch'] = normalized_snatch
    powerlifting['normalized_clean_and_jerk'] = normalized_clean_and_jerk
    powerlifting['normalized_total'] = normalized_total

    # compare R^2, for 2/3
    # highlight max
    test = copy.deepcopy(powerlifting[powerlifting['sex'] == 'f'])
    snatch_test = stats.linregress(test['body_mass_log'], test['snatch_log'])

    clean_and_jerk_test = stats.linregress(test['body_mass_log'], test['clean_and_jerk_log'])
    total_test = stats.linregress(test['body_mass_log'], test['total_log'])

    regrs = [snatch_test, clean_and_jerk_test, total_test]

    for regr in regrs:
        print(f'{round(regr.slope, 3)}, {round(regr.intercept, 3)}, {regr.rvalue**2}')

    out = powerlifting.round(3)
    for index, row in out.iterrows():
        print(f"{row['noramlized_snatch']} & {row['normalized_clean_and_jerk']} & {row['normalized_total']}")
def two():
    pass

one()