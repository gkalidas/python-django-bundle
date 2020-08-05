from sys import argv

file_name, user_name = argv
input_symbol = '> '

print(f"Hi {user_name}, how are you doing today?")
response = input(input_symbol)

# shut down the system in given time
x = [i for i in range(0, 11)]


def shut_down():
    for i in x[::-1]:
        print(i)


if response == 'nbsg':
    print("Welcome to the future gk")
else:
    print("Hi, System has recongnized an unauthorised user, shutting down in ")
    shut_down()
