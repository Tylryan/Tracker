# Make it to where the user can input hours and minutes
# and it automatically calculates the time.

import pandas as pd
import csv
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
import time
import functions
import datetime
import os

# Removing an entry 

historical_records = pd.read_csv('records.csv', parse_dates = True, infer_datetime_format = True)
historical_records = historical_records.sort_values('Date', ascending = True)
historical_records['Date'] = pd.to_datetime(historical_records['Date']).dt.date


