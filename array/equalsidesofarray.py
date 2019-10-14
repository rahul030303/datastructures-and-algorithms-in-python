#incorrect
def find_even_index(arr):
    for i in arr:
        lsum = sum(arr[:i])
        rsum = sum(arr[i+1:])
        if lsum == rsum:
            return arr.index(i)
        return (-1)

b = find_even_index([1,2,3,4,3,2,1])
print(b)