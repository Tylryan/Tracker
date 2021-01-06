# Make it to where the user can input hours and minutes
# and it automatically calculates the time.

import seaborn as sns
#python 1/25/25 1 25
#list[2] = hour

import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import time, date, datetime
historical_records = pd.read_csv('record.csv')


hours_by_subject = historical_records.groupby('Subject').Hours.sum()
hours_by_subject.plot(kind = 'bar', legend = True)

# hours_by_subject.plot(kind = 'bar', figsize = (20,10))
# historical_records =  historical_records.set_index('Date')