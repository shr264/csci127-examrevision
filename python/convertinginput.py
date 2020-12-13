"""
int(): converts a string (series of characters) into the corresponding integer (whole number).
float(): converts a string (series of characters) into the corresponding floating point number (real number).
str(): converts a number into the corresponding sequence of characters.
"""

#Name:  your name
#Email: your email
#Date:  September 2019
#Converter example program from Lab 4


print("Welcome to Daniel's calculator!")
#1. Input the distance in kilometers (call it km)
km = float(input('Enter distance in kilometers: '))
#2. Calculate the distance in miles as 0.621371*km
miles = 0.621371*km
#3. Output miles
print("The miles are", miles)