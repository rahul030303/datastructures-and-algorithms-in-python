# The syntax of rsplit() is:

# str.rsplit([separator [, maxsplit]])

# rsplit() Parameters
# The rsplit() method takes maximum of 2 parameters:

# separator (optional)- The is a delimiter. The rsplit() method splits string starting from the right at the specified separator.
# If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
# maxsplit (optional) - The maxsplit defines the maximum number of splits.
# The default value of maxsplit is -1, meaning, no limit on the number of splits.

# Return Value from rsplit()
# The rsplit() breaks the string at the separator starting from the right and returns a list of strings.

text= 'Love thy neighbor'

# splits at space
print(text.rsplit())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.rsplit(', '))

# Splitting at ':'
print(grocery.rsplit(':'))

# when maxsplit is provided, the max no of elements can be seperated is (maxsplit+1)
grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.rsplit(', ', 2))

# maxsplit: 1
print(grocery.rsplit(', ', 1))

# maxsplit: 5
print(grocery.rsplit(', ', 5))

# maxsplit: 0
print(grocery.rsplit(', ', 0))