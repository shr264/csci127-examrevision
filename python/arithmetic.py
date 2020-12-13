x = 6
y = x % 4
w = y**3
z = w / 2
print(x,y,w,z)
z = w // 2
print(x,y,w,z)
x,y = y,w
print(x,y,w,z)
x = y / 2
print(x,y,w,z)