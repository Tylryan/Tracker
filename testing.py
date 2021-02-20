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

############################################ REMOVING AN ENTRY ###################################################

#! Instead of showing the user the historical records, maybe just show the last 20.
#! Better yet, just show the last entry for each subject.
def remove(historical_records):
    while True:
        try:
            # Clearing the terminal to reduce clutter
            functions.clear_terminal()
            last_items_entered = historical_records.groupby('Subject').last()
            print(f'These are the last records entered BY SUBJECT\n\n'
                    f'{last_items_entered}\n\n')
            # Asking the user which entry they would like to remove
            item_to_remove = input('Type in the SUBJECT and DATE of the entry you would\n'
            'like to remove: ').lower().split()

            # Defining the subject and date
            subject = item_to_remove[0]
            date = pd.to_datetime(item_to_remove[1]).date()

            # Creating a mask that identifies in the dataframe which record the user if referring to.
            removal_mask  = (historical_records['Subject'] == subject) & (historical_records['Date'] == date)
            # Reterning the entire row the user is referring to.
            item_to_remove_row = historical_records[removal_mask]
            # Grabing the index number/unique identifier.
            item_to_remove_index = historical_records.index[removal_mask][0]
            print('----------------------------------------------------------------------')
            print(f'To Remove: "{subject} {date}"\n\n')
            cont = input(f'Would you like to continue? [Y/n]: ').lower()
            print('----------------------------------------------------------------------')
            # This flow makes it to where the user can press any key except "n" to continue
            if 'n' in cont:
                pass
            else:
                # Dropping the entry.
                historical_records.drop([item_to_remove_index], inplace = True)
                print(f'Ok. Removing {subject} {date}"\n')
                time.sleep(1.5)
                print(f'\n\n"{subject} {date}" has been removed ')
                # Saving the new records.
                historical_records['Date'] = pd.to_datetime(historical_records['Date']).dt.date
                historical_records.to_csv('records.csv', sep = ',', index = False)
                cont = input('Would you like me to update the backup.csv as well? [Y/n]: ').lower()
                if 'n' in cont:
                    break
                else:
                    historical_records['Date'] = pd.to_datetime(historical_records['Date']).dt.date
                    historical_records.to_csv('backup.csv', sep = ',', index = False)

                cont = input('Would you like to remove another? [Y/n]: ')
                if 'n' in cont:
                    break
                else:
                    pass
        except IndexError:
            print('\n...')
            time.sleep(1.5)
            print('It doesn\'t look like I have that in the system\n\n ')
            time.sleep(1.5)
            cont = input('Would you like to retry? [Y/n]: ')
            if 'n' in cont:
                break
        except ValueError:
            print('\n...')
            time.sleep(1.5)
            print('\nYou might have entered in some information wrong...\n')
            print('It doesn\'t look like I have that in the system\n\n ')
            time.sleep(1.5)
            cont = input('Would you like to retry? [Y/n]: ')
            if 'n' in cont:
                break

remove(historical_records)

