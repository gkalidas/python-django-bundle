# function yeild


def mod_two(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


def yeild_string(str_x):
    word = []
    for i in str_x:
        word += i
        yield word


# print(list(mod_two(6)))
# for i in yeild_string('fake_string'):
#     print(i)

# print(lambda x:y = list(yeild_string(x)),'fake_string')
# print(map(yield_string, 'fake_string'))
