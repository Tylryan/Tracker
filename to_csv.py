import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import time, date, datetime
import seaborn as sns

historical_records = pd.read_csv('record.csv', parse_dates=True, infer_datetime_format=True)
proceed = 1

while proceed ==1:

    print("""
    --------------------------------------------------------------------------
Enter in a record formatted like: Subject Date Hours Minutes \n
Or Type in a number below.

(1) Time Calculator: If you know when, but not how many.
(2) A list of all things tracked.
(3) The last 5 Entries
(4) For Stats and Charts
(stop) To stop the program.

    --------------------------------------------------------------------------
    """)
    first_input = input('What would you like to do? ').lower().split()
    print('---------------------------------------------------------------')
    if '1' in first_input[0]:
        # Create a time calculator e.g. 15:36 - 12:36 = 3 Hours
        print('Format = Hour Minute: NO COMMA OR ANYTHING')
        start_time = input('Start Hour/Minute: ').split()
        start_hour = int(start_time[0])
        start_minute = int(start_time[1])
        start = time(start_hour, start_minute)

        print('Format = Hour Minute: NO COMMA OR ANYTHING')
        end_time = input('End Hour/Minute: ').split()
        end_hour = int(end_time[0])
        end_minute = int(end_time[1])
        end = time(end_hour, end_minute)

        time_studied = datetime.combine(date.min, end) - datetime.combine(date.min, start)
        print(f'You have studied for {time_studied} hours.')
    elif '2' in first_input:
        print(f'Subjects Tracked: {historical_records.Subject.unique()}')
    elif '3' in first_input:
        print(f'The following are your last 5 entries: \n {historical_records[-5:]}')
    elif '4' in first_input:
        #PUT THINGS THAT REQUIRE DATE TO BE INDEX AT THE BOTTOM!!!
        hours_by_subject = historical_records.groupby('Subject').Hours.sum()
        hours_by_subject.plot(legend = True, kind = 'pie')
        x_label = plt.xlabel('Subject')
        y_label = plt.ylabel('Hours')
        title = plt.title('Hours Studied by Subject')
        plt.legend(loc = 'best')
        plt.tight_layout()
        plt.show()
        print(hours_by_subject)
        print('Not quite ready. Check back in a couple of days.')
    elif len(first_input) == 3:
        # Here we are going to start tracking.
        subject = first_input[0]
        date = first_input[1]
        hours = first_input[2]
        new_record = [subject,date,hours]
        if subject not in historical_records.Subject.unique():
            track = input(f'It looks like "{subject.title()} is new to our records. Would you like\n'
                          f'to start tracking it? (y/n): ').lower()
            if track == 'y':
                new_record = pd.DataFrame({'Subject': [subject], 'Date': [date], 'Hours': [hours]})
                historical_records = historical_records.append(new_record, ignore_index=True)

                historical_records.to_csv('record.csv', sep = ',', index = False)
        else:
            track = input(f'You are about to enter that you have studied [{subject.swapcase()}] for [{hours}]\n'
                          f'on [{date.swapcase()}]. Is this correct? (y/n): ').lower()
            if track == 'y':
                new_record = pd.DataFrame({'Subject': [subject], 'Date': [date], 'Hours': [hours]})
                historical_records = historical_records.append(new_record, ignore_index=True)

                historical_records.to_csv('record.csv', sep = ',', index = False)
    elif len(first_input) != 3: # This is the very last one!
        print('There should only be 4 entries: x x x x.')
    elif 'stop' in first_input:
        proceed -= 1
