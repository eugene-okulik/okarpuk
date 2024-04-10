secret_digit = 10

while True:
    user_input = int(input('Try to get the secret digit: '))
    if user_input == secret_digit:
        break

    elif user_input != secret_digit:
        print('Sorry, but no...')
        continue

print('Got it! You win!')
