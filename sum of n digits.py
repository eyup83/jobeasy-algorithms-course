from random import randint

number = int(input('input number of digits'))
e = ""
for x in range(number):
    e = str(e) + "9"
print(e)

n = randint(0, int(e))
print(n)
sum_result = 0
for digit_str in str(n):
    sum_result += int(digit_str)

print(sum_result)