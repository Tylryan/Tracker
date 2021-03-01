import functions
import pandas as pd
import time
import datetime as dt
import testing
# Try no to make the functions print questions. Let the main control the flow

#Checking to make sure the user has the correct files in their directory.
functions.file_checking()
# Making sure the users has data in their files. Won't work without it.
while True:
    functions.first_data()
    # This is the main screen.
    historical_records = pd.read_csv('records.csv', parse_dates = True, index_col='Date')
    historical_records = historical_records.sort_values('Date', ascending = True)
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
    # This shows the last Items entered by subject.
    last_items_entered = historical_records.groupby('Subject').last() #! This might work now, but it probably won't work in the future
    print(f'These are the last records entered BY SUBJECT\n\n'
            f'{last_items_entered}\n\n')
    first_input = input('What would you like to do? ').lower().split()
    print('----------------------------------------------------------------------')
    # If 9 is pressed, then stop the program
    if '9' == first_input[0]:
        print('Application stopped')
        time.sleep(1.5)
        functions.clear_terminal()
        break
    elif len(first_input) == 3: #! You just have to make it actually save to a file.
        # I Separated this out like this for readability.
        subject = first_input[0]
        date = first_input[1]
        hours = first_input[2]

        new_record = pd.DataFrame(
            {
                'Subject': [subject], 
                'Date': [date], 
                'Hours': [hours]
            }
        )

        # Creating a new entry instance.
        new_entry = testing.Records(new_record,historical_records)
        # Checking if that new entry is currently recorded 
        # This will ask if they want it to be tracked.
        new_entry.is_your_subject_in_our_records(subject)
        print(f"{new_entry.currently_tracking_subject}" )

        # Checking to make sure the user actually wants to save.
        if new_entry.currently_tracking_subject == False:
            pass
        else:
            would_you_like_to_save = input('Would you like to save? [Y/n]')
            # This will actually save the data
            new_entry.do_you_want_to_save_hm(would_you_like_to_save)
            print(f"{new_entry.do_you_want_to_save}")
            
            # print(f'{last_items_entered}')

            would_you_like_to_backup = input('Would you like to backup?')
            # This will actually backup the data
            new_entry.do_you_want_to_backup_hm(would_you_like_to_backup)
            print(new_entry.do_you_want_to_backup)
            input('Break')

    