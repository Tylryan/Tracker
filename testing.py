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


##################################### If you don't have the correct files in your directory ##########################################################

def file_checking():
    functions.clear_terminal()
    # Check to see if the correct csv files are in the directory
    files_in_directory = [file for file in os.listdir('.')]
    # If they are not, put them there
    if 'record.csv' not in files_in_directory:
        no_record = True
        # This just tells the terminal (mac/linux)
        new_records = os.system('touch records.csv')
    if 'backups.csv' not in files_in_directory:
        no_backup = True
        new_backup = os.system('touch backup.csv')
    if (no_record == True )and (no_backup == True):
        print('You have neither a record.csv nor backup.csv')
        print('I will create them for you ')
        cont = input('Press "Enter" to continue. ')
file_checking()

##################################### If you have no data in your files ##############################################################################

def first_data():
    
    empty_records_file = os.stat("records.csv").st_size == 0
    if empty_records_file == True:
        # Create the column names "Subject","Date","Hours" in the empty records.csv.
        historical_data = pd.DataFrame(columns = ['Subject','Date','Hours'])

        # Sample Data
        subject = 'python'
        date = '02/25/25'
        hours = '1.5'

        # Creating the new dataframe.
        new_record = pd.DataFrame(
            {
                'Subject': [subject],
                'Date': [date],
                'Hours': [hours]
                
            }
        )

        historical_data = historical_data.append(new_record)
        historical_data.to_csv('records.csv', index = False)



# try:
#     historical_records = pd.read_csv('test.csv', parse_dates = True, infer_datetime_format = True)
#     historical_records = historical_records.sort_values('Date', ascending = True)

#     subject = 'python'
#     # Creating datetime format with only the date. Not seconds or anything.
#     date = pd.to_datetime('02/02/25').date()
#     hours = 1.5
#     # Creating a new record which will be appended to an empty dataframe
#     new_record = [subject,date,hours]
# except NameError:
#     print('There is no data in this file')