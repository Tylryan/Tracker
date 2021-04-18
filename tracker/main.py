#! /bin/python
import functions
import help
import pandas as pd
from datetime import time, date, datetime
import time
import plotext
import matplotlib.pyplot as plt
###################################### CHECKING TO MAKE SURE THEY HAVE FILES AND STUFF IN THEM ##################################

# Checking to make sure they have the correct files in this directory
functions.file_checking()
# Making sure they have data in their files. Won't work without it.
functions.first_data()
############################################### #####################################################################

while True:
    ########################################## READING HISTORICAL DATA ##############################################################
    try:
        functions.clear_terminal()
        print("""
Enter in a record formatted like: Python 01/01/21 1.5 \n
Or Type in a number below.

(1) Stopwatch
(2) Time Calculator
(3) Tracked Subjects
(4) Last 5 Entries
(5) Stats and Charts
(6) Backup Save
(7) Remove Entry
(8) Help

**********************************************************************
(9) To exit the program
**********************************************************************
        """)
        #! This shows you the last entry for each item.
        historical_records = pd.read_csv(
            'records.csv', parse_dates=True, infer_datetime_format=True)
        historical_records = historical_records.sort_values(
            'Date', ascending=True)
        historical_records['Date'] = pd.to_datetime(
            historical_records['Date']).dt.date
        last_items_entered = historical_records.groupby('Subject').last().sort_values(
            by='Date')  # ! This might work now, but it probably won't work in the future
        print(f'These are the last records entered BY SUBJECT\n\n'
              f'{last_items_entered}\n\n')
        first_input = input('What would you like to do? ').lower().split()

        print('----------------------------------------------------------------------')
    #############################################################################################################
        if '9' == first_input[0]:
            print('Application stopped')
            time.sleep(1.5)
            functions.clear_terminal()
            break
        ########################################## DEFAULT INPUT #################################################
        elif len(first_input) == 3:

            # Here we are going to start saving to the database
            subject = first_input[0]
            date = first_input[1]
            hours = first_input[2]
            #! Add a way to automatically save data locally to a different file for backup
            if pd.to_datetime(date) > datetime.now():
                print('You have entered in a date that\'s in the future cheater ')
                cont = input('\n\nPress "Enter to try again ')
                functions.clear_terminal()
                pass
            else:
                if subject not in historical_records.Subject.unique():
                    track = input(f'It looks like "{subject.upper()}" is new to our records. Would you like\n'
                                  f'to start tracking it? [Y/n]: ').lower()
                    if track == 'n':
                        print(
                            f'\n\n{subject.upper()} has NOT been added to the record books.')
                        time.sleep(1.5)
                        break
                    else:
                        new_record = pd.DataFrame(

                            {'Subject': [subject],
                             'Date': [date],
                             'Hours': [hours]
                             }
                        )
                        print(
                            '----------------------------------------------------------------------')
                        try:  # This try and except allows incorrect values such as 12/29/39
                            functions.save(new_record, historical_records)
                            # This is the back up save. Can be recovered if original data is corrupted.
                            functions.backup(historical_records)
                        except TypeError and ValueError:
                            print('Something went wrong')
                            cont = input('Press "Enter" to continue ')

                else:
                    print(
                        '----------------------------------------------------------------------')
                    track = input(f'You are about to enter that you have studied [{subject.swapcase()}] for [{hours}] hours\n'
                                  f'on [{date}]. Is this correct? [Y/n]: ').lower()
                    print(
                        '----------------------------------------------------------------------')
                    if track == 'n':
                        pass
                    else:
                        new_record = pd.DataFrame(
                            {'Subject': [subject], 'Date': [date], 'Hours': [hours]})
                        functions.save(new_record, historical_records)
                        # This print statement helps verify that nothing went wrong in the code.
                        functions.backup(historical_records)

        #################################### HERE ARE ALL THE OPTIONS ##############################################
        elif '1' == first_input[0]:
            functions.tracker_save_decisions(first_input, historical_records)
        elif '2' == first_input[0]:
            # Create a time calculator e.g. 15:36 - 12:36 = 3 Hours
            functions.time_calculator_save_decisions(
                first_input, historical_records)
        elif '3' == first_input[0]:
            print(f'Subjects Tracked: {historical_records.Subject.unique()}')
            cont = input('Press "Enter" to continue: ')
        elif '4' == first_input[0]:
            functions.clear_terminal()
            print(
                f'The following are your last 5 entries: \n {historical_records[-5:]}')
            cont = input('Press "Enter" to continue: ')
        elif '5' == first_input[0]:
            data_type = input(
                'Would You like (1)Graphs, (2)Data, or (3)Both?: ').split()
            print('Not quite ready. Check back in a couple of days.')
            if len(data_type) > 1:
                print('Please try again...')
                cont = input('Press "Enter" to continue: ')
            elif '1' in data_type[0]:
                cont = input("\n\n(Enter) Regular, (1) Terminal: ")
                if '1' in cont:
                    from matplotlib_terminal import plt as pltt
                    functions.clear_terminal()
                    # functions.weekly_rolling_avg_graph_terminal()
                    cont = input('\n\nPress "Enter" to continue: ')
                    functions.past_seven_days_graph_terminal(
                        historical_records)
                    cont = input('\n\nPress "Enter" to continue: ')
                else:
                    functions.clear_terminal()
                    # These can be done with limited data
                    #! A pie plot showing what you spend most of your time studying.
                    functions.pie_hours_by_subject(historical_records)
                    # These must have at least seven days of data
                    try:
                        #! This shows you the total hours studied by subject for the last week (7 DAYS).
                        functions.past_seven_days_graph(historical_records)
                        #! A function that returns the 7-day rolling average of hours studied.
                        functions.weekly_rolling_avg_graph(historical_records)
                        cont = input('\n\nPress "Enter" to continue: ')
                    except IndexError:
                        time.sleep(0.5)
                        pass

            elif '2' in data_type[0]:

                try:
                    #! All data
                    functions.all_data(historical_records)
                except IndexError:
                    pass

            elif '3' in data_type[0]:
                # Graphs
                #! A pie plot showing what you spend most of your time studying.
                functions.pie_hours_by_subject(historical_records)
                #! This shows you the total hours studied by subject for the last week (7 DAYS).
                try:
                    functions.past_seven_days_graph(historical_records)
                    #! A function that returns the 7-day rolling average of hours studied.
                    functions.weekly_rolling_avg_graph(historical_records)
                except IndexError:
                    pass
                # Dataframes
                #! Total Hours Studied by Subject
                functions.hours_by_subject(historical_records)
                try:
                    #! Hours studied by subject over the past week.
                    functions.past_seven_days(historical_records)
                except IndexError:
                    pass
                #! Average hours studied per day by subject.
                functions.hours_studied_per_day(historical_records)
            else:
                print('Please try again...')
                cont = input('Press "Enter" to continue: ')

        elif '6' == first_input[0]:
            functions.clear_terminal()
            functions.backup(historical_records)
        elif '7' == first_input[0]:
            functions.remove(historical_records)

        elif '8' == first_input[0]:
            help.help()
        else:
            print('Please Try again...')
            cont = input('Press "Enter" to continue: ')
    except KeyboardInterrupt:
        print('\n\n*****************************************************')
        print('You have stopped the program with "^C"')
        print('\n*****************************************************')
        time.sleep(2)
        functions.clear_terminal()
        break
