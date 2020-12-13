"""
You can loop through a list the same way as you loop through a string.

The split() function breaks up a string into substrings, 
throwing away the character or delimiter on which the function splits.

Then you can loop through the list just like you loop through a string to access the 
individual substrings.

For example, given the string "FridaysSaturdaysSundays", 
split('s') will break up the string into a list of days: ["Friday","Saturday","Sunday",""] throwing away the 's' characters on which it splits.

Notice that it will produce an empty string at the end because of the 's' 
character at the end of "Sundays".
"""

myString = "FridaysSaturdaysSundays"

days = myString.split('s')
print(days)

for day in days:
    print(day)
