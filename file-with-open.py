with open('text.txt', 'w') as f:
    content = "Hi there Welcome to the ...\nThis is second line "
    f.write(content)
f.close()

# with open('text.txt') as f:
#     content = f.read()
# print(content.lstrip())

# read file content as a list
file_path = 'text.txt'
with open(file_path) as f:
    f = f.readlines()

string = ''

for i in f:
    string += i.rstrip()
print(string)
