from sys import argv

file_name, user_name = argv

prompt = '> '

print(f"Hi {user_name} I'm {file_name} script.")
print("I'd like to ask you few questions.")
print(f"Do you like the {file_name} script?")
like = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(
    f"So you like {file_name},\
    you live in {lives} and you have {computer} computer.")
