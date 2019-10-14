#In this program, you'll learn to display powers of the integer 2 using Python anonymous function.

terms = int(input("Enter number of terms"))
result = list(map(lambda x: 2 ** x, range(terms)))

for i in range(terms):
    print("2 raised to power",i,"is:",result[i])
    