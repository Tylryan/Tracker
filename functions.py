#! /bin/python

import pandas as pd
import csv
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
import time 
import os
#! Eventually, I would the graphs to be in a dashboard.
#! Eventually, you are going to want to see the weekly change in total hours by subject.
    #* Figure out how to subtract 2 group by with .diff().
    #* Last 7 days grouped minus 8 to 14 days grouped.
    #* This week you studied Python for 5 more hours.
#! I would also like to see a desktop version. Perhaps using Tkinter.


# historical_records = pd.read_csv('record.csv', parse_dates=True, infer_datetime_format=True)
# historical_records = historical_records.sort_values('Date', ascending = True)
############################## CLEARING THE TERMINAL ######################################
# A useful function that clears the terminal to avoid clutter
def clear_terminal():
    # If the system is microsoft, then print to the terminal "cls". If the system is not microsoft, print to the terminal "clear"
    clear = os.system('cls' if os.name == 'nt' else 'clear')
    return clear

#!##################################### If the user has not previous files or data #######################################################

##################################### Checking that the correct files are in this directory ##########################################################

def file_checking():
    try:
        clear_terminal()
        # Check to see if the correct csv files are in the directory

        # Gets all the files and directories in the current directory
        files_in_directory = [file for file in os.listdir('.')]
        # Checks to see if "records.csv" is in the current directory
        no_record = False
        no_backup = False
        if 'records.csv' not in files_in_directory:
            no_record = True
        # Checks to see if "backup.csv" is in the current directory
        if 'backup.csv' not in files_in_directory:
            no_backup = True

        # Creates csv files if both are not there
        if (no_record == True ) and (no_backup == True): # Both yes and no work 2-19-21
            print('You have neither a record.csv nor backup.csv')
            new_files = input('I will create them for you if you want: y/n: ')
            if 'y' in new_files:

            # This just tells the terminal (mac/linux)
                new_records = os.system('touch records.csv')
                new_backup = os.system('touch backup.csv')
                cont = input('Press "Enter" to continue ')
            else:
                print('No new files were created')
                print('You are now leaving this program')
                time.sleep(2)
                exit_program = os.sys.exit()
    except: # This try except loop doesn't work
        print('One of your files might me missing ')
        print("Don't worry too much. Just copy and paste one to the other ")

##################################### Checking if there is any data in those files ##############################################################################

def first_data():
    empty_records_file = os.stat("records.csv").st_size == 0
    if empty_records_file == True:
        print('You have no data in your records.csv')
        print('Let\'s enter in a new record' )
        cont = input('Press "Enter" to continue' )
        # Create the column names "Subject","Date","Hours" in the empty records.csv.
        historical_data = pd.DataFrame(columns = ['Subject','Date','Hours'])
        print('Please use a space as the delimiter!!')
        creating_data = input('Type in the SUBJECT, DATE, and HOURS spent in this format\n\n'
        'Python 01/01/25 1.5: ').lower().split()
        subject = creating_data[0]
        date = creating_data[1]
        hours = creating_data[2]

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
        historical_data.to_csv('backup.csv', index = False)

############################## TIME CALCULATOR ######################################
# Allows you to insert the the time of day you started and stopped studying. Then calculates the time spent studying.
def time_calculator():
    
    # Trying the below code.
    try: 
        #Clear the terminal to reduce clutter.
        clear_terminal()

        subject_date = input('Enter the subject and date you are calculating for: ').lower().split()
        subject = subject_date[0]
        date = subject_date[1]

        print('Format = Hour Minute: NO COMMA OR ANYTHING')

        # Getting start time information from the user.
        start_time = input('Start Hour/Minute: ').split()
        # Separating the input by hour and minute
        start_hour = int(start_time[0])
        start_minute = int(start_time[1])
        # Using timedelta to create an actual time the computer can use to calucalate.
        start = dt.timedelta(hours = start_hour, minutes= start_minute)

        print('Format = Hour Minute: NO COMMA OR ANYTHING')
        # Getting the end time from the user.
        end_time = input('End Hour/Minute: ').split()
        # Separating the input by hour and minute
        end_hour = int(end_time[0])
        end_minute = int(end_time[1])
        # Using timedelta to create an actual time the computer can use to calucalate.
        end = dt.timedelta(hours = end_hour, minutes= end_minute)
        # Using time delta to calculate the difference between end time and start time.
        hours = round((end - start).total_seconds() / 3600,2)
        new_record = [subject,date,hours]
        # Telling the user the amount of time they have studied.
        print(f'\n\nYou have studied for {hours} hours.')
        # Pausing the screen to let the user digest the information. Allows them to continue at their own pace.
        cont = input('Press "Enter" to continue: ')
        print('----------------------------------------------------------------------\n')
        # Clearing the terminal to reduce clutter.
    # If the input doesn't work by user error or the code's, then it won't break the code, it will just restart to the top.
        return subject, date, hours, new_record
    except:
        print("\n################## Error #####################\n"
                "You probably didn't enter the right time.\n")
        # Stoping the code to allow the user to digest the error message. Let's the user continue at their own pace.
        cont = input('Press "Enter" to continue: ')
        clear_terminal()

