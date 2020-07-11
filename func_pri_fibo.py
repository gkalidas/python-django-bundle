# prime and fibonacci series


def prime_num(n):
    '''
    Check if given number is prime or not.

    reads the input from user and returns true or false based on the
    logic of prime number.
    '''
    prime = True
    for i in range(2, n):
        if n % 2 == 0:
            prime = False
    return prime

# num = int(input('Please enter number > '))

# if prime_num(num):
#     print(num, 'is a prime number.')
# else:
#     print(num, 'is not a prime number.')


def fibonacci(num):
    """
    Accepts "num" as input.

    "num" defines how many numbers we want in our
    fibonicci series.

    Returns a list with expected result.

    here we define the first and second number
    because this is how fibonacci series starts with

    first = 1
    second = 2

    example:
    1, 2, 3, 5, 8, 13,...
    """

    first = 1
    second = 2
    fibo_list = []
    for i in range(num):
        fibo_list.append(first)
        new = first + second
        first = second
        second = new
    return print(fibo_list)


n = int(input('Enter number > '))
fibonacci(n)
