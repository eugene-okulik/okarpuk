def fibonacci():
    a, b = 0, 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b


count = 1

for num in fibonacci():
    if count in [5, 200, 1000, 100000]:
        print(f'{count} number in Fibonacci sequence: {num}')
        if count == 100000:
            break
    count += 1
