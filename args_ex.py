# program to test multiple args in python

# def function(*args):
#     for string in args:
#         print(string)


# function('Hi', 'we', 'are', 'working' ' with ' ' multiple arguments here.')


def function(*args):
    name = args[0]
    last_name = args[1]
    age = args[2]
    print('Welcome ', name, age, last_name)


function('John', 'Doe', 45)
