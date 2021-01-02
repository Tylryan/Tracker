from pathlib import Path
import ast
import datetime

record_path = Path('record.json')

with open(record_path) as file:
    contents = file.read()
    historical_records = ast.literal_eval(contents)

    file.close()

new_record = {}
print("""
If you need more info, type "help".
-----------------------------------
""")
while True:
    try:
        input1 = input('Type in the Subject, Date, Hours Studied, Minutes Studied. Delimiter:  ').lower().split()
        print('-----------------------------------------------------------------------------')
        for i in input1:
            if i == 'help':
                print("""
                Here is an example: Python 12/26/20 2 50 \n

                1. To stop the program.
                2. For Stats
                3. Total Hours Logged.
                --------------------------------------------------------------------------
                """)
                input2 = input('Now what would you like to do?').lower()
                if '2' in input2:
                    input3 = input('''
                    Here are the following things that are tracked.
                    (1) Total Hours
                    (2) All Subjects. (Usefull for making sure you have not typos)
                    (3) Total Days Studied.
                    (4) Day with most entries
                    --------------------------------------------------------------
                    ''')
                    if '1' in input2:
                        subject_total_hours = input('Which subject would you like the total hours?: ').lower()
                        print('---------------------------------------------------------------------')
                        total_hours = 0
                        for i in historical_records[subject_total_hours][1:]:
                            for x in i:
                                total_hours += x['Hours']
                        print(f'You have studied {subject_total_hours} for {round(total_hours,2)} hours.'
                              f'------------------------------------------------------------------------\n')
                    elif '2' in input2.lower():
                        all_subjects = []
                        for i in historical_records:
                            all_subjects.append(i)
                        print(f'All subjects tracked: {all_subjects}.\n'
                              f'----------------------------------------')
                    elif '3' in input3.lower():
                        unique_days = []
                        total_days_studied = len(unique_days)
                        for i in historical_records['python'][1:]:
                            for x in i:
                                if x['Date'] not in unique_days:
                                    unique_days.append(x)
                        print(f'On record, you have studied {total_days_studied} days.\n'
                              f'----------------------------------------------------------')

            elif (len(input1) != 4) and (input1 != 'help'):
                print('\n\nYou either have not typed in enough information, or you have typed too much. ')
                break
            else:
                subject = input1[0]
                date = input1[1]
                hours = round(int(input1[2]) + (int(input1[3]) / 60), 2)
                if subject not in historical_records:
                    new_record[subject] = [{'Date': '',
                                            'Hours': 0
                                            }]
                    historical_records[subject] = new_record[subject]
                    new_record[subject] = [{'Date': date, 'Hours': hours}]
                    historical_records[subject].append(new_record[subject])
                    print(f'You have entered that you have studied {subject.capitalize()} for {hours} hours on {date}\n'
                          f'----------------------------------------------------------------------------------')
                    break

                elif subject in historical_records:
                    new_record[subject] = [{'Date': date, 'Hours': hours}]
                    historical_records[subject].append(new_record[subject])
                    print(f'You have entered that you have studied {subject.capitalize()} for {hours} hours on {date}\n'
                          f'----------------------------------------------------------------------------------')
                    break
    except:
        print('Hmm. Something went wrong. Try again. \n\n If you need more help, type "help"')



# with open('record.json', 'w') as file:
#     file.write(str(historical_records))
#     file.close()



