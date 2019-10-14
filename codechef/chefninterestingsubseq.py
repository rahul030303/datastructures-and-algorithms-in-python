from collections import Counter
import math
def ncr(n,r):
    fac = math.factorial
    return fac(n)//(fac(r)*fac(n-r))
t = int(input())
for j in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    d= dict(Counter(l))
    #print(d)
    z = l[k-1]
    #print(z)
    num2 = d[z]
    #print(num2)
    num1 = 0
    for i in range(n):
        if l[i] == z and i < k:
            num1+=1
    #print(num1,' ',num2)
    num = ncr(num2,num1)
    print(num)
