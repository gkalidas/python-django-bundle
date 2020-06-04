# dictionary with for

# d = {
#     'key_1': {'name': 'John', 'age': 34, 'family_name': 'Doe'},
#     'key_2': {'name': 'John1', 'age':36, 'family_name': 'Loe'},
#     'key_3': {'name': 'John2', 'age':38, 'family_name': 'Joe'}
# }

# print items from dictionary
# for key, value in d.items():
#     print key, value pair
#     print(key, value)
#     print only values using key
#     print(d[key])

d = {
    'movie_1': 2001,
    'movie_2': 2001,
    'movie_3': 2002,
    'movie_4': 2002,
    'movie_5': 2003,
    'movie_6': 2003,
    'movie_7': 2004
}

year = int(input('Please enter movie year '))

# writing items to the list with condition
my_list = [k for (k, v) in d.items() if v == year]
print(my_list)
