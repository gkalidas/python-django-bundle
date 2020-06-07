# while with dictionary and boolean

users = ['hai', 'mana', '**', 'gyan', 'Yaha']
activated_users = []

while users:
    current_user = users.pop()
    activated_users.append(current_user)

print(activated_users)
