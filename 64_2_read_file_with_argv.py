
# !/usr/bin/env python3
# Also run the following command
# chmod +x 64_2_read_file_with_argv.py
# to run the file
from sys import argv

script_file, file_name = argv


def read_file(file_name):
    txt = open(file_name)
    print(f'This is your file {file_name}')
    print(txt.read())


read_file(file_name)

while True:
    read_again = input('Would you like to read another file? (y/n) ')
    if read_again == 'y':
        file_name = input('Enter file name ')
        read_file(file_name)
    else:
        break
