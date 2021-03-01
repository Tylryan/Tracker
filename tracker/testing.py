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

#! Create a class for data


# Try no to make the functions print questions. Let the main control the flow
historical_records = pd.read_csv('records.csv', parse_dates = True, infer_datetime_format = True)
historical_records = historical_records.sort_values('Date', ascending = True)
historical_records['Date'] = pd.to_datetime(historical_records['Date']).dt.date

class Records:
    do_you_want_to_save = False
    do_you_want_to_backup = False
    currently_tracking_subject = False
    


    def __init__(self, new_record, historical_records):
        self.new_record = new_record
        self.historical_records = historical_records
    #! Start here for saving stuff.
    def is_your_subject_in_our_records(self,subject):
        self.subject = subject
        if subject not in historical_records.Subject.unique():
            track = input(f'It looks like "{subject.upper()}" is new to our records. Would you like\n'
                        f'to start tracking it? [Y/n]: ').lower()
            if track == 'n':
                print(f'\n\n{subject.upper()} has NOT been added to the record books.')
                time.sleep(1.5)
                pass #! Potentially might need to fix this
            else:
                print(f'{self.subject} will now be tracked.')
                self.currently_tracking_subject = True #This actually changes to true
        else:
            self.currently_tracking_subject = True
        

    def do_you_want_to_save_hm(self,would_you_like_to_save):
        if 'n' in would_you_like_to_save:
            print('You are not saving')
            pass
        else:
            print('You are saving')
            self.do_you_want_to_save = True
    #! End here for saving stuff.
    def do_you_want_to_backup_hm(self, would_you_like_to_backup):
        if 'n' in would_you_like_to_backup:
            print('You have not backed up your data')
            pass
        else:
            self.do_you_want_to_backup = True
            print('you have backed up your data')

subject = 'python'
date = '02/25/25'
hours = 1.5
new_record = pd.DataFrame(
    {
        'Subject': [subject],
        'Date': [date],
        'Hours': [hours]    
    }
)

new_entry = Records(new_record,historical_records)

new_entry.is_your_subject_in_our_records(subject)





































# class Stopwatch:
#     does_user_want_to_save = False
#     does_user_want_to_backup = False
#     def __init__(self, historical_records):
#         self.historical_records = historical_records

#     def tracker(self,historical_records,to_track):

#         while True:
#             functions.clear_terminal()
#             try:
#                 subject = to_track[0]
#                 date = to_track[1]
#                 if ('/' or '-') not in date:
#                     print('You have not entered something correctly')
#                     cont = input('Press "Enter to continue ')
#                     break
#                 # Clear the terminal here
#                 print('This stopwatch returns values in terms of hours rounded to the hundredths\n\n'
#                 'For example, 10 minutes will return 0.17 hours')
#                 print('\n\n----------------------------------------------------------------------')
#                 start_input = input('Time will be STARTED after you press "Enter". ')
#                 stopwatch_start = dt.datetime.now()
#                 print(f'\nRecording Time: {stopwatch_start}')
#                 print('----------------------------------------------------------------------')

#                 end_input = input('\nTime will be STOPPED after you press "Enter"')
#                 stopwatch_end = dt.datetime.now()

#                 studied = round((stopwatch_end - stopwatch_start).total_seconds() / 3600,2)
#                 print(f'\nRecording Ended: {stopwatch_end}\n')
#                 time.sleep(1.0)
#                 # Clear Terminal
#                 print('################################ && ##################################\n')
#                 print(f'You have studied for {studied} hours')
#                 print('\n################################ && ##################################\n\n\n')
#                 cont = input('Press Enter to continue ')

#                 hours = studied
#                 return subject, date, hours
#             except IndexError:
#                     print('\n...')
#                     time.sleep(1.5)
#                     print('Looks like you didn\'t enter something in correctly')
#                     cont = input('Press "Enter" to retry or "N" to go back to the main menu: ').lower()
#                     if 'n' in cont:
#                         break


#     def tracker_save_decisions(self, historical_records,would_you_like_to_save,would_you_like_to_backup):
#         subject, date, hours = self.tracker(historical_records, to_track)
#         while True:
#             functions.clear_terminal()
#             try:

#                 #! Add a way to automatically save data locally to a different file for backup
#                 if 'n' in would_you_like_to_save:
#                     print('Your data has NOT been saved ')
#                     time.sleep(1.5)
#                 else:

#                     if subject not in historical_records.Subject.unique():
#                         track = input(f'It looks like "{subject.upper()}" is new to our records. Would you like\n'
#                                         f'to start tracking it? [Y/n]: ').lower()
#                         if 'y' in track:
#                             print(f'\n\n{subject.upper()} has NOT been added to the record books.')
#                             time.sleep(1.5)
#                         else:
#                             new_record = pd.DataFrame(
#                                                     {'Subject': [subject],
#                                                     'Date': [date], 
#                                                     'Hours': [hours]
#                                                     }
#                                                 )
#                             save(new_record,historical_records)
#                             #This is the back up save. Can be recovered if original data is corrupted.
#                             backup(historical_records)
#                     else:
#                         print('----------------------------------------------------------------------')
#                         track = input(f'You are about to enter that you have studied [{subject.swapcase()}] for [{hours}] hours\n'
#                                         f'on [{date}]. Is this correct? [Y/n]: ').lower()
#                         print('----------------------------------------------------------------------')

#                         if 'n' in track:
#                             break
#                         else:
#                             new_record = pd.DataFrame(
#                                                     {'Subject': [subject],
#                                                     'Date': [date], 
#                                                     'Hours': [hours]
#                                                     }
#                                                 )
#                             save(new_record, historical_records)
#                             # This backup function asks them if they want to save first.        
#                             backup(historical_records)
#             except UnboundLocalError and TypeError:
#                 print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#                 print('Nice Try. You almost broke me. Enter in something valid next time\n\n ')
#                 cont = input('Press "Enter" to retry: ')

# # Starting and stopping the stopwatch and storing the output
# new_stopwatch_time = Stopwatch(historical_records)
# to_track = input('Enter the SUBJECT and DATE of the task you want to start: ').lower().split()
# new_stopwatch_time.tracker(historical_records, to_track)

# # Saving that output
# would_you_like_to_save = input('Would You like to enter this data? [Y/n]: ')
