from pathlib import Path
import ast
from datetime import time, date, datetime

record_path = Path('record.json')

with open(record_path) as file:
    contents = file.read()
    historical_records = ast.literal_eval(contents)

    file.close()

new_record = {}

proceed = 1
while proceed == 1:
    try:
        print("""
        If you need more info, type "help".
        -----------------------------------
        """)
        input1 = input('Type in the Subject, Date, Hours Studied, Minutes Studied. Delimiter:  ').lower().split()
        print('-----------------------------------------------------------------------------')
        for i in input1:
            if i == 'help':
                print("""
                Here is an example: Python 12/26/20 2 50 \n

                (1) Log study Time.
                (2) For Stats
                (3) Time Calculator
                (4) To stop the program.

                --------------------------------------------------------------------------
                """)
                input2 = input('Now what would you like to do?: ')
                print('-----------------------------------------')
                if '4' in input2:
                    print('Program Stopped')
                    proceed -= 1
                elif '1' in input2:
                    break
                elif '2' in input2:
                    print('''
                    Here are the following things that are tracked.
                    (1) Total Hours
                    (2) All Subjects. (Useful for making sure you have not typos)
                    (3) Total Days Studied.
                    (4) Day with most entries
                    --------------------------------------------------------------
                    ''')
                elif '3' in input2:
                    # Create a time calculator e.g. 15:36 - 12:36 = 3 Hours
                    print('Format = Hour Minute: NO COMMA OR ANYTHING')
                    start_time = input('Start Hour/Minute: ').split()
                    start_hour = int(start_time[0])
                    start_minute = int(start_time[1])
                    start = time(start_hour,start_minute)

                    print('Format = Hour Minute: NO COMMA OR ANYTHING')
                    end_time = input('End Hour/Minute: ').split()
                    end_hour = int(end_time[0])
                    end_minute = int(end_time[1])
                    end = time(end_hour,end_minute)

                    time_studied = datetime.combine(date.min, end) - datetime.combine(date.min, start)
                    print(f'You have studied for {time_studied} hours.')
                    break

                input3 = input('Which one would you like to see stats for?: ')
                if '1' in input3:
                    subject_total_hours = input('Which subject would you like the total hours?: ').lower()
                    print('---------------------------------------------------------------------')
                    total_hours = 0
                    for i in historical_records[subject_total_hours][1:]:
                        for x in i:
                            total_hours += x['Hours']
                    print(f'You have studied {subject_total_hours} for {round(total_hours,2)} hours.'
                          f'------------------------------------------------------------------------\n')
                elif '2' in input3:
                    all_subjects = []
                    for i in historical_records:
                        all_subjects.append(i)
                    print(f'All subjects tracked: {all_subjects}.\n'
                          f'----------------------------------------')
                elif '3' in input3:
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
                    new_record[subject] = [{"Date": "",
                                            "Hours": 0
                                            }]
                    historical_records[subject] = new_record[subject]
                    new_record[subject] = [{"Date": date, "Hours": hours}]
                    historical_records[subject].append(new_record[subject])
                    print(f'You have entered that you have studied {subject.capitalize()} for {hours} hours on {date}\n'
                          f'----------------------------------------------------------------------------------')

                    correct = input('Is this correct? (y/n)').lower()
                    print('----------------------------------------------')
                    if 'y' in correct:
                        output = Path('record.json')
                        with open(output, 'w') as file:
                            file.write(str(historical_records))
                            file.close()
                        print(f'[{subject}] was not in the record books, but I added it. ')
                        break
                    else:
                        print("Well then. Let's try that again. As of right now, I cannot remove files once they are inserted.")



                elif subject in historical_records:
                    print(f'You have entered that you have studied {subject.capitalize()} for {hours} hours on {date}\n'
                          f'----------------------------------------------------------------------------------')
                    correct = input('Is this correct? (y/n)').lower()
                    print('------------------------------------------------')
                    if 'y' in correct:
                        output = Path('record.json')
                        new_record[subject] = [{"Date": date, "Hours": hours}]
                        historical_records[subject].append(new_record[subject])
                        print(f'You have entered that you have studied {subject.capitalize()} for {hours} hours on {date}\n'
                              f'----------------------------------------------------------------------------------')
                        output = Path('record.json')
                        with open(output, 'w') as file:
                            file.write(str(historical_records))
                            file.close()
                        break
                    else:
                        print("Well then. Let's try that again. As of right now, I cannot remove files once they are inserted.")
    except:
        print('Hmm. Something went wrong. Try again. \n\n If you need more help, type "help"')






