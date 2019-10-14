num1 =  int(input("Enter number"))
for i in range(1,11):
    mul = num1 * i
    print(mul,end = "\n") #end is '\n' bydefault in python!

#another way

num = int(input("Display multiplication table of? "))

# use for loop to iterate 10 times
for i in range(1, 11):
   print(num,'x',i,'=',num*i)