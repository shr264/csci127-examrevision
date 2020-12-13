#Predict what will be printed:
for i in range(4):
    print('The world turned upside down')
for j in [0,1,2,3,4,5]:
    print(j)   
for count in range(6):
    print(count)
for color in ['red', 'green', 'blue']:
    print(color)      
for i in range(2):
    print('Starting j loop for i = {}'.format(i))
    for j in range(2):
        print('This is j loop for j = {}'.format(j))
        print('Look around,')
    print('Ending j loop for i = {}'.format(i))
    print('How lucky we are to be alive!')