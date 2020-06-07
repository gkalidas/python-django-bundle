# while with dictionary and boolean

users = ['hai', 'mana', '**', 'gyan', 'Yaha']
activated_users = []

while users:
    current_user = users.pop()
    activated_users.append(current_user)

for i in activated_users:
    print(i)
    # always put a title to look it more appealing
    print(i.title())
