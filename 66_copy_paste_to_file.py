#!/home/dell/.local/share/virtualenvs/python-django-bundle-lXSQ1xu5/bin/python
from sys import argv, exit

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")
print("Press 'Enter' to continue ")
print('Press "e" or "exit" to canel')

a = input(' ')
if a == 'e' or a == 'exit':
    exit(0)

file_1 = open(from_file)
file_1 = file_1.read()

print(f"The input file is {len(file_1)} Bytes long \n")
file_2 = open(to_file, 'w')
file_2.write(file_1)
print('Copied')

file_2.close()
