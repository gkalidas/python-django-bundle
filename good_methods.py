# some useful methods of python

random_string = '     234     '

# print(random_string.upper())
# print(random_string.lower())
# print(random_string.isalpha())
# print(random_string.isalnum())
# print(random_string.isnumeric())
# print(random_string.isdecimal())
# print(random_string.isspace())
# print(random_string.istitle())

# will add 20 spaces from right(from start)
# print(random_string.rjust(20))

# will add 20 spaces from left(from end)
# print(random_string.ljust(20))

# fill spaces with your character
# print(random_string.rjust(20, '*'))

# fill spaces on both the sides
print(random_string.center(20, '*'))

# remove spaces from string
print(random_string.strip())

# remove spaces from right side of the string
print(random_string.rstrip())

# remove spaces from left side of the string
print(random_string.lstrip())
