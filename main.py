#! /usr/bin/python

import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import time, date, datetime
import seaborn as sns
import functions
import time
################################ READING HISTORICAL DATA ########################################################################

historical_records = pd.read_csv('record.csv', parse_dates=True, infer_datetime_format=True)
historical_records = historical_records.sort_values('Date', ascending = True)
proceed = 1

while proceed ==1:
#############################################################################################################
    functions.clear_terminal()
    print("""
----------------------------------------------------------------------
Enter in a record formatted like: Python 01/01/21 1.5 \n
Or Type in a number below.

(1) Time Calculator: If you know when, but not how many.
(2) A list of all things tracked.
(3) The last 5 Entries
(4) For Stats and Charts
(stop) To stop the program.

----------------------------------------------------------------------
    """)
    #! This shows you the last entry for each item.
    last_items_entered = historical_records.groupby('Subject').last()
    print(f'These are the last records entered by subject\n\n'
            f'{last_items_entered}\n\n')
    first_input = input('What would you like to do? ').lower().split()

    print('----------------------------------------------------------------------')
#############################################################################################################
    
    if '1' in first_input[0]:
        # Create a time calculator e.g. 15:36 - 12:36 = 3 Hours
        functions.time_calculator()
    elif '2' in first_input:
        print(f'Subjects Tracked: {historical_records.Subject.unique()}')
        cont = input('Press "Enter" to continue: ')
    elif '3' in first_input:
        functions.clear_terminal()
        print(f'The following are your last 5 entries: \n {historical_records[-5:]}')
        cont = input('Press "Enter" to continue: ')
    elif '4' in first_input:
            data_type = input('Would You like (1)Graphs, (2)Data, or (3)Both?: ')
            print('Not quite ready. Check back in a couple of days.')
            functions.clear_terminal()
            if '1' in data_type:
                #! A pie plot showing what you spend most of your time studying.
                functions.pie_hours_by_subject(historical_records)
                #! This shows you the total hours studied by subject for the last week (7 DAYS).
                functions.past_seven_days_graph(historical_records)
                #! A function that returns the 7-day rolling average of hours studied.
                functions.weekly_rolling_avg()

            elif '2' in data_type:
                #! Subject grouped by hours
                functions.hours_by_subject(historical_records)
                functions.past_seven_days(historical_records)


        #! Eventually, you are going to want to see the weekly change in total hours by subject.
        #* Figure out how to subtract 2 group by with .diff().
        #* Last 7 days grouped minus 8 to 14 days grouped.
        #! This week you studied Python for 5 more hours.
    elif len(first_input) == 3:
        # Here we are going to start tracking.
        subject = first_input[0]
        date = first_input[1]
        hours = first_input[2]
        new_record = [subject,date,hours]
        #! Add a way to automatically save data locally to a different file for backup
        if subject not in historical_records.Subject.unique():
            track = input(f'It looks like "{subject.title()} is new to our records. Would you like\n'
                          f'to start tracking it? (y/n): ').lower()
            if track == 'y':
                new_record = pd.DataFrame({'Subject': [subject], 'Date': [date], 'Hours': [hours]})
                historical_records = historical_records.append(new_record, ignore_index=True)

                historical_records.to_csv('record.csv', sep = ',', index = False)
        else:
            track = input(f'You are about to enter that you have studied [{subject.swapcase()}] for [{hours}] hours\n'
                          f'on [{date.swapcase()}]. Is this correct? (y/n): ').lower()
            if track == 'y':
                new_record = pd.DataFrame({'Subject': [subject], 'Date': [date], 'Hours': [hours]})
                historical_records = historical_records.append(new_record, ignore_index=True)

                historical_records.to_csv('record.csv', sep = ',', index = False)
    elif len(first_input) != 3: # This is the very last one!
        print('There should only be 4 entries: x x x x.')
    elif 'stop' in first_input:
        proceed -= 1

