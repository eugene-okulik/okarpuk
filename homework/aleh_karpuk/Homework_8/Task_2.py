def fibonacci():
    first_digit = 0
    second_digit = 1
    yield first_digit
    yield second_digit

    while True:
        temp_digit = first_digit
        first_digit = second_digit
        second_digit = temp_digit + first_digit
        yield second_digit


count = 1

for num in fibonacci():
    if count in [5, 200, 1000, 100000]:
        print(f'{count}th number in Fibonacci sequence = {num}')
        if count == 100000:
            break
    count += 1
