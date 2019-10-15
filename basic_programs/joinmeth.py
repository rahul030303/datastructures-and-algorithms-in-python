# list1 = ["hello","hii","my","Lovable"]
# for i in list1:
#     print("#".join(list1))

from itertools import permutations 
  
def allPermutations(str): 
       
     # Get all permutations of string 'ABC' 
    permList = permutations(str) 
    # print(permList)
    a = list(permList)
    print(a)
     # print all permutations 
    for perm in a: 
        print (''.join(perm)) 
    
        
# Driver program 
if __name__ == "__main__": 
    str = 'ABC'
    allPermutations(str) 