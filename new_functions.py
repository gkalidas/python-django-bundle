# I'm not aware about what new functions are in this lesson
# let's get started and explore

# write a function to check if given phone number is valid or not
# number format is as follows:
# 000-000-0000


def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Here is my phone number 989-090-7676 or 334-545-3434 is my office'

for i in range(len(message)):
    phone = message[i:i+12]
    if is_phone_number(phone):
        print('Phone number found: ', phone)
