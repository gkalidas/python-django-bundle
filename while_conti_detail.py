# while and continue in details

i = 0
while True:
    i += 1
    if i == 3:
        print('Skippinng 3')
        continue
    if i == 5:
        print('Skipping 5')
        continue
    if i == 10:
        print('Ending the loop here.')
        break
    print(i)
print('Finished executing the program.')
