#Name: Your name here
#Email: Your email here
#Date: 16 October 2017
#Program #23:  Computes the majority of 3 inputs

in1 = bool(input('Please enter in1:'))
in2 = bool(input('Please enter in2:'))
in3 = bool(input('Please enter in3:'))
out = ((in1 and in2) or (in1 and in3)) or (in2 and in3)
print(out)