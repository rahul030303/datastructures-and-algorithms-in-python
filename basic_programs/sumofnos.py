num = int(input("enter number upto which you want to sum"))
sum = 0
while num > 0:
    sum += num
    num -= 1
print(sum)

#another way

num = int(input("enter number upto which you want to sum"))
sum = 0
for i in range(num + 1):
    sum += i
print(sum)