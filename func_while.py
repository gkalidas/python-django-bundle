# function in while loop


def get_full_name(first_name, last_name):
    """
    returns full name
    """
    full_name = first_name + ' ' + last_name
    return full_name


while True:
    print('Enter "exit" or "e" to exit.')

    f_name = input('Enter your first name : ')
    if f_name == 'e' or f_name == 'exit':
        break
    l_name = input('Enter your last name : ')
    if l_name == 'e' or l_name == 'exit':
        break
    fullname = get_full_name(f_name, l_name)
    print('Welcome ', fullname)
    repeat = input('Do you want to continue? y/n ')
    if repeat == 'n' or repeat == 'no':
        break
