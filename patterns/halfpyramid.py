# Demonstrating the use of '\n'

# print("hello",end ="")    
# print("\nHii\n",end="")
# print("me")

rows = int(input("Enter no of rows"))
def halfPyramid(n):
    for row in range(rows):
        for col in range(row +1):
            print("*",end = " ")
        print("\n")

halfPyramid(rows)
    