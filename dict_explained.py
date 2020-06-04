# dictionary in details

my_dict = {
    'numbers_1': [1, 2, 3, 4], 'numbers_2': [3, 4, 5, 6], 'count': 6
}

# print only keys

# 1
# for k in my_dict:
#     print(k)

# 2
# for k in my_dict.keys():
#     print(k)

# print only values
# for v in my_dict.values():
#     print(v)

# prints keys with values
for k, v in my_dict.items():
    if print(type(v)) is list:
        print(v)

# dictionary keys can only be int or str
