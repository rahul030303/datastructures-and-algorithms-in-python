rows = int(input("Enter no of rows"))
cols = int(input("Enter no of columns"))
def rectPattern(n,m):
    for i in range(n):
        for j in range(m):
            print("*",end=" ")
        print("\n")
rectPattern(rows,cols)
    

