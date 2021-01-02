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
        input1 = input('Type in the Subject, Date, Hours Studied, Minutes Studied. Delimiter \n'
                       '-------------------------------------------------------------------->: ').lower().split()
        for i in input1:
            if i == 'help':
                print("""
                Here is an example: Python 12/26/20 2 50 \n

                To stop the program, type clear.
                To see the total hours logged for a particular subject type "Total Hours"
                ------------------------------------------------------------------------------------
                """)
                input2 = input('Now what would you like to do?').lower()
                if 'total hours' in input2:
                    subject_total_hours = input('For which subject would you like the total hours?: ').lower()
                    total_hours = 0
                    for i in historical_records[subject_total_hours][1:]:
                        for x in i:
                            total_hours += x['Hours']
                    print(f'You have studied {subject_total_hours} for {total_hours} hours.')




            elif i == 'clear':
                break
            elif (len(input1) != 4) and (input1 != 'help'):
                print('\n\nYou either have not typed in enough information, or you have typed too much. ')
                break
            else:
                subject = input1[0]
                date = input1[1]
                hours = round(int(input1[2]) + (int(input1[3]) / 60), 2)
                print(hours)
                if subject not in historical_records:
                    new_record[subject] = [{'Date': '',
                                            'Hours': 0
                                            }]
                    historical_records[subject] = new_record[subject]
                    new_record[subject] = [{'Date': date, 'Hours': hours}]
                    historical_records[subject].append(new_record[subject])
                    print(f'You have entered {new_record}')
                    break

                elif subject in historical_records:
                    new_record[subject] = [{'Date': date, 'Hours': hours}]
                    historical_records[subject].append(new_record[subject])
                    print(f'You have entered {new_record}')
                    break
    except:
        print('Hmm. Something went wrong. Try again. \n\n If you need more help, type "help"')

    with open('record.json', 'w') as file:
        file.write(str(historical_records))
        file.close()






