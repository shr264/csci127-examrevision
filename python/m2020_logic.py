in1 = False
in2 = True
out = not in1 or in2
print(out)


in1 = False
in2 = True
out = not (not in1 and in2) or in1
print(out)

in1 = False
in2 = not False and not in1
in3 = not in1 and not in2
out = (in1 and in2) or not in3
print(out)