from datetime import datetime,date, time
print('Format = Hour Minute: NO COMMA OR ANYTHING')
    # start_time = input('Start Hour/Minute: ').split()
    # # start_hour = int(start_time[0])
    # # start_minute = int(start_time[1])
start = time(12, 36)

print('Format = Hour Minute: NO COMMA OR ANYTHING')
# end_time = input('End Hour/Minute: ').split()
# end_hour = int(end_time[0])
# end_minute = int(end_time[1])
end = time(15, 36)

print(datetime.combine(date.min, end) - datetime.combine(date.min, start))