numbers = list(map(int,(input("enter numbers").split())))
results = filter(lambda x:(x % 13 == 0), numbers)
print(list(results))

