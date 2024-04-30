PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {item[0]: int(item[1][:-1]) for item in (line.split() for line in PRICE_LIST.split('\n'))}

print(price_dict)
