#"Словари и множества"
my_dict = {'Alex': 2001, 'Greta': 1985, 'Max': 1980}
print(my_dict)
print(my_dict['Greta'])
print(my_dict.get('Sveta'))
my_dict.update({'Sveta': 1995,
                'Kola': 2005})
a = my_dict.pop('Max')
print(a)
print(my_dict)
my_set = {1,2,3,1,5,2,'git',True,8,5}
print(my_set)
my_set.add(0)
my_set.add(7)
my_set.remove(3)
print(my_set)

