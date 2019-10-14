# x, y, z = input("enter three numbers").split(',')
x,y,z = map(int,input("enter three numbers ").split(','))
# print(y)
# print(isinstance(y,str))
# print(type(y))

if x > y:
    if x > z:
        print('{0} is largest'.format(x))
    else:
        print('{0} is largest'.format(z))
elif y > z:
    print("{0} is largest".format(y))
else:
    print('{0} is largest'.format(z))


#another way 

num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number between",num1,",",num2,"and",num3,"is",largest)
