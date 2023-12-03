def fib(n):
    fib1 = fib2 = 1

    for i in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


fibonacci_iterator = fib(200)

with open("fib.txt", "w") as file:
    for num in fibonacci_iterator:
        file.write(str(num) + "\n")