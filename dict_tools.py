d = {
    'name': 'John',
    'age': 34,
    'family_name': 'Doe'
}

# print keys from dictionary
print(d.keys())

# print values from dictionary
print(d.values())

# print key and values together
print(d.items())

# get name from dictinary
# print(d['name'])
# print(d.get('name1', "name1 doens't exists into the dictionary"))

# deleting item from dictionary

# del d['name']
# or
# a = d.pop('name')
# print("Type of a is ", type(a))

# copy dictionary
# d2 = d.copy()

# update dictionary
d2 = {}
d2.update(d)
print(d2)
