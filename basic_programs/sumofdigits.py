def sumofdigits(N):
    sum = 0 
    while N!= 0:
        digit = N % 10
        sum += digit
        N = N //10
    return sum
result = sumofdigits(134)
print(result)

