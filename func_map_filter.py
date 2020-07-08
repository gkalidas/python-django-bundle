# function map and filter examples

# def add_six(x):
#     return x + 6


# numbers = [3, 4, 5, 6, 7]
# result = list(map(add_six, numbers))
# print(result)

# or using lamda
# numbers = [3, 4, 5, 6, 7]
# result = list(map(lambda x: x + 6, numbers))
# print(result)

# filter example

def check_num(x):
    if x % 2 == 0:
        return x


numbers = [3, 4, 5, 6, 7]
# result = list(filter(check_num, numbers))
# print(result)

# or using lambda
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)
