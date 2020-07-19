# defining a function to a variable


def get_sum(first, second):
    """
    This function returns sum of two given numbers
    """
    addition = first + second
    return addition


get_sum_var = get_sum(3, 4)
# print(get_sum_var)


# defining a function to a variable in a dictionary


# def get_full_name(first_name, last_name):
#     """
#     This function returns concatinate the given string and returns the same
#     """
#     full_name = first_name + ' ' + last_name
#     return full_name


# d = {
#     'first': get_full_name('Ganesh', 'Kalidas'),
#     'second': get_full_name('Deepak', 'Malhotra'),
#     'third' : get_full_name('Mahesh', 'Mane'),
# }

# print(d['first'])
# print(d['second'])


def get_full_name(first_name, last_name, middle_name=''):
    """
    This function returns full name
    """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name


print(get_full_name('Ganesh', 'Kalidas'))
print(get_full_name('Deepak', 'Mane', 'John'))
