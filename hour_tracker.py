from pathlib import Path
import ast

record_path = Path('record.json')

with open(record_path) as file:
    contents = file.read()
    historical_records = ast.literal_eval(contents)

    file.close()

new_record = {}
input = input('Type in the Subject, Date, Hours Studied, Minutes Studied. Delimiter = " ": ').split()
subject = input[0]
date = input[1]
hours = round(int(input[2]) + (int(input[3]) / 60),2)
print(hours)
if subject not in historical_records:
    new_record[subject] = [{'Date': '',
                           'Hours': 0
    }]
    historical_records[subject] = new_record[subject]
    new_record[subject] = [{'Date': date, 'Hours': hours}]
    historical_records[subject].append(new_record[subject])

elif subject in historical_records:
    new_record[subject] = [{'Date': date, 'Hours': hours}]
    historical_records[subject].append(new_record[subject])

print(new_record)


with open('record.json', 'w') as file:
    file.write(str(historical_records))
    file.close()





