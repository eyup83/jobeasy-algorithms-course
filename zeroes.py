num = int(input('enter the a number to get rid of ending zeros: '))

#print("The original number is " + str(num))

if num == 0:
    print(num)
else:
    num = str(num)
    num = num.rstrip('0')

print(num)


