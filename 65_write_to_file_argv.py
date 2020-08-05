from sys import argv, exit

script, file_name = argv

print(f'We are going to erase {file_name}')
print("Press 'Enter' to continue ")
print('Press "e" or "exit" to canel')

a = input(' ')
if a == 'e' or a == 'exit':
    exit(0)

print(f'Opening file {file_name}')
target = open(file_name, 'w')
print(f'Truncating the file {file_name}')
target.truncate()

print("Now I'm going to ask you few questions")

line1 = input('Line 1 ')
line2 = input('Line 2 ')
line3 = input('Line 3 ')

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Now we are closing the file.")
target.close()
