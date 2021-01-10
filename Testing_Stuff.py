# Make it to where the user can input hours and minutes
# and it automatically calculates the time.

import seaborn as sns
#python 1/25/25 1 25
#list[2] = hour

import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import time, date, datetime
historical_records = pd.read_csv('record.csv', index_col=1, parse_dates = True, infer_datetime_format=True)

unique_days = historical_records.index.unique()

seven_days_ago = unique_days[-7]

seven_days_of_data = historical_records[historical_records.index >= seven_days_ago]

grouped_seven = seven_days_of_data.groupby('Subject').Hours.sum()


print(f'----------------------------------------------'
      f'\n\nTotal Hours for the Last Seven Days.\n\n'
      f'{grouped_seven}\n\n'
      f'---------------------------------------------')

grouped_seven.plot(kind = 'bar', legend = True, figsize = (20,10))
title = plt.title('Total Hours Logged By Subject For The Last Week')
ylabel = plt.ylabel('Hours Logged')
plt.show()

#! Eventually, you are going to want to see the weekly change in total hours by subject.
#! This week you studied Python for 5 more hours.