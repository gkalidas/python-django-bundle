# passing dictionary as a parameter to function


def make_pizza(size, *toppings):
    print('\nmaking pizza with size ' + str(size))
    for topping in toppings:
        print('_ ', topping.title())

# make_pizza(30, 'tomato', 'cheese', 'onion')
