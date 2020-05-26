# if, elif and else intro
# following program will take age as input
# and returns message based on age.

age = int(input('Please enter your age '))

if age < 18:
    print("You can't enter :|")
elif 18 < age and age < 21:
    print("You can enter :)")
elif age > 60:
    print("You are too old to come here ;)")
else:
    print("Please enter your age :|")
