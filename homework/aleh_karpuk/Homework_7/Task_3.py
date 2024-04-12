result_1 = "результат операции: 42"
result_2 = "результат операции: 54"
result_3 = "результат работы программы: 209"
result_4 = "результат: 2"

def calc(app_output):
    func_result = int(app_output[app_output.index(':') + 2:])
    func_result += 10
    print(func_result)

calc(result_1)
calc(result_2)
calc(result_3)
calc(result_4)
