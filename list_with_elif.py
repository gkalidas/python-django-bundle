# list with conditional statements

my_list = ['root', 'admin', 'administrator', 'haha']

# check if element exists into the list
name = str(input('Please enter your name '))
if name not in my_list:
    print('Your name is not in list, but I have added it to the list')
    my_list.append(name)
print('Welcome {}'.format(name))
print(my_list)


# check if input contains something
# n = str(input('Please enter your name '))
# if n:
#     print('Welcome {}'.format(n))
# else:
#     print('Please enter your name USER')

# check if list has items in it
# if l:
#     print(l)
# else:
#     print('List is empty.')
