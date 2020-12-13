semHours = 18
reqHours = 120
if semHours >= 12:
    print('Full Time')
else:
    print('Part Time')
    
pace = reqHours // semHours
if reqHours % semHours != 0:
    pace = pace + 1
print('At this pace, you  will graduate in', pace, 'semesters,')
yrs = pace / 2
print('(or', yrs, 'years).')

for i in range(1,20):
    if(i > 10) and (i % 2 == 1):
        print('oddly large')
    else:
        print(i)