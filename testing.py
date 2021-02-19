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

historical_records = pd.read_csv('record.csv', parse_dates=True, infer_datetime_format=True)
historical_records = historical_records.sort_values('Date', ascending = True)

# This looks really good if you are just looking at it.
# a = pd.DataFrame(historical_records.groupby(['Subject','Date']).Hours.sum())

#! Creating a built in stopwatch
first_input = input('something -> ').lower().split()
def stopwatch(historical_records):
    to_track = input('Insert the subject you would like to track and the current day. ').lower().split()
    subject = to_track[0]
    date = to_track[1]

    # Clear the terminal here
    print('This stopwatch returns values in terms of hours rounded to the hundredths\n\n'
    'For example, 10 minutes will return 0.17 hours')
    print('\n\n----------------------------------------------------------------------')
    start_input = input('Time will be started after you press "Enter". ')
    stopwatch_start = dt.datetime.now()
    print(f'\nRecording Time: {stopwatch_start}')
    print('----------------------------------------------------------------------')

    end_input = input('\nTime will be stopped after you press "Enter"')
    stopwatch_end = dt.datetime.now()

    studied = round((stopwatch_end - stopwatch_start).total_seconds() / 3600,2)
    print(f'\nRecording Ended: {stopwatch_end}\n')
    time.sleep(1.0)
    # Clear Terminal
    print('################################ && ##################################\n')
    print(f'You have studied for {studied} hours')
    print('\n################################ && ##################################\n\n\n')
    cont = input('Press Enter to continue ')

    hours = studied
    new_record = [subject,date,hours]
    return subject, date, hours, new_record

def stopwatch_save(first_input, historical_records):
    if len(first_input) == 2: # NOTE THIS ALLOWS YOU TO AUTOMATICALL GO TO TIME TRACKING WITHOUT PRESSING 2.
        subject, date, hours, new_record = stopwatch(historical_records)
    elif first_input[0] == '2':
        subject, date, hours, new_record = stopwatch(historical_records)
    elif len(first_input) == 3:
        subject = first_input[0]
        date = first_input[1]
        hours = first_input[2]
        new_record = [subject,date,hours]
    #! Add a way to automatically save data locally to a different file for backup
    if subject not in historical_records.Subject.unique():
        track = input(f'It looks like "{subject.upper()}" is new to our records. Would you like\n'
                        f'to start tracking it? (y/n): ').lower()
        if track == 'y':
            new_record = pd.DataFrame({'Subject': [subject], 'Date': [pd.Timestamp(date).date], 'Hours': [hours]})
            functions.save(new_record,historical_records)
            #This is the back up save. Can be recovered if original data is corrupted.
            functions.backup(historical_records)
        else:
            print(f'\n\n{subject.upper()} has NOT been added to the record books.')
            time.sleep(1.5)
    else:
        print('----------------------------------------------------------------------')
        track = input(f'You are about to enter that you have studied [{subject.swapcase()}] for [{hours}] hours\n'
                        f'on [{date}]. Is this correct? (y/n): ').lower()
        print('----------------------------------------------------------------------')
        if track == 'y':
            new_record = pd.DataFrame({'Subject': [subject], 'Date': [date], 'Hours': [hours]})
            functions.save(new_record, historical_records)
            # This print statement helps verify that nothing went wrong in the code.             
            functions.backup(historical_records)