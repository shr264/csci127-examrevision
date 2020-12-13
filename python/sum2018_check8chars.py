"""
Write a complete Python program that prompts the user for a password. If the user
entered a string with fewer than 8 characters, the program repeatedly asks until a string
with 8 or more characters is entered. The program then prints the string that was entered.
"""

#Input checking:
s = input('Enter a string: ')
while len(s) < 8:
    s = input('Enter a password with at least 8 characters: ')
print("You entered:",s)