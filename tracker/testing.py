# Make it to where the user can input hours and minutes
# and it automatically calculates the time.

import pandas as pd
import csv
from matplotlib_terminal import plt
import plotext 
import datetime as dt
import seaborn as sns
import time
import functions
import datetime
import os
from termgraph import termgraph as tg

#! Create a class for data
historical_records = pd.read_csv('records.csv', parse_dates = True, infer_datetime_format = True)
historical_records = historical_records.sort_values('Date', ascending = True)
historical_records['Date'] = pd.to_datetime(historical_records['Date']).dt.date
last_items_entered = historical_records.groupby('Subject').last().sort_values(by = 'Date') #! This might work now, but it probably won't work in the future

def weekly_rolling_avg_graph_terminal():
    historical_records = pd.read_csv('records.csv', parse_dates = True, index_col='Date')
    historical_records = historical_records.sort_values('Date', ascending = True)
    subjects = historical_records.Subject.unique()

    df = pd.DataFrame()

    # Creating a base
    mask = historical_records.Subject == 'python'
    python_records = historical_records[mask]['Hours']
    df['python'] = python_records

    for i in subjects:
        mask = historical_records.Subject == i
        subject_records = pd.DataFrame(historical_records[mask]['Hours'])
        subject_records.columns = [i]
        df[i] = subject_records

    df = df.fillna(0)
    df = df.rolling(window = 7).mean().dropna()

    df.plot()
    title = plt.title(
        'Total Hours Logged By Subject For The Last Week', 
        loc = 'left')
    # Naming the y label/axis
    ylabel = plt.ylabel('Hours Logged')
    # Displaying the chart to the user

    plt.show('braille')
weekly_rolling_avg_graph_terminal()