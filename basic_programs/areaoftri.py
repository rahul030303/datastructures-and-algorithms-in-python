a, b, c = input("enter sides").split()
s = (int(a) + int(b) + int(c))/2
ar = (s*(s-int(a))*(s-int(b))*(s-int(c))) ** (0.5)
print(ar)

