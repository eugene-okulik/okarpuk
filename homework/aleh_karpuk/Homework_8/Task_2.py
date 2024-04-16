def fibonacci(n):
    first_digit = 0
    second_digit = 1
    for i in range(n-1):
        temp_digit = second_digit
        second_digit = first_digit + second_digit
        first_digit = temp_digit
    print(first_digit)

fibonacci(5)
fibonacci(200)
fibonacci(1000)
fibonacci(100000)
