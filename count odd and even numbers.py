n = int(input("Enter a number: "))

even_count = 0
odd_count = 0
while n > 0:
    rem = n % 10
    if rem % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    n = int(n / 10)

print("Even count : ", even_count)
print("Odd count : ", odd_count)
