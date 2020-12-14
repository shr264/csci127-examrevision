colonies = "New Jersey, New York, New Hampshire, North Carolina"

#count number of spaces in variable colonies
print(colonies.count(' '))

# python code to slice "North"
print(colonies[-14:-9])

#python code to split the string colonies and print intials of states as NJNYNHNC
initials = ""
words = colonies.split( )
for word in words:
    initials = initials + word[0]
print(initials)