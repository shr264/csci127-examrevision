pioneers = "Lovelace,Ada-Fleming,Williamina-Hopper,Grace"
num = pioneers.count(',')
num = num + pioneers.count('-')
print(pioneers[len(pioneers)-num:])

names = pioneers.split('-')
l = names[0].split(',')
print(l[1].upper())

for n in names:
    print(n[0]+'.')