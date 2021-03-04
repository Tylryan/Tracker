import pandas as pd

historical_records = pd.read_csv('records.csv', parse_dates = True, index_col='Date')
historical_records = historical_records.sort_values('Date', ascending = True)


def hours_studied_per_day():
    historical_records = pd.read_csv('records.csv', parse_dates = True, index_col='Date')
    historical_records = historical_records.sort_values('Date', ascending = True)
    subjects = historical_records.Subject.unique()

    df = pd.DataFrame()

    # Creating a base
    mask = historical_records.Subject == 'python'
    python_records = historical_records[mask]['Hours']
    df['python'] = python_records

    mask = historical_records.Subject == 'bash_scripting'
    bash_records = historical_records[mask]['Hours']
    df['bash_scripting'] = bash_records



    for i in subjects[1:]:
        mask = historical_records.Subject == i
        subject_records = pd.DataFrame(historical_records[mask]['Hours'])
        subject_records.columns = [i]
        df[i] = subject_records

    df = df.fillna(0)

    # Grouping the original dataframe by subject and averaging the hours spent on each subject. Then turning it into it's own dataframe.
    hr_grouped_by_subject = pd.DataFrame(df[-7:].mean().round(2))
    # Renaming the dataframe's column to "Hours Studied per Day"
    hr_grouped_by_subject.columns = ['Daily Avg']
    # Telling the user the results
    # Pausing the screen to let the user digest the information. Allows them to continue at their own pace.
    return hr_grouped_by_subject
print(hours_studied_per_day())