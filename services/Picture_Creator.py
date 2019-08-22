from portfolio_analysis import *
import plotly.graph_objects as go
from plotly.offline import plot
import csv
from IPython.display import Image
import os
import io

starting_cash = 388139.78
sp_dates = []
sp_value = []
with open("MII/SP500.csv", 'r') as csv_file:
    first = True
    stocks_reader = csv.reader(csv_file)
    for row in stocks_reader:
        if first:
            first = False
            continue
        if datetime.strptime(row[0], '%Y-%m-%d') == datetime.strptime('2018-08-20', '%Y-%m-%d'):
            shares = starting_cash / float(row[4])
        if datetime.strptime(row[0], '%Y-%m-%d') >= datetime.strptime('2018-08-20', '%Y-%m-%d'):
            sp_dates.append(row[0])
            sp_value.append(float(row[4]) * shares)

fig = go.Figure()

dates, value = get_axis()
fig.add_trace(go.Scatter(x=dates, y=value,
                    mode='lines',
                    name='MII Portfolio'))

fig.add_trace(go.Scatter(x=sp_dates, y=sp_value,
                    mode='lines',
                    name='S&P 500'))


fig.write_image("fig1.png", width = 2800, height = 2000)