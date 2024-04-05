my_dict = {'tuple': ('tuple_1', 'tuple_2', 'tuple_3', 'tuple_4', 'tuple_5'),
           'list': ['list_1', 'list_2', 'list_3', 'list_4', 'list_5'],
           'dict': {'dict_1': 'd_1', 'dict_2': 'd_2', 'dict_3': 'd_3', 'dict_4': 'd_4', 'dict_5': 'd_5'},
           'set': {'set_1', 'set_2', 'set_3', 'set_4', 'set_5'}
           }

my_tuple = my_dict.get('tuple')
print(my_tuple[-1])

my_list = my_dict.get('list')
my_list.append('list_6')
my_list.pop(1)

my_new_dict = my_dict.get('dict')
my_new_dict['i am a tuple'] = 'new value'
del my_new_dict['dict_2']

my_set = my_dict.get('set')
my_set.add('set_6')
my_set.remove('set_1')

print(my_dict)
