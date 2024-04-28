def operation_dec(func):
    def wrapper(first, second):
        if first == second and first >= 0 and second >= 0:
            return func(first, second, '+')
        elif first > second and first >= 0 and second >= 0:
            return func(first, second, '-')
        elif second > first and first >= 0 and second >= 0:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')
    return wrapper


@operation_dec
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first_number = float(input("Enter first digit: "))
second_number = float(input("Enter second digit: "))

result = calc(first_number, second_number)

print("Operation result:", result)
