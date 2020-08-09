print("Enter two numbers to divide.")
print("Enter 'q' to exit.")

while True:
    n_1 = int(input('\nPlease enter a number '))
    if n_1 == 'q':
        break
    n_2 = int(input('Please enter another number '))
    if n_2 == 'q':
        break

    try:
        answer = n_1 / n_2
    except ZeroDivisionError:
        print('The answer is zero')
    else:
        print('The answer is ', answer)
