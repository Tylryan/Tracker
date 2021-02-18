# Make it to where the user can input hours and minutes
# and it automatically calculates the time.

import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import time, date, datetime
import seaborn as sns
import functions
import datetime

historical_records = pd.read_csv('record.csv', parse_dates=True, infer_datetime_format=True)
historical_records = historical_records.sort_values('Date', ascending = True)

# This looks really good if you are just looking at it.
a = pd.DataFrame(historical_records.groupby(['Subject','Date']).Hours.sum())

# This is a really good idea.
last_30_days_by_subject = a[-30:]

# a.plot(kind = 'bar', figsize = (30,10))
# plt.show()


def past_seven_days(historical_records):
    indexed = historical_records.set_index('Date')
    unique_days = indexed.index.unique()
    seven_days_ago = unique_days[-7]
    seven_days_of_data = indexed[indexed.index >= seven_days_ago]
    grouped_seven = seven_days_of_data.groupby('Subject').Hours.sum()
    grouped_seven.columns = ['Hours Studied']
    print(f'----------------------------------------------------------------------'
        f'\n\nTotal Hours for the Last Seven Days.\n\n'
        f'{grouped_seven}\n\n'
        f'----------------------------------------------------------------------')
    enter = input('Press "Enter" to continue: ')

past_seven_days(historical_records)