############################## DATA REPORTS (NO GRAPHS) ######################################

# This will show the user the total hours spent studying each subject from the time they started to use the program.
def hours_by_subject(historical_records):

    # Grouping the data by subject and summing the hours. Then turning that into a dataframe.
    total_hours = pd.DataFrame(historical_records.groupby('Subject').Hours.sum())
    # Renaming the column to "Hours Studied"
    total_hours.columns = ['Hours Studied']
    # Showing the user how many hours they studied each subject
    print(f'Total Hours Studied by Subject: \n\n'
        f'{total_hours}')
    # Pausing the screen to let the user digest the information. Allows them to continue at their own pace.
    enter = input('Press "Enter" to continue: ')



# This will show the user the total amount of time spent studying for the past seven days (Weekly)
def past_seven_days(historical_records):
    # Setting the date as the index
    indexed = historical_records.set_index('Date')
    # Essentially reducing duplicate days. This will be used as a dictionary of sorts.
    unique_days = indexed.index.unique()
    # Creating a mask that takes the dates from the "Dictionary" above and chooses the last seven entries. I.e. The last seven days.
    seven_days_ago = unique_days[-7]
    # Applying the mask to the indexed dataframe to return all data from the last seven days.
    seven_days_of_data = indexed[indexed.index >= seven_days_ago]
    # Grouping the data from the last seven days by subject and summing the hours.
    grouped_seven = pd.DataFrame(seven_days_of_data.groupby('Subject').Hours.sum())
    # Renaming the new dataframe column to "Hours Studied"
    grouped_seven.columns = ['Hours Studied']
    # Telling the user the results.
    print(f'----------------------------------------------------------------------'
        f'\n\nTotal Hours for the Last Seven Days.\n\n'
        f'{grouped_seven}\n\n'
        f'----------------------------------------------------------------------')
    # Pausing the screen to let the user digest the information. Allows them to continue at their own pace.
    enter = input('Press "Enter" to continue: ')

# Finding the average amount of hours studied per day by subject.
def hours_studied_per_day(historical_records):
    # Grouping the original dataframe by subject and averaging the hours spent on each subject. Then turning it into it's own dataframe.
    hr_grouped_by_subject = pd.DataFrame(historical_records.groupby('Subject').Hours.mean().round(2))
    # Renaming the dataframe's column to "Hours Studied per Day"
    hr_grouped_by_subject.columns = ['Hours Studied per Day']
    # Telling the user the results
    print(hr_grouped_by_subject)
    # Pausing the screen to let the user digest the information. Allows them to continue at their own pace.
    enter = input('Press "Enter" to continue: ')

############################## GRAPHS ######################################
def pie_hours_by_subject(historical_records):
    # grouping the original dataframe by subject and summing the hours.
    hours_by_subject = historical_records.groupby('Subject').Hours.sum()
    # Creting a pie chart that displays the results
    plot = hours_by_subject.plot(legend = True, kind = 'pie')
    # Naming the x label of the chart to subject
    x_label = plt.xlabel('Subject')
    # Naming the y label of the chart to hours
    y_label = plt.ylabel('Hours')
    # Giving the graph a title
    title = plt.title('Hours Studied by Subject')
    # Setting the legend to be in the best location
    plt.legend(loc = 'best')
    # Making the graph layout to be as compact as possible
    plt.tight_layout()
    # Displaying the graph to the user
    plt.show()


