#Counting plurals
nouns = input('Enter nouns: ') #shoe socks sweater suits
m = nouns.split()
plural = 0
for word in m:
    if word[-1] == 's':
        plural = plural + 1
print("Number of plurals is", plural)



nouns = input('Enter nouns: ') #shoe socks sweater suits
num = nouns.count('s ')
if nouns[-1] == 's':
    num = num+1
print("Number of nouns is", num)

