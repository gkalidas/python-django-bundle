# while with dictionary and boolean

# 4
res = {}

active = True
while active:
    name = input('Please enter your name: ')
    b_date = input("Please enter your b_date: ")
    res[name] = b_date
    repeat = input('Would you like to repeat for someone else? yes/no: ')
    if repeat == 'no':
        break

for k, v in res.items():
    print('_ ', k, v)

# 3
# while True:
#     print('please enter you name')
#     name = input(': ')
#     if name == 'exit' or name == 'e':
#         break


# 2
# pets = ['cat', 'dog', 'cat', 'paliv', 'prani', 'aahe', 'cat', ]

# while 'cat' in pets:
#     # removes a 'cat' element from a list
#     pets.remove('cat')
# print(pets)

# 1
# users = ['hai', 'mana', '**', 'gyan', 'Yaha']
# activated_users = []

# while users:
#     current_user = users.pop()
#     activated_users.append(current_user)

# for i in activated_users:
#     print(i)
#     # always put a title to look it more appealing
#     print(i.title())