# Creating a bar chart that displays total hours studied by subject for the past seven days or week.
def past_seven_days_graph(historical_records):
    # Setting the index of the original dataframe as the date
    indexed = historical_records.set_index('Date')
    # Finding the unique days to use as a "Dictionary" of sorts
    unique_days = indexed.index.unique()
    # Finding the last seven days of the week
    seven_days_ago = unique_days[-7]
    # Creating a mask that captures the last seven days
    last_seven_days = indexed.index >= seven_days_ago
    # Filtering out the indexed dataframe to only display all data fromthe last sevend days
    seven_days_of_data = indexed[last_seven_days]
    # Grouping this filtered data by subject and summing the hours and turning it into a dataframe.
    grouped_seven = pd.DataFrame(seven_days_of_data.groupby('Subject').Hours.sum())
    # Renaming the column of the dataframe to "Hours"
    grouped_seven.columns = ['Hours']
    # Creating a bar chart to display the results
    grouped_seven.plot(
                    # Setting the chart to a bar chart
                    kind = 'bar', 
                    # Creating a legend
                    legend = True, 
                    # Setting the size of the chart
                    figsize = (20,10))
    # Giving the chart a title
    title = plt.title('Total Hours Logged By Subject For The Last Week')
    # Naming the y label/axis
    ylabel = plt.ylabel('Hours Logged')
    # Displaying the chart to the user
    plt.show()

# Creating a line graph that shows the user the seven day rolling/moving average of hours spent studying by subject
# Getting all the subjects.
def weekly_rolling_avg_graph(historical_records):
    # Creating a live list of subject studied.
    subjects = [unique for unique in historical_records['Subject'].unique()]
    # Creating a mask that will return only the data that pertains to python
    mask = historical_records['Subject'] == 'python'
    # Creating an initial dataframe that will be used as the base to conatenate all other dataframes
    initial_df = pd.DataFrame(historical_records[mask].groupby('Date').sum())

    # Adding the other's to the dataframe.
    for i in subjects:
        print(i)
        # Creating a filter
        mask = historical_records['Subject'] == i
        # Applying filter to historical records
        temp_df = historical_records[mask].groupby('Date').sum()
        # Turning the data into a dataframe.
        new_df= pd.DataFrame(temp_df)
        # Creating Column names for the new columns.
        new_df.columns = [f'{i.title()} Hours']        
        # Combining all the new dataframes to the existing one.
        initial_df = pd.concat([initial_df,new_df], axis = 'columns', join = 'outer')
    # Replacing the NaNs with 0
    combined_df = initial_df.fillna(0)
    # Dropping the extra column from the initial dataframe
    subjects_in_columns = combined_df.drop(columns = ['Hours'])
    # Finding the seven day rolling/moving average of hours spent studying by subject
    rolling_7 = subjects_in_columns.rolling(window = 7).mean()
    # Creating a graph that will display the results
    rolling_7.plot()
    # Displaying the graph to the user
    plt.show()

    
    ################################ SAVING ########################################
# This is the initial save
def save(new_record, historical_records):
    # Updating the historical records to reflect the new entry
    historical_records['Date'] = pd.to_datetime(historical_records['Date']).dt.date
    updated_historical_records = historical_records.append(new_record)
    # This is the main save. Could be corrupted by faulty code.
    updated_historical_records.to_csv('records.csv', sep = ',', index = False)
    ############################### Backup #########################################
# This is an independent backup save in case the original save gets messed up
def backup(historical_records):
    # This print statement helps verify that nothing went wrong with the code.
    print('These are the last ten records. If they look correct, then backup is safe.\n\n')
    historical_records = pd.read_csv('records.csv', parse_dates=True, infer_datetime_format=True)
    historical_records['Date'] = pd.to_datetime(historical_records['Date']).dt.date
    print(historical_records.tail(10))
    # Asking the user if they would like to back up their files
    backup = input('\n\nWould You like to back this data up? [Y/n] ')
    # A conditional statement depending on the user's input
    if 'n' in backup.lower():
        # If the user doesn't want to backup their data, then this elif statement will be activated
        # Confirming to the user that their data has not been backed up
        print('\n\nBackup database has NOT been updated.')
        # This give the user time to digest the the message above
        time.sleep(1.5)
    else:
        # If the user wants to backup their data, this is the backup save that saves to a file called "backup.csv"
        historical_records['Date'] = pd.to_datetime(historical_records['Date']).dt.date
        historical_records.to_csv('backup.csv', sep = ',', index = False)
        print('Your backup has been saved. ')
        time.sleep(1.5)


############################### Stopwatch Saving ###################################################
    # Here we are going to start tracking.
