import pandas as pd
import csv
from datetime import time, date, datetime
import functions
import help
import time

###################################### CHECKING TO MAKE SURE THEY HAVE FILES AND STUFF IN THEM ##################################

# Checking to make sure they have the correct files in this directory
functions.file_checking()
# Making sure they have data in their files. Won't work without it.
functions.first_data()
########################################## READING HISTORICAL DATA ##############################################################

historical_records = pd.read_csv('records.csv', parse_dates = True, infer_datetime_format = True)
historical_records = historical_records.sort_values('Date', ascending = True)
# historical_records['Date'] = pd.to_datetime(historical_records['Date']).dt.date
############################################### THE GAME!!! #####################################################################

while True:
    try:
        functions.clear_terminal()
        print("""
    ----------------------------------------------------------------------
    Enter in a record formatted like: Python 01/01/21 1.5 \n
    Or Type in a number below.

    (1) Time Calculator: If you know when, but not how many hours you studied
    (2) Stopwatch: A built in stopwatch to track time studied
    (3) A list of all things tracked
    (4) The last 5 Entries
    (5) For Stats and Charts
    (6) Backup Data
    (7) Help
    (9) To exit the program

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
            functions.time_calculator_save_decisions(first_input, historical_records)
        elif '2' in first_input[0]:
            functions.tracker_save_decisions(first_input, historical_records)
        elif '3' in first_input:
            print(f'Subjects Tracked: {historical_records.Subject.unique()}')
            cont = input('Press "Enter" to continue: ')
        elif '4' in first_input:
            functions.clear_terminal()
            print(f'The following are your last 5 entries: \n {historical_records[-5:]}')
            cont = input('Press "Enter" to continue: ')
        elif '5' in first_input:
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
            # Here we are going to start saving to the database
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
        elif '6' in first_input:
            functions.clear_terminal()
            print('These are the last ten records. If they look correct, then backup is safe.\n\n')
            functions.backup(historical_records)
        elif '7' in first_input:
            help.help()
    except KeyboardInterrupt:
        print('\n\nYou have stopped the program with ^C')
        print('You can also stop the program by by typing "9"')
        break