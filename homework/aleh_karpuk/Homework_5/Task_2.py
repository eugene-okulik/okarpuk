result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"

number1 = int(result1[result1.index(':') + 2:])
number2 = int(result2[result2.index(':') + 2:])
number3 = int(result3[result3.index(':') + 2:])

number1 += 10
number2 += 10
number3 += 10

print(number1)
print(number2)
print(number3)