def tracker(historical_records):
    to_track = input('Insert the subject you would like to track and the current day ').lower().split()
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

def tracker_save_decisions(first_input, historical_records):
    clear_terminal()
    try:

        if len(first_input) == 2: # NOTE THIS ALLOWS YOU TO AUTOMATICALL GO TO TIME TRACKING WITHOUT PRESSING 2.
            subject, date, hours, new_record = tracker(historical_records)
        elif first_input[0] == '1':
            subject, date, hours, new_record = tracker(historical_records)
        #! Add a way to automatically save data locally to a different file for backup
        would_you_like_to_save = input('Would You like to enter this data? y/n: ')
        if 'y' in would_you_like_to_save:

            if subject not in historical_records.Subject.unique():
                track = input(f'It looks like "{subject.upper()}" is new to our records. Would you like\n'
                                f'to start tracking it? (y/n): ').lower()
                if track == 'y':
                    new_record = pd.DataFrame(
                                            {'Subject': [subject],
                                            'Date': [date], 
                                            'Hours': [hours]
                                            }
                                        )
                    save(new_record,historical_records)
                    #This is the back up save. Can be recovered if original data is corrupted.
                    backup(historical_records)
                else:
                    print(f'\n\n{subject.upper()} has NOT been added to the record books.')
                    time.sleep(1.5)
            else:
                print('----------------------------------------------------------------------')
                track = input(f'You are about to enter that you have studied [{subject.swapcase()}] for [{hours}] hours\n'
                                f'on [{date}]. Is this correct? (y/n): ').lower()
                print('----------------------------------------------------------------------')
                if track == 'y':
                    new_record = pd.DataFrame(
                                            {'Subject': [subject],
                                            'Date': [date], 
                                            'Hours': [hours]
                                            }
                                        )
                    save(new_record, historical_records)
                    # This backup function asks them if they want to save first.        
                    backup(historical_records)
        else:
            print('Your data has NOT been saved ')
            time.sleep(1.5)
    except UnboundLocalError:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('Nice Try. You almost broke me. Enter in something valid next time\n\n ')
        cont = input('Press "Enter" to continue: ')

####################################### Time Calculator Save ##############################################################
def time_calculator_save_decisions(first_input, historical_records):
    try:
        clear_terminal()
        subject, date, hours, new_record = time_calculator()
        #! Add a way to automatically save data locally to a different file for backup
        would_you_like_to_save = input('Would You like to enter this data? y/n: ')
        if 'y' in would_you_like_to_save:

            if subject not in historical_records.Subject.unique():
                track = input(f'It looks like "{subject.upper()}" is new to our records. Would you like\n'
                                f'to start tracking it? (y/n): ').lower()
                if track == 'y':
                    new_record = pd.DataFrame(
                                            {'Subject': [subject],
                                            'Date': [date], 
                                            'Hours': [hours]
                                            }
                                        )
                    save(new_record,historical_records)
                    #This is the back up save. Can be recovered if original data is corrupted.
                    backup(historical_records)
                else:
                    print(f'\n\n{subject.upper()} has NOT been added to the record books.')
                    time.sleep(1.5)
            else:
                print('----------------------------------------------------------------------')
                track = input(f'You are about to enter that you have studied [{subject.swapcase()}] for [{hours}] hours\n'
                                f'on [{date}]. Is this correct? (y/n): ').lower()
                print('----------------------------------------------------------------------')
                if track == 'y':
                    new_record = pd.DataFrame(
                                            {'Subject': [subject],
                                            'Date': [date], 
                                            'Hours': [hours]
                                            }
                                        )
                    save(new_record, historical_records)
                    # This backup function asks them if they want to save first          
                    backup(historical_records)
        else:
            print('Your data has NOT been saved ')
            time.sleep(1.5)
    except UnboundLocalError:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('Nice Try. You almost broke me. Enter in something valid next time\n\n ')
        cont = input('Press "Enter" to continue: ')

############################################ REMOVING AN ENTRY ###################################################

#! Instead of showing the user the historical records, maybe just show the last 20.
#! Better yet, just show the last entry for each subject.
def remove(historical_records):
    while True:
        try:
            # Clearing the terminal to reduce clutter
            clear_terminal()
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
                # Checking to make sure it's ok to back up data
                cont = input('Would you like me to update the backup.csv as well? [Y/n]: ').lower()
                if 'n' in cont:
                    break
                else:
                    # Saving the data
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