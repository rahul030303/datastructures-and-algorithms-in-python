#A positive integer is called an Armstrong number of order n if

#abcd... = a ** n + b ** n + c ** n + d ** n + ...

num = int(input("Enter number"))
order = len(str(num))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print('{} is an armstrong number'.format(num))
else:
    print('{} is not an armstrong number'.format(num))


# armstrong number within an interval


for num in range(150,300):
    order = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if sum == num:
        print(num)
