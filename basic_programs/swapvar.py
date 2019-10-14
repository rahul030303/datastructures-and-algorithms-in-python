x, y = input("enter x & y").split()
y,x = x,y
print("x=",x)
print("y=",y)

x = int(x) ^ int(y)
print(x)
y = int(x) ^ int(y)
print(y)
x = int(x) ^ int(y)

print(x)
print(y)