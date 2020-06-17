# while in calculator

while True:
    c = None
    print('\n\tSIMPLE CALCULATOR\n')
    print('Enter "sub" to subtract two numbers')
    print('Enter "add" to add two numbers')
    print('Enter "mul" to multiply two numbers')
    print('Enter "div" to divide two numbers')
    print('Enter "exit" or "e" to exit')
    user_input = input('> ')

    if user_input == 'e' or user_input == 'exit':
        break
    elif user_input == 'add':
        a = float(input('please enter first number '))
        b = float(input('please enter second number '))
        c = a + b
    elif user_input == 'sub':
        a = float(input('please enter first number '))
        b = float(input('please enter second number '))
        c = a - b
    elif user_input == 'mul':
        a = float(input('please enter first number '))
        b = float(input('please enter second number '))
        c = a * b
    elif user_input == 'div':
        a = float(input('please enter first number '))
        b = float(input('please enter second number '))
        c = a / b
    else:
        print('Enter valid choice')
        print('now continue .....')
        continue
    print(f'The answer of {user_input} is {c}')

print('Exiting, Thanks for using calculator')
