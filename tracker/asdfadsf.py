import pandas as pd

historical_records = pd.read_csv('historical_records.csv', parse_dates = True, index_col='Date')
historical_records = historical_records.sort_values('Date', ascending = True)

# subjects = historical_records.Subject.unique()

# df = pd.DataFrame()

# # Creating a base
# mask = historical_records.Subject == 'python'
# python_records = historical_records[mask]['Hours']
# df['python'] = python_records

# print(df)

# for i in subjects[1:]:
#     mask = historical_records.Subject == i
#     subject_records = pd.DataFrame(historical_records[mask]['Hours'])
#     subject_records.columns = [i]
#     df = pd.concat([df,subject_records], axis = 'columns', join = 'outer')

# df = df.fillna(0)

# print(df)

# df.to_csv('historical_records.csv')


# Creating a new record

subject = 'python'
date = '02/25/25'
hours = 1.5

new_records = pd.Series(
    {
        subject:hours
    }, name=date

)

# print(historical_records)
# historical_records = historical_records.append(new_records)
# print(historical_records)


a = historical_records.loc['2021-02-21':'2021-02-25']
print(a)