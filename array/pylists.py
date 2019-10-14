#slicing
list1 = [1,3,4,5,6,7,8,9]
print(list1[-5:-1])  

# list always traverses forward

list1 = [1,3,4,5,6,7,8,9]
print(list1[-1:-5])  #wrong way of slicing a list

#List are mutable, meaning, their elements can be changed unlike string or tuple.

#We can add one item to a list using append() method or add several items using extend() method.
odd = [1, 3, 5]
odd.append(7)
# Output: [1, 3, 5, 7]
print(odd)
odd.extend([9, 11, 13])
# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)

#We can also use + operator to combine two lists. This is also called concatenation.
#The * operator repeats a list(all list items) for the given number of times.
odd = [1, 3, 5]
# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])
#Output: ["re", "rahul", "re", "rahul", "re", "rahul"]
print(["re","rahul"] * 3)

#Furthermore, we can insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.
odd = [1, 9]
odd.insert(1,3)
# Output: [1, 3, 9] 
print(odd)
odd[2:2] = [5, 7]
# Output: [1, 3, 5, 7, 9]
print(odd[3])

#We can delete one or more items from a list using the keyword del. It can even delete the list entirely.
my_list = ['p','r','o','b','l','e','m']
# delete one item
del my_list[2]
# Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(my_list)
# delete multiple items
del my_list[1:5]  
# Output: ['p', 'm']
print(my_list)
# delete entire list
del my_list       
# Error: List not defined
# print(my_list)

#We can use remove() method to remove the given item or pop() method to remove an item at the given index.
#The pop() method removes and returns the last item if index is not provided. This helps us implement lists as stacks (first in, last out data structure).
#We can also use the clear() method to empty a list.

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'o'
print(my_list.pop(1))
# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'm'
print(my_list.pop())
# Output: ['r', 'b', 'l', 'e']
print(my_list)
my_list.clear()
# Output: []
print(my_list)

#Finally, we can also delete items in a list by assigning an empty list to a slice of elements.

mylist = ['p','r','o','b','l','e','m']
mylist[2:3] = []
print(mylist)
#['p', 'r', 'b', 'l', 'e', 'm']
mylist[2:5] = []
print(mylist)
#['p', 'r', 'm']

#Methods that are available with list object in Python programming are tabulated below.
# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list

# Some examples of Python list methods:

my_list = [3, 8, 1, 6, 0, 8, 4]
# Output: 1
print(my_list.index(8))
# Output: 2
print(my_list.count(8))
my_list.sort()
# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list)
my_list.reverse()
# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)

#List Comprehension: Elegant way to create new List
#List comprehension is an elegant and concise way to create new list from an existing list in Python.
#List comprehension consists of an expression followed by for statement inside square brackets.

#Here is an example to make a list with each item being increasing power of 2.

pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)
#This code is equivalent to

pow2 = []
for x in range(10):
   pow2.append(2 ** x)
# A list comprehension can optionally contain more for or if statements. An optional if statement can filter out items for the new list. Here are some examples.

pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)
#[64, 128, 256, 512]
odd = [x for x in range(20) if x % 2 == 1]
print(odd)
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
list12 = [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
#['Python Language', 'Python Programming', 'C Language', 'C Programming']

#Other List Operations in Python

# List Membership Test
# We can test if an item exists in a list or not, using the keyword in.

my_list = ['p','r','o','b','l','e','m']
# Output: True
print('p' in my_list)
# Output: False
print('a' in my_list)
# Output: True
print('c' not in my_list)

#Iterating Through a List
#Using a for loop we can iterate though each item in a list.

for fruit in ['apple','banana','mango']:
    print("I like",fruit)