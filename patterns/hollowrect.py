rows,cols = map(int,input("Enter no of rows and columns").split())
def hollowRect(n,m):
    for i in range(n):
        for j in range(m):
            if(i==0 or i==n-1 or j==0 or j== m-1):
                print("* ",end="")
            else:
                print("  ",end ="")
        print("\n")
hollowRect(rows,cols)
