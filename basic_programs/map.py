# x,y,z = map(int,input("enter three numbers ").split(','))
def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = [1, 2, 3, 4]
result = map(addition, numbers) # map(function,iterable)
print(tuple(result)) 

#another example
numArray = list(map(int, input("enter numbers").split()))
print(numArray)