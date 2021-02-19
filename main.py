import pandas as pd
import csv
from datetime import time, date, datetime
import functions
import time
################################ READING HISTORICAL DATA ########################################################################

historical_records = pd.read_csv('records.csv')
historical_records = historical_records.sort_values('Date', ascending = True)
historical_records['Date'] = pd.to_datetime(historical_records['Date']).dt.date

################################# THE GAME!!! ##############################################################
stop = False
while stop == False:
    functions.clear_terminal()
    print("""
----------------------------------------------------------------------
Enter in a record formatted like: Python 01/01/21 1.5 \n
Or Type in a number below.

(1) Time Calculator: If you know when, but not how many.
(2) A list of all things tracked.
(3) The last 5 Entries
(4) For Stats and Charts
(5) Backup Data
(9) To stop the program.

----------------------------------------------------------------------
    """)
    #! This shows you the last entry for each item.
    last_items_entered = historical_records.groupby('Subject').last()
    print(f'These are the last records entered by subject\n\n'
            f'{last_items_entered}\n\n')
    first_input = input('What would you like to do? ').lower().split()

    print('----------------------------------------------------------------------')
#############################################################################################################
    if '9' in first_input:
        print('Application stopped')
        time.sleep(1.5)
        break

    elif '1' in first_input[0]:
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
                functions.weekly_rolling_avg_graph(historical_records)

            elif '2' in data_type:
                #! Total Hours Studied by Subject
                functions.hours_by_subject(historical_records)

                #! Hours studied by subject over the past week.
                functions.past_seven_days(historical_records)
                #! Average hours studied per day by subject.
                functions.hours_studied_per_day(historical_records)

    elif len(first_input) == 3:
        # Here we are going to start tracking.
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
                break
            else:
                print(f'\n\n{subject.upper()} has NOT been added to the record books.')
                time.sleep(1.5)
                break
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
    elif '5' in first_input:
        functions.clear_terminal()
        print('These are the last ten records. If they look correct, then backup is safe.\n\n')
        functions.backup(historical_records)
    elif len(first_input) != 3: # This is the very last one!
        print('There should only be 4 entries: x x x x.')


