# Make it to where the user can input hours and minutes
# and it automatically calculates the time.

import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import time, date, datetime
import seaborn as sns
# import functions
import datetime

historical_records = pd.read_csv('record.csv', parse_dates=True, infer_datetime_format=True)
historical_records = historical_records.sort_values('Date', ascending = True)

# This looks really good if you are just looking at it.
a = pd.DataFrame(historical_records.groupby(['Subject','Date']).Hours.sum())

# This is a really good idea.
last_30_days_by_subject = a[-30:]

# a.plot(kind = 'bar', figsize = (30,10))
# plt.show()


def hours_studied_per_day(historical_records):
    hr_grouped_by_subject = pd.DataFrame(historical_records.groupby('Subject').Hours.mean().round(2))
    hr_grouped_by_subject.columns = ['Hours Studied per Day']
    print(hr_grouped_by_subject)


hours_studied_per_day(historical_records)