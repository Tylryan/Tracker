
import pandas as pd
import csv
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import time 
import os
#! Eventually, I would the graphs to be in a dashboard.
# historical_records = pd.read_csv('record.csv', parse_dates=True, infer_datetime_format=True)
# historical_records = historical_records.sort_values('Date', ascending = True)
############################## CLEARING THE TERMINAL ######################################
def clear_terminal():
    clear = os.system('cls' if os.name == 'nt' else 'clear')
    return clear

############################## TIME STUDIED CALCULATOR ######################################
def time_calculator():
    
    try: 
        clear_terminal()
        print('Format = Hour Minute: NO COMMA OR ANYTHING')
        start_time = input('Start Hour/Minute: ').split()
        start_hour = int(start_time[0])
        start_minute = int(start_time[1])
        # This is an easy way to calculate time spent.
        start = datetime.timedelta(hours = start_hour, minutes= start_minute)

        print('Format = Hour Minute: NO COMMA OR ANYTHING')
        end_time = input('End Hour/Minute: ').split()
        end_hour = int(end_time[0])
        end_minute = int(end_time[1])
        end = datetime.timedelta(hours = end_hour, minutes= end_minute)

        time_studied = end - start
        print(f'\n\nYou have studied for {time_studied} hours.')
        cont = input('Press "Enter" to continue: ')
        clear_terminal()


        # This clears the terminal to avoid clutter.
    except:
        print("\n################## Error #####################\n"
                "You probably didn't enter the right time.\n")
        cont = input('Press "Enter" to continue: ')
        clear_terminal()

############################## DATA REPORTS (NO GRAPHS) ######################################
def hours_by_subject(historical_records):

    total_hours = pd.DataFrame(historical_records.groupby('Subject').Hours.sum())
    total_hours.columns = ['Hours Studied']
    print(f'Total Hours Studied by Subject: \n\n'
        f'{total_hours}')
    enter = input('Press "Enter" to continue: ')

def past_seven_days(historical_records):
    indexed = historical_records.set_index('Date')
    unique_days = indexed.index.unique()
    seven_days_ago = unique_days[-7]
    seven_days_of_data = indexed[indexed.index >= seven_days_ago]
    grouped_seven = pd.DataFrame(seven_days_of_data.groupby('Subject').Hours.sum())
    grouped_seven.columns = ['Hours Studied']
    print(f'----------------------------------------------------------------------'
        f'\n\nTotal Hours for the Last Seven Days.\n\n'
        f'{grouped_seven}\n\n'
        f'----------------------------------------------------------------------')
    enter = input('Press "Enter" to continue: ')
# Finding the average amount of hours studied per day by subject.
def hours_studied_per_day(historical_records):
    hr_grouped_by_subject = pd.DataFrame(historical_records.groupby('Subject').Hours.mean().round(2))
    hr_grouped_by_subject.columns = ['Hours Studied per Day']
    print(hr_grouped_by_subject)
    enter = input('Press "Enter" to continue: ')
############################## GRAPHS ######################################
def pie_hours_by_subject(historical_records):

    hours_by_subject = historical_records.groupby('Subject').Hours.sum()
    plot = hours_by_subject.plot(legend = True, kind = 'pie')
    x_label = plt.xlabel('Subject')
    y_label = plt.ylabel('Hours')
    title = plt.title('Hours Studied by Subject')
    plt.legend(loc = 'best')
    plt.tight_layout()
    plt.show()

def past_seven_days_graph(historical_records):
    indexed = historical_records.set_index('Date')
    unique_days = indexed.index.unique()
    seven_days_ago = unique_days[-7]
    seven_days_of_data = indexed[indexed.index >= seven_days_ago]
    grouped_seven = seven_days_of_data.groupby('Subject').Hours.sum()
    grouped_seven.columns = ['Subject','Hours']
    grouped_seven.plot(kind = 'bar', legend = True, figsize = (20,10))
    title = plt.title('Total Hours Logged By Subject For The Last Week')
    ylabel = plt.ylabel('Hours Logged')
    plt.show()

# This is the 7-day rolling average.
# Getting all the subjects.
def weekly_rolling_avg_graph(historical_records):
    # Creating a live list of subject studied.
    subjects = [unique for unique in historical_records['Subject'].unique()]
    # Creating a single dataframe to add the others to.
    mask = historical_records['Subject'] == 'python'
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


    subjects_in_columns = combined_df.drop(columns = ['Hours'])


    rolling_7 = subjects_in_columns.rolling(window = 7).mean()
    print(rolling_7)

    rolling_7.plot()
    plt.show()

    
    ################################ SAVING ########################################

        
    ############################### Backup #########################################

