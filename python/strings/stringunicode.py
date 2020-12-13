"""
Each character has a number assigned to it. When you write a character, it is converted to its number, and that is stored instead to save space. Python uses the standard Unicode encoding (which extends the popular ASCII encoding to new symbols and alphabets). For example, ord('a') give the Unicode number for the character, a, which is 97.

Let's look at the Unicode of the characters in our string:
"""

myString = "I love Python!!"

print(myString)

for c in myString:
    print(c, ord(c))
