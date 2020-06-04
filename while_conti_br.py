# while with continue and break

i = 0
while i < 20:
    i += 1
    if i % 2 != 0:
        print('Odd')
        continue
    if i % 2 == 0:
        print(i)
