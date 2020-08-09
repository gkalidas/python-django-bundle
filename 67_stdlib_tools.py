from itertools import count, accumulate, takewhile, product

# starts from 3 and goes forever

for i in count(3):
    print(i)
    if i >= 11:
        break

# generates the list with adding 1, 2, 3,... to each number

nums = list(accumulate(range(7)))
print(nums)

num_takewhile = list(takewhile(lambda x: x <= 6, nums))
print("Num takewhile", num_takewhile)

vowels = ['a', 'e', 'i', 'o', 'u']

print(list(product(vowels, range(3))))
