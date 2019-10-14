yr = int(input("Enter any year"))
# check for laep year
if yr % 100 == 0:
    if yr % 400 == 0:
        print('leap year(century)')
    else:
        print('not a leap year(century)')
elif yr % 4 == 0:
    print('leap year')
else:
    print('not a leap year')