import random


def salary_sum(salary):
    bonus = bool(random.randint(0, 1))
    random_bonus = random.randrange(1, 10000)

    if bonus is True:
        print(f'You have a bonus - {random_bonus}. Your salary with bonus is - {salary + random_bonus}')
    else:
        print(f'No bonus this month. Your salary is - {salary}')


salary_sum(int(input('Enter your salary ')))
