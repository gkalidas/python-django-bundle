# list with for loop

l1 = ['Hi', 'my', 'name', 'is', 'Ganesh']

l2 = ['Hi', 'my', 'name', 'is', 'Pandurang']

l3 = []

for a in l1:
    for b in l2:
        if a == b:
            l3.append(a)

print(l3)
