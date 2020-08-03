with open('text.txt', 'w') as f:
    content = "Hi there Welcome to the ...   "
    f.write(content)
f.close()

# with open('text.txt') as f:
#     content = f.read()
# print(content.lstrip())

file_path = 'test.txt'

with open(file_path) as f:
    f = f.readlines()
print(f)
