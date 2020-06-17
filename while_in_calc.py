# while in calculator

while True:
    print('please enter numbers to proceed')
    a = int(input('please enter first number '))
    b = int(input('please enter second number '))
    c = None

    print('SIMPLE CALCULATOR')
    print('Enter "sub" to subtract two numbers')
    print('Enter "add" to add two numbers')
    print('Enter "mul" to multiply two numbers')
    print('Enter "div" to divide two numbers')
    print('Enter "exit" or "e" to exit')
    user_input = input('> ')

    if user_input == 'e' or user_input == 'exit':
        break
    elif user_input == 'add':
        c = a + b
    elif user_input == 'sub':
        c = a - b
    elif user_input == 'mul':
        c = a * b
    elif user_input == 'div':
        c = a / b
    else:
        print('Enter valid choice')
    if c:
        print(c)

print('Exiting, Thanks for using calculator')
