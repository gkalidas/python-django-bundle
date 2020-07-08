# function which returns another functions is called as
# decoration function/s

# # uncomment below code
# # simple example
# def apply_ones(func, args):
#     return func(args)


# def add_ten(x):
#     return x + 10


# print(apply_ones(add_ten, 20))
# # simple example ends here


# # uncomment below code
# # difficulty level medium
# # example two
# def apply_twice(func, args):
#     return func(func(args))


# def add_ten(x):
#     return x + 10

# print(apply_twice(add_ten, 20))
# # example two ends here

# anonymous functions

# def test(func, args):
#     return func(args)


# print(test(lambda x: 3 * x, 5))

# # The above code is equivalent to
# # the following function

# # def lambda_1(x):
# #     return 3 * x

# # lambda example 2
print("lambda ", (lambda x: x**2 + 5*x + 4)(6))


def test(x):
    return x**2 + 5*x + 4


print(test(6))
# # lambda example 2 ends here

# # lambda example 3
a = (lambda x, y: x*y)(4, 5)
print(a)
# # lambda example 3 ends here

# lambda example 4
# below method is not recommended by some of the
# git hooks so commenting
# sqr = lambda x: x * x
# add = lambda x, y: x + y

# print(sqr(5))
# print(add(sqr(5), sqr(5)))
# lambda example 4 ends here
