for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        i = 'FuzzBuzz'
        print(i)

    elif i % 3 == 0:
        i = 'Fuzz'
        print(i)

    elif i % 5 == 0:
        i = 'Buzz'
        print(i)

    else:
        print(i)
