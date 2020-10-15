
needed_fibo = int(input('enter the needed item number from fibo: '))
fibo_list = []
def fibonacci(n):
    fibonacci_1 = 1
    fibonacci_2 = 1

    if n == 0:
#        print(0)
        fibo_list.append(0)
    if n > 0:
#        print(fibonacci_1)
        fibo_list.append(fibonacci_1)
    if n > 1:
#        print(fibonacci_2)
        fibo_list.append(fibonacci_2)
    index = 0
    while index < n - 2:
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
        index += 1
#        print(fibonacci_2)
        fibo_list.append(fibonacci_2)


fibonacci(10)
fibo = needed_fibo - 1
print(fibo_list[fibo])

